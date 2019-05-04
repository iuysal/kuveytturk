from __future__ import absolute_import

from kuveytturk.error import KTError
from .config import *
from kuveytturk.api import API
from kuveytturk.auth import OAuthHandler

import unittest

from .config import KuveytturkTestCase, use_replay, tape


class KuveytTurkApiTests(unittest.TestCase):
    @tape.use_cassette('test_test_customer_list.yaml')
    def test_test_customer_list(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
        api = API(auth)
        r = api.test_customer_list()
        self.assertTrue(r.success)
        self.assertEqual(len(r.value), 5)

    # The following test case is intentionally left commented. It uses authorization code flow
    # for getting the access token, which requires user interaction.
    #
    # @tape.use_cassette('test_account_list.yaml')
    # def test_account_list(self):
    #     auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
    #     scopes = ['accounts']
    #     authorization_url = auth.get_authorization_url(scopes)
    #     print('Please authorize: ' + authorization_url)
    #     code = input('Enter the authorization code from the callback URL')
    #     auth.get_access_token_via_authorization_code_flow(code)
    #     self.assertTrue(auth.access_token is not None)
    #     # use the access token to verify that it is valid
    #     api = API(auth)
    #     r = api.account_list()
    #     self.assertTrue(r.success)

    @tape.use_cassette('test_bank_branch_list.yaml')
    def test_bank_branch_list(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
        auth.get_access_token_via_client_credentials_flow(['public'])
        api = API(auth)
        r = api.bank_branch_list(bankId=205, cityId=34)
        self.assertTrue(r.success)

        try:
            r = api.bank_branch_list(bankId=205, cityId=34)
        except KTError as error:
            self.assertTrue('cityId' in error.reason)

    @tape.use_cassette('test_collection_list.yaml')
    def test_collection_list(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
        api = API(auth)
        data = {
          "accountNumber": 8002577,
          "accountSuffix": 1,
          "processId": 421553,
          "isPTTCollection": "false"
        }
        r = api.collection_list(data)
        self.assertTrue(r.success)

    @tape.use_cassette('test_generic_request.yaml')
    def test_generic_request(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
        api = API(auth)
        endpoint_params = {
            'path': '/v1/data/testcustomers',
            'method': 'GET',
            'scope': 'public',
            'authorization_flow': 'client credentials'
        }
        r = api.generic_request(endpoint_params)
        self.assertTrue(r.success)
        self.assertEqual(len(r.value), 5)


if __name__ == '__main__':
    unittest.main()