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
    response = api.test_customer_list()
except KTError as err:
    pass

for customerId in response.value:
    print(customerId)