import phpsap,requests as rq

apiKey='rcjhhmwr'
username='username'

sap_payload=dict(username=username,apiKey=apiKey)
wallet_balance_request=rq.get(phpsap.payment_balance_url,json=sap_payload, headers=phpsap.headers)
print(wallet_balance_request.text)