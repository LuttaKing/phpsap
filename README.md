# !!!!important note before you start

still learning how to upload python modules to PYPI so for now you will have to 
manually  DOWNLOAD THE PHPSAP.py into your project directory :o

# Python wrapper for PHP SAP - SMS, AIRTIME, PAYMENTS

This is a python wrapper for the phpsap API that enables python developers to easily integrate SMS,Airtime and Mobile payments using MPESA into their dynamic web applications.It is very easy to get started by creating an account and grabbing an API Key.Upon creation of an account a SAP wallet is automatically created for you,you will have to top it up with cash to start using our API to send SMS and distribute airtime.For mobile payments using MPESA a payments wallet is also automatically created for you, this is where all payments made to your application will be collected and managed. Simply hit this link to get started https://renthero.co.ke/phpsap

# Sending sms
```Python
 
import phpsap,requests as rq

phpsap.apiKey='your api key'
phpsap.username='your userNAMEZ'

Receiver='put phone number beginning with +254'
Message='Example text message.Lutta is awesome :o'

sms_payload=dict(username=phpsap.username,apiKey=phpsap.apiKey,Receiver=Receiver,Message=Message)
sms_request = rq.get(phpsap.sms_url,json=sms_payload, headers=phpsap.headers)

print(sms_request.text)

```
# Sending airtime
```python

import phpsap,requests as rq

apiKey='your key'
username='username'

PhoneNumber='put phone number'
Amount='10' # should be string minimum 10

airtime_payload=dict(username=username,apiKey=apiKey,Receiver=PhoneNumber,Amount=Amount)
airtime_request = rq.get(phpsap.airtime_url,json=airtime_payload, headers=phpsap.headers)
print(airtime_request.text)
```

# Checking sap balance
```python

import phpsap,requests as rq

apiKey='your api key'
username='sir_lutta'

sap_payload=dict(username=username,apiKey=apiKey)
sap_balance_request=rq.get(phpsap.sap_balance_url,json=sap_payload, headers=phpsap.headers)
print(sap_balance_request.text)
```

# Wallet balance
```python
import phpsap,requests as rq

apiKey='rcjhhmwjkghkjfhkygfuuuuuuuuuuuuuuuuur'
username='username'

sap_payload=dict(username=username,apiKey=apiKey)
wallet_balance_request=rq.get(phpsap.payment_balance_url,json=sap_payload, headers=phpsap.headers)
print(wallet_balance_request.text)
```

# Payment transfer
```python
import phpsap,requests as rq

apiKey='your key'
username='username'

DestinationAccountName='account name'
Amount='amount'

payments_transfer_payload=dict(username=username,apiKey=apiKey,DestinationAccountName=DestinationAccountName,Amount=Amount)
payment_trans_request= rq.get(phpsap.payments_trans_url,json=payments_transfer_payload, headers=phpsap.headers)

print(payment_trans_request.text)
```
# b2b transfer
```python
import phpsap,requests as rq

apiKey='your key'
username='username'

paybill='paybill no'
Amount='amount'
acc_no='account number'

b2b_payload=dict(username=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2b_request=rq.get(phpsap.mobileb2b_url,json=b2b_payload,headers=phpsap.headers)
print(b2b_request.text)
```
# b2c transfer
```python

import phpsap,requests as rq

apiKey='your key'
username='username'

PhoneNumber='number'
Amount='amount'

b2c_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)

b2c_request = rq.get(phpsap.mobileb2c_url,json=b2c_payload, headers=phpsap.headers)
print(b2c_request.text)
```
# mobile stk push
```python

import phpsap,requests as rq

apiKey='your key'
username='username'

PhoneNumber='put phone number'
Amount='10' #should be string minimum 10

mobile_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
mobile_request = rq.get(phpsap.Mobile_Push_url,json=mobile_payload, headers=phpsap.headers)
print(mobile_request.text)
```
# payment validation

```python
import phpsap,requests as rq

apiKey='your key'
username='username'
MPESATransactionID='mpesa id'

validation_payload=dict(username=username,apiKey=apiKey,MPESATransactionID=MPESATransactionID)
validation_request=rq.get(phpsap.validation_url,json=validation_payload,headers=phpsap.headers)
print(validation_request.text)
```
