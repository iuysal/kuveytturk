from __future__ import absolute_import

from .config import *
from kuveytturk.api import API
from kuveytturk.auth import OAuthHandler

import unittest


class KuveytTurkAuthTests(unittest.TestCase):

    def test_client_credentials_access_token(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)

        # test getting access token
        auth.get_access_token_via_client_credentials_flow(['public'])
        self.assert_(auth.access_token is not None)

        # use the access token to verify that it is valid
        api = API(auth)
        r = api.test_customer_list()
        self.assert_(r.success)

    def test_authorization_code_access_token(self):
        auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
        scopes = ['accounts']
        authorization_url = auth.get_authorization_url(scopes)
        print('Please authorize: ' + authorization_url)
        code = input('Enter the authorization code from the callback URL')
        auth.get_access_token_via_authorization_code_flow(code)
        self.assert_(auth.access_token is not None)
        # use the access token to verify that it is valid
        api = API(auth)
        r = api.account_list()
        self.assert_(r.success)
