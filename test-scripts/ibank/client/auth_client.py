import json
import requests

from ibank.settings import ibank_auth_url


class AuthClient:
    def get_access_token(self, login) -> str:
        request_body = {
            "method": "FUTURAE",
            "login": login,
            "code": "123456"
        }

        response = requests.post(
            url=ibank_auth_url,
            data=json.dumps(request_body),
            headers={
                'Content-Type': 'application/json'
            }
        )

        return response.json().get('accessToken')
