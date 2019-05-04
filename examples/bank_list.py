from kuveytturk.api import API
from kuveytturk.auth import OAuthHandler
from kuveytturk.error import KTError

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''
PRIVATE_KEY = ''

# Create an authentication handler with your credentials
auth = OAuthHandler(CLIENT_ID, CLIENT_SECRET, PRIVATE_KEY, REDIRECT_URI)

# Then create an API instance using this authentication handler
api = API(auth)

try:
    # Since this endpoint is not defined as a method in this library,
    # we use the generic_request method to call any endpoint.
    response = api.generic_request(
        {
            'path': '/v1/data/banks',
            'method': 'GET',
            'scope': 'public',
            'authorization_flow': 'client credentials'
        })
except KTError as err:
    pass
