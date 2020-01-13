import phpsap,requests as rq

apiKey='your keysy'
username='usernamvjjea'

paybill='paybill no'
Amount='amount'
acc_no='accohjjunt_numbers'

b2b_payload=dict(username=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.text)
