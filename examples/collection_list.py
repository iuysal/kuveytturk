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
    response = api.collection_list(
        {
            "accountNumber": 8002577,
            "accountSuffix": 1,
            "processId": 421553,
            "isPTTCollection": "false"
        }
    )
except KTError as err:
    pass
