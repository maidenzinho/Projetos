from requests import get, post
from rich import print
from urllib3 import disable_warnings
disable_warnings()

import json

def main() -> None:

        request_body = {
                "client_id": "xxx",
                "client_secret": "xxx",
                "grant_type": "client_credentials"
        }

        token_url = "https://xxx/iso/oauth2/token"

        print(f"[cyan][!] Generating token with {token_url}[/]")

        response = post(token_url, verify=False, data=request_body)
        status_code = response.status_code
        body = response.text

        parsed_json = json.loads(body)
        access_token = parsed_json['access_token']
        print(f"[green][+] Token generated: [/][yellow]{access_token}[/]\n")

        get_credential(access_token)

def get_credential(access_token) -> None:
        credential_id = int(input("[?] Type the credential ID to get: "))

        headers = {
                "Authorization": f"Bearer {access_token}"
        }

        credential_url = f"https://xxx/iso/pam/credential/{credential_id}"
        response = get(credential_url, headers=headers, verify=False)
        body = response.text
        print(body)

        get_device(access_token)

def get_device(access_token) -> None:
        print("\n")
        device_id = int(input("[?] Type the device ID to get: "))
        headers = {
                "Authorization": f"Bearer {access_token}"
        }

        device_url = f"https://xxx/iso/pam/device/{device_id}"
        response = get(device_url, headers=headers, verify=False)
        body = response.text
        print(body)

        get_all_passwords(access_token)

def get_all_passwords(access_token) -> None:
        print("\n[yellow][!] Extracting all passwords with Bearer token [/]")

        headers = {
                "Authorization": f"Bearer {access_token}"
        }

        passwords_url = f"https://xxx/iso/pam/credential"
        response = get(passwords_url, headers=headers, verify=False)
        body = response.text
        print(body)

main()