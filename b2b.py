import phpsap,requests as rq

apiKey='your key'
username='username'

paybill='paybill no'
Amount='amount'
acc_no='account number'

b2b_payload=dict(username=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.text)