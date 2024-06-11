import unittest
from unittest.mock import patch, MagicMock
from andrea_library.aqua_api import api_authentication


class TestAuthentication(unittest.TestCase):
    @patch('andrea_library.aqua_api.requests.post')
    def test_authentication_success(self, mock_post):
        # Mock the API response for successful authentication
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 200,
            'code': 0,
            'data': 'kpXVCJ9.eyJ1c2VyX2lk'
        }
        mock_post.return_value = mock_response

        # API credentials
        base_url = 'https://eu-1.api.cloudsploit.com'
        api_key = 'mock_api_key'
        api_secret = 'mock_api_secret'
        api_methods = '["ANY"]'
        aqua_role = 'api_admin_role'

        result = api_authentication(base_url, api_key, api_secret, aqua_role, api_methods)

        # Verify the result contains the expected data
        self.assertIn('data', result.json())
        self.assertEqual(result.status_code, 200)

    @patch('andrea_library.aqua_api.requests.post')
    def test_authentication_failure(self, mock_post):
        # Mock the API response for failed authentication
        mock_response = MagicMock()
        mock_response.status_code = 403  # Unauthorized status code
        mock_response.json.return_value = {
            'status': 403,
            'id': 'cedf3a57-1b0a-4057-8dba-b119e4197c32',
            'code': 1,
            'message': 'Access denied',
            'errors': ['API request signature is invalid.']
        }
        mock_post.return_value = mock_response

        # API credentials
        base_url = 'https://eu-1.api.cloudsploit.com'
        api_key = 'invalid_mock_api_key'
        api_secret = 'invalid_mock_api_secret'
        api_methods = '["ANY"]'
        aqua_role = 'api_admin_role'

        result = api_authentication(base_url, api_key, api_secret, aqua_role, api_methods)

        # Verify the authentication failure response
        self.assertNotIn('data', result.json())
        self.assertEqual(result.status_code, 403)


if __name__ == '__main__':
    unittest.main()
