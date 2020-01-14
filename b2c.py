import phpsap,requests as rq

apiKey='your key'
username='usefrname'

PhoneNumber='numfber'
Amount='amount'

b2c_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)

b2c_request = rq.get(phpsap.mobileb2c_url,json=b2c_payload, headers=phpsap.headers)
print(b2c_request.text)
