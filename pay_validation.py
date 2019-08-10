import phpsap,requests as rq

apiKey='your key'
username='username'
MPESATransactionID='mpesa id'

validation_payload=dict(username=username,apiKey=apiKey,MPESATransactionID=MPESATransactionID)
validation_request=rq.get(phpsap.validation_url,json=validation_payload,headers=phpsap.headers)
print(validation_request.text)