import json,requests

headers = {
            'Accept': 'application/json'
        }
response = requests.get('https://official-joke-api.appspot.com/random_joke', headers=headers)
print(response)

if response.status_code == 200:
    datum =  json.loads(response.content.decode('utf-8'))
    setup = datum['setup']
    punchline = datum['punchline']
    quote = setup + '\n' + punchline
else:
    quote = "A joke"

print(quote)