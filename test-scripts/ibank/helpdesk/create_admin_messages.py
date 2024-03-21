import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder
from random import randint

from ibank.settings_admin import ibank_url_admin, ibank_jwt_token_admin


def create_message():
    message_body = {
        "managerId": "CSO",
        "messageTitle": "test_test_{}".format(randint(1, 9999)),
        "messageBody": "test message 1",
        "companyCif": "006609",
        "messageDirection":"IN",
        "managerLogin": "cbs-manager",
        "messageType": 0,
        "messageStatus": 0,
        "sendTo": "user",
        "receiver": "fronttest"
    }

    mp_encoder = MultipartEncoder(
        fields={
            'data': json.dumps(message_body),
            # plain file object, no filename or mime type produces a
            # Content-Disposition header with just the part name
            # 'spam': ('spam.txt', open('spam.txt', 'rb'), 'text/plain'),
        }
    )

    response = requests.post(
        url=ibank_url_admin,
        data=mp_encoder,
        headers={
            'Content-Type': mp_encoder.content_type,
            'Authorization': 'Bearer {}'.format(ibank_jwt_token_admin)

        }
    )

    print(response)
    print(response.content)


for i in range(1000):
    create_message()