import phpsap,requests as rq

apiKey='your kevsy'
username='usernajjea'

paybill='payhbilln
Amount='amoufdffgdfgsfgsdfnt'
acc_no='accohjjuntmbers'

b2b_payload=dict(useame=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.tex
