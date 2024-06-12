import sys
import json
from dotenv import load_dotenv
import os
from andrea_library.aqua_functions import get_token,get_repositories

# Load environment variables from .env file
load_dotenv()

# API details
base_url = os.getenv('BASE_URL')
csp_url = os.getenv('CSP_URL')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
api_methods = os.getenv('API_METHODS')
aqua_role = os.getenv('AQUA_ROLE')

# Authentication
# Call the get_token function
try:
    token = get_token(base_url, api_key, api_secret, aqua_role, api_methods)

except Exception as e:
    # Handle the error as needed (e.g., logging, displaying an error message to the user)
    print(f'Error occurred: {e}')
    sys.exit(1)

# List repos
page = 1
page_size = 200
registry = "Docker Hub"

try:
    repos = get_repositories(csp_url, token, page, page_size, registry)
    print(json.dumps(repos))

except Exception as e:
    # Handle the error as needed (e.g., logging, displaying an error message to the user)
    print(json.dumps({"Error occurred": e}))