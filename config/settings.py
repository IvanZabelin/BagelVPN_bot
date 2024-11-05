from decouple import config
from outline_vpn.outline_vpn import OutlineVPN


token = config('TOKEN_BOT')
pay_secret_key = config('PAY_SECRET_KEY')
api_url = config('API_URL')
cert_sha256 = config('CERT_SHA')
CURRENCY = 'RUB'
SHOP_ID = '506751'
PRICE = '15000'

client = OutlineVPN(api_url=api_url, cert_sha256=cert_sha256)
