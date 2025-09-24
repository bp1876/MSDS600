import requests
from requests_oauthlib import OAuth1
import jsonlines

api_key = "DFqNPJAB7KMh5swvPKGIudopq"
api_secret = "CLKRWTDvmaBYkYB8iuIXjbjjNCSOKKO8ckLV4RDmUGFM86rhTz"
access_token_key = "1280283562952908800-LtaEg503eTUgaIE2tHSBQ3HwaAhLn6"
access_token_secret = "Mk6l94gbY4AeemOIY4YO3M1J9trT1RKtIOLJWNhPRnqKV"

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

r = requests.get(url, auth=auth)
print(r.status_code)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with jsonlines.open('output.json', mode='w') as writer:    
    try:
        for line in r.iter_lines(decode_unicode=True):
            if line:
                writer.write(line)
    except KeyboardInterrupt:
        pass
