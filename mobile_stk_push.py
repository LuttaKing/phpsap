import phpsap,requests as rq

apiKey='your ey'
username='username'

PhoneNumber='put phone number'
Amount='10' #should be string minimum 1
mobile_payload=t(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
mobile_request = rq.(phpsap.Mobile_Push_url,json=mobile_payload, headers=phpsap.headers)
print(mobile_request.ext)
