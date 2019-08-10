import phpsap,requests as rq

phpsap.apiKey='your api key'
phpsap.username='sir_lutta'

sap_payload=dict(username=phpsap.username,apiKey=phpsap.apiKey)
sap_balance_request=rq.get(phpsap.sap_balance_url,json=sap_payload, headers=phpsap.headers)
print(sap_balance_request.text)