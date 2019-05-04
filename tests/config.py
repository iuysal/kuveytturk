import os
import unittest
import vcr

from kuveytturk.auth import OAuthHandler
from kuveytturk.api import API


oauth_client_id = os.environ.get('TEST_CLIENT_ID', '')
oauth_client_secret = os.environ.get('TEST_CLIENT_SECRET', '')
redirect_uri = os.environ.get('TEST_REDIRECT_URI', '')
private_key_file_path = os.environ.get('TEST_PRIVATE_KEY_FILE_PATH', '')
use_replay = os.environ.get('USE_REPLAY', False)


tape = vcr.VCR(
    cassette_library_dir='cassettes',
    filter_headers=['Authorization'],
    serializer='yaml',
    # Either use existing cassettes, or never use recordings:
    record_mode='none' if use_replay else 'all',
)


class KuveytturkTestCase(unittest.TestCase):
    def setUp(self):
        self.auth = create_auth()
        self.api = API(self.auth)
        self.api.retry_count = 2
        self.api.retry_delay = 0 if use_replay else 5


def get_private_key():
    with open(private_key_file_path, 'r') as f:
        private_key = f.read()
    return private_key


def create_auth():
    auth = OAuthHandler(oauth_client_id, oauth_client_secret, get_private_key(), redirect_uri)
    return auth
