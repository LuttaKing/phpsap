import requests as rq

#$ PYTHON WRAPPER FOR PHP SAP API
# FIRST PROTOTYPE

headers={
        'Referer':'https://renthero.co.ke/phpsap/developer/payments/payments_wallet_balance.php',
'Accept-Language': 'en-GB,en;q=0.5',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

apiKey='you api keys'
username='your username'

Receiver=''
Message='Php sap api testing.Long message man'
PhoneNumber=''
Amount='' #should be string
DestinationAccountName='accountName'

paybill='9298393029939839939'
acc_no='4569045649856856785'

MPESATransactionID='fjytfdydrydyy'

sms_payload=dict(username=username,apiKey=apiKey,Receiver=Receiver,Message=Message)
pwallet_payload=dict(username=username,apiKey=apiKey)
mobile_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
airtime_payload=dict(username=username,apiKey=apiKey,Receiver=Receiver,Amount=Amount)
payments_transfer_payload=dict(username=username,apiKey=apiKey,DestinationAccountName=DestinationAccountName,Amount=Amount)
b2b_payload=dict(username=username,apiKey=apiKey,DestinationChannel=paybill,DestinationAccount=acc_no,Amount=Amount)
b2c_payload=dict(username=username,apiKey=apiKey,PhoneNumber=PhoneNumber,Amount=Amount)
validation_payload=dict(username=username,apiKey=apiKey,MPESATransactionID=MPESATransactionID)


payment_balance_url='https://renthero.co.ke/phpsap/developer/payments/payments_wallet_balance.php'
sms_url='https://renthero.co.ke/phpsap/developer/payments/sms.php'
sap_balance_url='https://renthero.co.ke/phpsap/developer/payments/sap_wallet_balance.php'
Mobile_Push_url='https://renthero.co.ke/phpsap/developer/payments/lnmo.php'
airtime_url='https://renthero.co.ke/phpsap/developer/payments/airtime.php'
payments_trans_url='https://renthero.co.ke/phpsap/developer/payments/payments_wallet_transfer.php'
mobileb2b_url='https://renthero.co.ke/phpsap/developer/payments/sapb2b.php'
mobileb2c_url='https://renthero.co.ke/phpsap/developer/payments/sapb2c.php'
validation_url='https://renthero.co.ke/payments/sapc2b_validation.php'


pwallet_request = rq.get(payment_balance_url,json=pwallet_payload, headers=headers) 
sms_request = rq.get(sms_url,json=sms_payload, headers=headers)
sap_balance_request=rq.get(sap_balance_url,json=pwallet_payload, headers=headers)
mobile_request = rq.get(Mobile_Push_url,json=mobile_payload, headers=headers)
airtime_request = rq.get(airtime_url,json=airtime_payload, headers=headers)
payment_trans_request= rq.get(payments_trans_url,json=payments_transfer_payload, headers=headers)
b2b_request=rq.get(mobileb2b_url,json=b2b_payload,headers=headers)
b2c_request = rq.get(mobileb2c_url,json=mobile_payload, headers=headers)
validation_request=rq.get(validation_url,json=validation_payload,headers=headers)

#print(pwallet_request.text)
#print(sap_balance_request.text)
