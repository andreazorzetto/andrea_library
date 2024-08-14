import requests
import hmac
import hashlib
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

def api_authentication(base_url, api_key, api_secret, aqua_role, api_methods):
    timestamp = str(int(time.time()))
    api_url = f"{base_url}/v2/tokens"

    post_body_str='{"validity":240,"allowed_endpoints":' + api_methods + '}'

    # Create the string to sign
    string_to_sign = timestamp + "POST" + "/v2/tokens" + post_body_str

    # Create HMAC signature
    signature = hmac.new(api_secret.encode(), string_to_sign.encode(), hashlib.sha256).hexdigest()

    # Debugging prints
    # print("POST Body:", post_body_str)
    # print("String to Sign:", string_to_sign)
    # print("Signature:", signature)
    # print("API URL:", api_url)
    # print("BASE URL:", base_url)

    # Set up the headers for the request
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key,
        "X-Timestamp": timestamp,
        "X-Signature": signature
    }

    # Issue the signed request to get the authentication token
    try: 
        response = requests.post(api_url, headers=headers, data=post_body_str)
        print("url:", response.request.url)
        print("header:", response.request.headers)
        print("body:", response.request.body)
        print("method:", response.request.method)

        return response
    except Exception as e:
        print(e)


def api_get_repositories(csp_url, token, page, page_size, registry=None, scope=None):
    api_url = "{csp_url}/api/v2/repositories?page={page}&pagesize={page_size}&include_totals=true&order_by=name".format(
            csp_url=csp_url,
            page=page,
            page_size=page_size)

    if registry:
        api_url = "{api_url}&registry={registry}".format(
            api_url=api_url,
            registry=registry)

    elif scope:
        api_url = "{api_url}&scope={scope}".format(
            api_url=api_url,
            scope=scope)

    headers = {'Authorization': f'Bearer {token}'}

    result = requests.get(url=api_url, headers=headers, verify=False)

    return result


# api call to get enforcer groups and enforcers
def api_get_enforcer_groups(csp_url, token, enforcer_group=None, scope=None, page_index=1, page_size=100):
    api_url = "{csp_url}/api/v1/hostsbatch?page={page_index}&pagesize={page_size}".format(
            csp_url=csp_url,
            page_index=page_index,
            page_size=page_size)

    if enforcer_group:
        api_url = "{api_url}&search={enforcer_group}".format(
            api_url=api_url,
            enforcer_group=enforcer_group
        )

    if scope:
        api_url = "{api_url}&scope={scope}".format(
            api_url=api_url,
            scope=scope
        )

    headers = {'Authorization': f'Bearer {token}'}

    result = requests.get(url=api_url, headers=headers, verify=False)

    return result
