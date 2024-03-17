import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder
from random import randint

from ibank.settings import url, jwtToken


def create_message():
    message_body = {
        "managerId": "CSO",
        "messageTitle": "test_1236_{}".format(randint(1, 9999)),
        "message_body": "test message1",
        "companyCif": "006609",
        "messageDirection": "OUT",
        "managerLogin": "s.stepanov"
    }

    mp_encoder = MultipartEncoder(
        fields={
            'data': json.dumps(message_body),
            # plain file object, no filename or mime type produces a
            # Content-Disposition header with just the part name
            # 'spam': ('spam.txt', open('spam.txt', 'rb'), 'text/plain'),
        }
    )

    response = requests.put(
        url,
        data=mp_encoder,
        headers={
            'Content-Type': mp_encoder.content_type,
            'Authorization': 'Bearer {}'.format(jwtToken),

        }
    )

    print(response)
    print(response.content)


for i in range(10):
    create_message()
