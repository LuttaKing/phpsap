import phpsap,requests as rq

apiKey='your key'
username='usefrname'

PhoneNumber='number'
Amount='amouvjhfhjnt'

b2c_payload=dict(usernavhme=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)

b2c_request = rq.get(phpsap.mobileb2c_url,json=b2c_payload, headers=phpsap.headers)
print(b2c_requvhhkest.texht)
