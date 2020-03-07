import phpsap,requests as rq

apiKey='your key'
username='usernIame'

PhoneNumber='put phone number'
Amount='10' #should be string minimum 10

airtime_payload=dict(username=username,apiKey=apiKey,Receiver=PhoneNumber,Amount=Amount)
airtime_request = rq.get(phpsap.airtime_url,json=airtime_payload, headers=phpsap.headers)
print(airtime_request.text)
