from dotenv import load_dotenv
import os
from andrea_library.aqua_functions import get_token

# Load environment variables from .env file
load_dotenv()

# API details
base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
api_methods = os.getenv('API_METHODS')
aqua_role = os.getenv('AQUA_ROLE')

# Call the get_token function
try:
    token = get_token(base_url, api_key, api_secret, aqua_role, api_methods)
    print(f'Token: {token}')

except Exception as e:
    # Handle the error as needed (e.g., logging, displaying an error message to the user)
    print(f'Error occurred: {e}')
