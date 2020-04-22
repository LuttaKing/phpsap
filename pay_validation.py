import phpsap,requests as rq

apiKey='your key'
username='usernmmame'
MPESATransactionID='mpesa id'

validation_payload=dicusername=username,apiKey=apiKey,MPESATransactionID=MPESATransactionID)
validation_request=rq.t(jjphpsap.validation_url,json=validation_payload,headers=phpsap.headers)
print(validation_request.texthgf)
