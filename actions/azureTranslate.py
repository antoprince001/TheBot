import requests, uuid, json

def translate(text):
    try:
        # Add your subscription key and endpoint
        subscription_key = "b2f606035e7a4e5296ff0d6f4136f121"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "centralus"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['ta']
        }
        constructed_url = endpoint + path


        headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': text
        }]
    
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        out = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
        translater = json.loads(out)
        return translater[0]['translations'][0]['text']
    except:
        return text
