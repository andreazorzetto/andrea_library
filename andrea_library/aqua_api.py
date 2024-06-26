import requests
import time
import hmac
import hashlib
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()


def api_authentication(base_url, api_key, api_secret, aqua_role, api_methods):
    timestamp = str(int(time.time()))
    api_url = base_url + "/v2/tokens"

    # Define the body of the POST request
    post_body_str = str(
        '{"validity":240,"allowed_endpoints":' + api_methods + ',"csp_roles":["' + aqua_role + '"]}').replace(" ", "")

    # Create the string to sign
    string_to_sign = timestamp + "POST" + "/v2/tokens" + post_body_str

    # Create HMAC signature
    signature = hmac.new(api_secret.encode(), string_to_sign.encode(), hashlib.sha256).hexdigest()

    # Issue the signed request to get authentication token
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": api_key,
        "X-Timestamp": timestamp,
        "X-Signature": signature
    }

    result = requests.post(api_url, headers=headers, data=post_body_str)

    return result


def api_get_repositories(csp_url, token, page, page_size, registry=None, scope=None):
    if registry:
        api_url = "{csp_url}/api/v2/repositories?registry={registry}&page={page}&pagesize={page_size}&include_totals=true&order_by=name".format(
            csp_url=csp_url,
            registry=registry,
            page=page,
            page_size=page_size)
    elif scope:
        api_url = "{csp_url}/api/v2/repositories?scope={scope}&page={page}&pagesize={page_size}&include_totals=true&order_by=name".format(
            csp_url=csp_url,
            scope=scope,
            page=page,
            page_size=page_size)
    else:
        api_url = "{csp_url}/api/v2/repositories?page={page}&pagesize={page_size}&include_totals=true&order_by=name".format(
            csp_url=csp_url,
            page=page,
            page_size=page_size)

    headers = {'Authorization': f'Bearer {token}'}

    result = requests.get(url=api_url, headers=headers, verify=False)

    return result