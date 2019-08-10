import phpsap,requests as rq

apiKey='rcjhln5y33a9rjbv9bi8ihg1ox6tsq3fm40gnti8q290wif1sgc89f00mhc8hmwr'
username='sir_lutta'

sap_payload=dict(username=username,apiKey=apiKey)
wallet_balance_request=rq.get(phpsap.payment_balance_url,json=sap_payload, headers=phpsap.headers)
print(wallet_balance_request.text)