from andrea_library.aqua_api import api_authentication


def get_token(base_url, api_key, api_secret, aqua_role, api_methods):
    # Call the authenticate function
    result = api_authentication(base_url, api_key, api_secret, aqua_role, api_methods)

    # Extract status and token from the response
    if result.status_code == 200:
        token = result.json()['data']
        return token

    else:
        # Authentication failed
        error_message = result.json().get('message', 'Authentication failed')
        raise Exception(f'Error: {result.status_code} - {error_message}')