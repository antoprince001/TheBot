from newsapi import NewsApiClient

newsapi_apikey = '01dd9bdbb831421da729c605300ec9e2'
newsapi = NewsApiClient(api_key=newsapi_apikey)

top_headlines=newsapi.get_everything(q='jvkenvk',page=1)
print(top_headlines)