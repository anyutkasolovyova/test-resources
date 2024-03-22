from ibank.client.auth_client import AuthClient
from ibank.client.ibank_client import IBankClient

if __name__ == '__main__':
    token = AuthClient().get_access_token(login="fronttest")
    ibank_client = IBankClient(token)

    for i in range(1):
        ibank_client.create_helpdesk_message()
