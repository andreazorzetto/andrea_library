import unittest
import os
from dotenv import load_dotenv
from andrea_library.aqua_api import api_authentication

# Load environment variables from .env file
load_dotenv()


class TestAuthentication(unittest.TestCase):
    def test_authentication_success(self):
        # API credentials from environment variables
        base_url = os.getenv('BASE_URL')
        api_key = os.getenv('API_KEY')
        api_secret = os.getenv('API_SECRET')
        api_methods = os.getenv('API_METHODS')
        aqua_role = os.getenv('AQUA_ROLE')

        result = api_authentication(base_url, api_key, api_secret, aqua_role, api_methods)

        # Verify the result contains the expected data
        self.assertIn('data', result.json())
        self.assertEqual(result.status_code, 200)

    def test_authentication_failure(self):
        # API credentials from environment variables
        base_url = os.getenv('BASE_URL')
        api_key = os.getenv('INVALID_API_KEY')  # Use an invalid key for testing failure
        api_secret = os.getenv('INVALID_API_SECRET')  # Use an invalid secret for testing failure
        api_methods = os.getenv('API_METHODS')
        aqua_role = os.getenv('AQUA_ROLE')

        result = api_authentication(base_url, api_key, api_secret, aqua_role, api_methods)

        # Verify the authentication failure response
        self.assertNotIn('data', result.json())
        self.assertEqual(result.status_code, 403)


if __name__ == '__main__':
    unittest.main()
