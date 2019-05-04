import requests
import six
from six.moves.urllib.parse import urlencode

from kuveytturk.error import KTError


class OAuthHandler(object):
    """OAuth authentication handler"""
    OAUTH_HOST = 'idprep.kuveytturk.com.tr'
    OAUTH_ROOT = '/api/connect/'

    def __init__(self, client_id, client_secret, private_key, redirect_uri=None, oauth_host=OAUTH_HOST):
        """  OAuthHandler instance Constructor

        :param client_id:
        :param client_secret:
        :param private_key:
        :param redirect_uri:
        :param oauth_host: url of the identity server, default: 'idprep.kuveytturk.com.tr',
                                                                'id.kuveytturk.com.tr' for Production
        """
        if type(client_id) == six.text_type:
            client_id = client_id.encode('ascii')

        if type(client_secret) == six.text_type:
            client_secret = client_secret.encode('ascii')

        self.client_id = client_id
        self.client_secret = client_secret
        self.private_key = private_key
        self.redirect_uri = redirect_uri
        self.oauth_host=oauth_host
        self.request_token = {}
        self.access_token = None
        self.token_response = None

    def _get_oauth_url(self, endpoint, **kwargs):
        return 'https://' + self.oauth_host + self.OAUTH_ROOT + endpoint

    def get_authorization_url(self, scope='', **kwargs):
        """
        Returns the url to redirect the user to for user consent
        """
        if isinstance(scope, (list, tuple, set, frozenset)):
            scope = ' '.join(scope)
        oauth_params = {
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'scope': scope,
            'response_type': 'code'
        }
        oauth_params.update(kwargs)
        return "%s?%s" % (self._get_oauth_url('authorize', **kwargs),
                          urlencode(oauth_params))

    def get_access_token_via_authorization_code_flow(self, code, **kwargs):
        """
        After user has authorized the request and authorization code is issued,
        get access token with that code.
        """
        self.access_token = None

        url = self._get_oauth_url('token')
        data = {
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
        }
        data.update(kwargs)

        response = requests.post(url, data=data)
        self.token_response = response
        try:
            self.access_token = response.json()['access_token']
        except KeyError:
            raise KTError(response.content)

    def get_access_token_via_client_credentials_flow(self, scopes, **kwargs):
        """
        After user has authorized the request and authorization code is issued,
        get access token with that code.
        """
        self.access_token = None

        url = self._get_oauth_url('token')
        if isinstance(scopes, (list, tuple, set, frozenset)):
            scopes = ' '.join(scopes)
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': scopes,
        }
        data.update(kwargs)

        response = requests.post(url, data=data)
        self.token_response = response
        try:
            self.access_token = response.json()['access_token']
        except KeyError:
            raise KTError(response.content)
