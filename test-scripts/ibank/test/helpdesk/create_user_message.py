from ibank.client.ibank_auth_client import IbankAuthClient
from ibank.client.ibank_client import IBankClient

if __name__ == '__main__':
    token = IbankAuthClient().get_access_token(login="fronttest")
    ibank_client = IBankClient(token)

    for i in range(1):
        ibank_client.create_helpdesk_message()
