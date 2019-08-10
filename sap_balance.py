import phpsap,requests as rq

apiKey='your api key'
username='sir_lutta'

sap_payload=dict(username=username,apiKey=apiKey)
sap_balance_request=rq.get(phpsap.sap_balance_url,json=sap_payload, headers=phpsap.headers)
print(sap_balance_request.text)