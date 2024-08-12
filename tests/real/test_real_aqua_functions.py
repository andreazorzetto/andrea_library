import unittest
import os
from dotenv import load_dotenv
from andrea_library.aqua_functions import get_token

# Load environment variables from .env file
load_dotenv()


class TestGetToken(unittest.TestCase):
    def test_get_token_success(self):
        # API credentials from environment variables
        base_url = os.getenv('BASE_URL')
        api_key = os.getenv('API_KEY')
        api_secret = os.getenv('API_SECRET')
        api_methods = os.getenv('API_METHODS')
        aqua_role = os.getenv('AQUA_ROLE')

        token = get_token(base_url, api_key, api_secret, aqua_role, api_methods)
        self.assertIsNotNone(token)

    def test_get_token_failure(self):
        # API credentials from environment variables
        base_url = os.getenv('BASE_URL')
        api_key = os.getenv('INVALID_API_KEY')
        api_secret = os.getenv('INVALID_API_SECRET')
        api_methods = os.getenv('API_METHODS')
        aqua_role = os.getenv('AQUA_ROLE')

        with self.assertRaises(Exception) as context:
            get_token(base_url, api_key, api_secret, api_methods, aqua_role)
            self.assertIn('Error: 403 - Access denied', str(context.exception))


if __name__ == '__main__':
    unittest.main()
