from andrea_library.aqua_api import api_authentication
from andrea_library.aqua_api import api_get_repositories


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


def get_repositories(csp_url, token, page, page_size, registry):
    result = api_get_repositories(csp_url, token, page, page_size, registry)

    # Extract status and token from the response
    if result.status_code == 200:
        # repos = result.json()['data']
        repos = result.json()
        return repos

    else:
        # Authentication failed
        error_message = result.json().get('message', 'Authentication failed')
        raise Exception(f'Error: {result.status_code} - {error_message}')