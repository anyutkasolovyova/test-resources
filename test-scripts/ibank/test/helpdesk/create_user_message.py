from ibank.client.ibank_auth_client import IbankAuthClient
from ibank.client.ibank_client import IBankClient

if __name__ == '__main__':
    token = IbankAuthClient().get_access_token(login="fronttest")
    ibank_client = IBankClient(token)

    ibank_client.create_helpdesk_message_with_body(
        request_body={
            "managerId": "CSO",
            "messageTitle": "test_1236_13_symbols",
            "messageBody": "test message1",
            "companyCif": "006609",
            "messageDirection": "OUT",
            "managerLogin": "s.stepanov"
        }
    )

    ibank_client.create_helpdesk_message_with_body(
        request_body={
            "managerId": "CSO",
            "messageTitle": "test_1236_3000_symbols",
            "messageBody": "test message1 adk;fvjn;kvjnwkejvnekvnkvnpkw test message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkwtest message1 adk;fvjn;kvjnwkejvnekvnkvnpkw",
            "companyCif": "006609",
            "messageDirection": "OUT",
            "managerLogin": "s.stepanov"
        }
    )
