import http.client
import json
from random import randint

for i in range(10): 
    conn = http.client.HTTPSConnection("dev-ibank.bocbs.cardpay-test.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=data;')
    dataList.append('Content-Type: text/plain')
    dataList.append('')

    messageBody = {
        "managerId": "CSO",
        "messageTitle": "test_1236_{}".format(randint(1, 9999)),
        "messageBody": "test message1",
        "companyCif": "006609",
        "messageDirection": "OUT",
        "managerLogin": "s.stepanov"
    }

    dataList.append(json.dumps(messageBody))
    dataList.append('--'+boundary+'--')
    dataList.append('')
    body = '\r\n'.join(dataList).encode()

    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ3YTZiUklGR0JyNlZkOG8zbEFQcnA0TjdiQmNkVTFVeUNYZGNjUVBMVmJNIn0.eyJleHAiOjE3MTAzNzc1NjQsImlhdCI6MTcxMDM3NjA2NCwianRpIjoiMjhmMWU0MDgtZDJjMS00YTllLWI5YzYtOTBlZDFkZjU5NmQ4IiwiaXNzIjoiaHR0cHM6Ly9kZXYtc3NvLmJvY2JzLmNhcmRwYXktdGVzdC5jb20vYXV0aC9yZWFsbXMvaWJhbmsiLCJhdWQiOlsiaWJhbmstd2ViIiwiaWJhbmstYXV0aC1jbGllbnQiXSwic3ViIjoiYzZlOTVlY2YtMGNjMi00N2U1LTg5ZTctMDUzNDFhZmQwY2JkIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiaWJhbmstYXV0aC1jbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiYzEyODBhYzUtYmYyNS00NTc1LTlkZmEtZjFhOTUyOGMwZWYzIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlc291cmNlX2FjY2VzcyI6eyJpYmFuay13ZWIiOnsicm9sZXMiOlsiUk9MRV9VU0VSIiwiUk9MRV9TSUdOX1RSQU5TQUNUSU9OIiwiUk9MRV9IRUxQREVTSyIsIlJPTEVfQURNSU4iLCJST0xFX09QRU5fQVBJIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm1vYmlsZUZ1dHVyYWVVc2VySWQiOiI3MTM5NjhmOS1jMDNjLTQ0ZWMtOTY5MC1mZWM0OGMxOTE2MmUiLCJtb2JpbGVFbmFibGVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmcm9udHRlc3QiLCJlbWFpbCI6ImEua3V6bmVjaGVua292YUBzdGFibGUuY29tIn0.J3QcQdp49Lo9HGXScUTb9ssvk0AvWY0c6BdCfj46xzGZ8Sl4mY5q-G0v2ngNTPzVQZBK8apd68UmNVn4BPs0LqhWjsFRp6aov6ePETH7ZpFWA2mWrh2x3OzlZNEI0Z3XBU123nXBpTvWg2J0C_iMkv9I4ZoOYlVSNxmKFHEXj9t5vzlc6BB8hq59y0dGJlcxsB824VAfkcMInu68C892yUl4j0bIQSPsqKORy5EWFz1Row2DA8PfYatcp0i1Dt7WghW0aZ8rjl13yfjVJ6yvrOs4_GAmi0vsrfaIcLBoypkluafgvnqadlbVlDSfuuUaUsu0aV8FLNlaryzJrPmVdA',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }

    conn.request("PUT", "/api/crud/outbox", body, headers)

    res = conn.getresponse()
    data = res.read()
    print("Message {}".format(i))
    print(data.decode("utf-8"))
    