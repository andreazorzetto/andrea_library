import unittest
from unittest.mock import MagicMock
from andrea_library.aqua_functions import get_token


class TestGetToken(unittest.TestCase):
    def test_get_token_success(self):
        # Mock the api_authentication function for successful authentication
        mock_result = MagicMock()
        mock_result.status_code = 200
        mock_result.json.return_value = {'data': 'mock_token'}

        with unittest.mock.patch('andrea_library.aqua_functions.api_authentication', return_value=mock_result):
            token = get_token('mock_base_url', 'mock_api_key', 'mock_api_secret', 'mock_aqua_role', '["ANY"]')
            self.assertEqual(token, 'mock_token')

    def test_get_token_failure(self):
        # Mock the api_authentication function for failed authentication
        mock_result = MagicMock()
        mock_result.status_code = 403
        mock_result.json.return_value = {'message': 'Access denied'}

        with unittest.mock.patch('andrea_library.aqua_functions.api_authentication', return_value=mock_result):
            with self.assertRaises(Exception) as context:
                token = get_token('mock_base_url', 'invalid_api_key', 'invalid_api_secret', 'mock_aqua_role', '["ANY"]')

        self.assertIn('Error: 403 - Access denied', str(context.exception))


if __name__ == '__main__':
    unittest.main()
