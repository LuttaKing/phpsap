import phpsap,requests as rq

apiKey='yougjl kevy'
username='usernaysydrsfgzddbea'

Vv
Amount='dsg'
acc_no='accohjjrs'

b2b_payload=dict(useame=hhhusername,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.tex
