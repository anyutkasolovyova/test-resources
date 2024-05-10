from ibank.client.ibank_auth_client import IbankAuthClient
from ibank.client.ibank_client import IBankClient


def test_create_user_message_for_cso():
    token = IbankAuthClient().get_access_token(login="fronttest")
    ibank_client = IBankClient(token)

    request_body = {
        "managerId": "CSO",
        "messageTitle": "test_1236_13_symbols",
        "messageBody": "test message1",
        "companyCif": "006609",
        "messageDirection": "OUT",
        "managerLogin": "s.stepanov"
    }

    response = ibank_client.create_helpdesk_message_with_body(request_body)

    assert response is not None

    response_body = response.json()
    assert response_body['messageId'] is not None
    assert response_body['state'] == 'in_progress'
    assert response_body['type'] == 'pending-inbox'

    assert response_body['managerId'] == request_body['managerId']
    assert response_body['messageTitle'] == request_body['messageTitle']
    assert response_body['messageBody'] == request_body['messageBody']
    assert response_body['companyCif'] == request_body['companyCif']
    assert response_body['messageDirection'] == request_body['messageDirection']
    assert response_body['managerLogin'] == request_body['managerLogin']

def test_create_user_message_for_relationship():
    token = IbankAuthClient().get_access_token(login="fronttest")
    ibank_client = IBankClient(token)

    request_body = {
        "managerId": "CSO",
        "messageTitle": "test_1236_13_symbols",
        "messageBody": "test message1",
        "companyCif": "006609",
        "messageDirection": "OUT",
        "managerLogin": "s.stepanov"
    }

    response = ibank_client.create_helpdesk_message_with_body(request_body)

    assert response is not None

    response_body = response.json()
    assert response_body['messageId'] is not None
    assert response_body['state'] == 'in_progress'
    assert response_body['type'] == 'pending-inbox'

    assert response_body['managerId'] == request_body['managerId']
    assert response_body['messageTitle'] == request_body['messageTitle']
    assert response_body['messageBody'] == request_body['messageBody']
    assert response_body['companyCif'] == request_body['companyCif']
    assert response_body['messageDirection'] == request_body['messageDirection']
    assert response_body['managerLogin'] == request_body['managerLogin']