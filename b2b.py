import phpsap,requests as rq

apiKey='yougjl kevy'
username='usernaysydrsdbea'

paybill='pay4rtst
Amount='amoufujkvjddfnt'
acc_no='accohjjbers'

b2b_payload=dict(useame=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.tex
