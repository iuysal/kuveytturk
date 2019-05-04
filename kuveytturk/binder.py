import re
from urllib.parse import urlencode

import requests

import six
import sys

from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

from kuveytturk.error import KTError
from kuveytturk.utils import import_simplejson

json = import_simplejson()


def bind_api(api, endpoint_params, post_data):

    class APIMethod(object):
        path = endpoint_params['path']
        method = endpoint_params.get('method', 'GET')
        authorization_flow = endpoint_params['authorization_flow']
        scope = endpoint_params['scope']
        session = requests.Session()

        def __init__(self, **kwargs):
            self.api = api
            # If no accees token is provided
            if not self.api.auth.access_token:
                # If the authorization flow is client_credentials
                if self.authorization_flow == 'client credentials':
                    try:
                        self.api.auth.get_access_token_via_client_credentials_flow(self.scope)
                    except KTError:
                        raise
                else:
                    raise KTError('Authentication required!')

            self.host = api.host
            self.post_data = kwargs
            self.parser = kwargs.pop('parser', api.parser)
            self.session.headers = kwargs.pop('headers', {})
            self.session.headers['Authorization'] = 'Bearer ' + self.api.auth.access_token
            self.build_request_url()  # This should be called before creating the signature
            self.create_signature()

        def create_signature(self):
            text = self.api.auth.access_token
            if self.method == 'GET':
                url_parts = self.path.split('?')
                if len(url_parts) == 2:
                    text += '?' + url_parts[1]
            else:
                text += str(json.dumps(self.post_data))

            rsakey = RSA.importKey(self.api.auth.private_key)
            signer = PKCS1_v1_5.new(rsakey)
            digest = SHA256.new()
            digest.update(text.encode('utf-8'))
            sign = signer.sign(digest)
            self.session.headers['Signature'] = b64encode(sign)

        def build_request_url(self):
            used_params = set()
            if self.post_data:
                # e.g. /v1/data/banks/{bankId}/branches
                named_args = re.findall(r'\{\w+\}', self.path)
                for arg in named_args:
                    used_params.add(arg[1:-1])

                try:
                    self.path = self.path.format(**self.post_data)
                except KeyError as error:
                    raise KTError('Please provide all the required parameters! ' + str(error))

            # e.g. /v1/accounts/{suffix?}
            optional_args = re.findall(r'\{\w+\?\}', self.path)
            for arg in optional_args:
                if arg[1:-2] in self.post_data:
                    used_params.add(arg[1:-2])
                    self.path = self.path.replace(arg, self.post_data[arg[1:-2]])
                else:
                    self.path = self.path.replace(arg, '')

            # e.g. /v1/accounts/1/transactions?beginDate=2017-08-01&endDate=2017-08-01&minAmount=100
            if self.method == 'GET':
                unused_params = {}
                for k, v in self.post_data.items():
                    if k not in used_params:
                        unused_params[k] = v
                if unused_params:
                    self.path = "%s?%s" % (self.path, urlencode(unused_params))

        def execute(self):
            full_url = self.host + self.path

            # Execute request
            try:
                resp = self.session.request(self.method,
                                            full_url,
                                            json=self.post_data,
                                            timeout=self.api.timeout)
            except Exception as e:
                six.reraise(KTError, KTError('Failed to send request: %s' % e), sys.exc_info()[2])

            self.api.last_response = resp

            # If 401 Unauthorized access is received
            if resp.status_code == 401:
                raise KTError('Unauthorized access!')

            # Parse the response payload
            result = self.parser.parse(resp.text)
            return result

    api_method = APIMethod(**post_data)
    return api_method.execute()
