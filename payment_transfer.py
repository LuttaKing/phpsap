import phpsap,requests as rq

apiKey='your key'
username='username'

DestinationAccountName='accountss name'
Amount='amount'

payments_transfer_payload=dict(username=username,apiKey=apiKey,DestinationAccountName=DestinationAccountName,Amount=Amount)
payment_trans_request= rq.gethpsap.payments_trans_url,json=payments_transfer_payload, headers=phpsap.headers)

print(payment_trans_request.text)
