import phpsap,requests as rq

apiKey='your key'
username='username'

PhoneNumber='put phone number'
Amount='10' #should be string minimum 10

mobile_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
mobile_request = rq.get(phpsap.Mobile_Push_url,json=mobile_payload, headers=phpsap.headers)
print(mobile_request.text)