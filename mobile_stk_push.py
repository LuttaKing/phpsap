import phpsap,requests as rq

phpsap.apiKey='your key'
phpsap.username='username'

PhoneNumber='put phone number'
Amount='10' #should be string minimum 10

mobile_payload=dict(username=phpsap.username,apiKey=phpsap.apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
mobile_request = rq.get(phpsap.Mobile_Push_url,json=mobile_payload, headers=phpsap.headers)
print(mobile_request.text)