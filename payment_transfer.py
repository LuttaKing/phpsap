import phpsap,requests as rq

apiKey='your key'
username='username'

DestinationAccountName='account name'
Amount='amount'

payments_transfer_payload=dict(username=username,apiKey=apiKey,DestinationAccountName=DestinationAccountName,Amount=Amount)
payment_trans_request= rq.get(phpsap.payments_trans_url,json=payments_transfer_payload, headers=phpsap.headers)

print(payment_trans_request.text)