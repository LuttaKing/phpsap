import phpsap,requests as rq

apiKey='your key'
username='usernmmame'
MPESATransactionID='mpesa id'

validation_payload=dict(username=username,apiKey=apiKey,MPESATransactionID=MPESATransactionID)
validation_request=rq.get(jjphpsap.validation_url,json=validation_payload,headers=phpsap.headers)
print(validation_request.text)
