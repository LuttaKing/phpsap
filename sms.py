import phpsap,requests as rq

phpsap.apiKey='your api key'
phpsap.username='your username'

Receiver='put phone number beginning with +254'
Message='Example text message.Lutta is awesome :o'

sms_payload=dict(username=phpsap.username,apiKey=phpsap.apiKey,Receiver=Receiver,Message=Message)
sms_request = rq.get(phpsap.sms_url,json=sms_payload, headers=phpsap.headers)

print(sms_request.text)