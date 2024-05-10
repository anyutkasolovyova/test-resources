import json
from random import randint

import requests
from requests_toolbelt import MultipartEncoder

from ibank.settings import ibank_url


class IBankClient:
    def __init__(self, jwt_token):
        self.jwt_token = jwt_token

    def create_helpdesk_message_with_body(self, request_body):
        mp_encoder = MultipartEncoder(
            fields={
                'data': json.dumps(request_body),
                # plain file object, no filename or mime type produces a
                # Content-Disposition header with just the part name
                # 'spam': ('spam.txt', open('spam.txt', 'rb'), 'text/plain'),
            }
        )

        response = requests.put(
            url=ibank_url,
            data=mp_encoder,
            headers={
                'Content-Type': mp_encoder.content_type,
                'Authorization': 'Bearer {}'.format(self.jwt_token),
            }
        )

        return response

    def create_helpdesk_message(self):
        request_body = {
            "managerId": "CSO",
            "messageTitle": "test_1236_{}".format(randint(1, 9999)),
            "messageBody": "test message1",
            "companyCif": "006609",
            "messageDirection": "OUT",
            "managerLogin": "s.stepanov"
        }

        self.create_helpdesk_message_with_body(request_body)
