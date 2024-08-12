from andrea_library.aqua_api import api_authentication
from andrea_library.aqua_api import api_get_repositories
from andrea_library.aqua_api import api_get_enforcer_groups


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


# Return a dict with a list and count of enforcer groups
# Optionally filtered by scope
def get_enforcer_groups(csp_url, token, scope=None, page_index=1, page_size=100):
    enforcer_groups = {
        "count": 0,
        "result": []
    }

    while True:
        result = api_get_enforcer_groups(csp_url, token, None, scope, page_index, page_size)

        if result.status_code == 200:
            if result.json()["result"]:
                # save count
                enforcer_groups["count"] = result.json()["count"]

                # add enforcer groups to list
                enforcer_groups["result"] += result.json()["result"]

                # increase page number
                page_index += 1

            # found all enforcers
            else:
                break
    return enforcer_groups