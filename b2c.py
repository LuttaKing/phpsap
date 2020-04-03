import phpsap,requests as rq

apiKey='youey'
username='usnam'

PhoneNumber='nuber'
Amount='amoujnt'

b2c_payload=dict(usernavggv=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
b2c_request = rq.get(phpsap.mobileb2c_url,json=b2c_payload, headers=phpsap.headers)
print(b2c_requvhhkest.texht)
