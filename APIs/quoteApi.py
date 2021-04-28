import json,requests

headers = {
            'Accept': 'application/json'
        }
response = requests.get('https://api.quotable.io/random', headers=headers)
print(response)

if response.status_code == 200:
    datum =  json.loads(response.content.decode('utf-8'))
    quote = datum['content']
else:
    quote = "Fake it till you make it"

print(quote)