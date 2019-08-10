import phpsap,requests as rq

phpsap.apiKey='your api key'
phpsap.username='username'

sap_payload=dict(username=phpsap.username,apiKey=phpsap.apiKey)
wallet_balance_request=rq.get(phpsap.payment_balance_url,json=sap_payload, headers=phpsap.headers)
print(wallet_balance_request.text)