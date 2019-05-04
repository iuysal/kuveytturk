from kuveytturk.api import API
from kuveytturk.auth import OAuthHandler
from kuveytturk.error import KTError

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''
PRIVATE_KEY = ''

# Create an authentication handler with your credentials
auth = OAuthHandler(CLIENT_ID, CLIENT_SECRET, PRIVATE_KEY, REDIRECT_URI)

# Then create an authorization url to get consent of the user.
scopes = ['accounts']
authorization_url = auth.get_authorization_url(scopes)

print('Please authorize: ' + authorization_url)
code = input('Enter the authorization code from the callback URL')

# Using the authroziation code, request an access token
auth.get_access_token_via_authorization_code_flow(code)

# Then create an API instance using this authentication handler
api = API(auth)

# Finally make the api request to retrieve the list of account information
# of the authenticated customer.
try:
    response = api.account_list()
except KTError as err:
    pass

print(response.value)
