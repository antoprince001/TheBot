# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions"

from typing import Any, Text, Dict, List
import json
import requests
import wikipedia 
from newsapi import NewsApiClient
from actions.azureTranslate import translate
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRespondQuote(Action):

    def name(self) -> Text:
        return "action_respond_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        headers = {
            'Accept': 'application/json'
        }
        # https://github.com/lukePeavey/quotable
        response = requests.get('https://api.quotable.io/random', headers=headers)

        if response.status_code == 200:
            datum =  json.loads(response.content.decode('utf-8'))
            quote = datum['content']
        else:
            quote = "யாதும் ஊரே யாவரும் கேளிர்"
        dispatcher.utter_message(text=quote)

        return []


class ActionFindAndShowWeather(Action):

    def name(self) -> Text:
        return "action_find_and_show_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city_name = tracker.get_slot("city")
        api_key = "df6d7566e1ff99c3e1f91ec11f22d5e9"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url) 
  
        weather = response.json() 
  
        if weather["cod"] != "404": 
            datum = weather["main"]
            celsius = str(int(datum['temp'])-273) + ""
            output = 'தற்போதைய வானிலை ' + translate(weather['weather'][0]['description']) + ' வெப்பநிலை '+celsius+'° Celsius'
        else:
            output = 'என்னை மன்னிக்கவும் ! என்னால் வானிலை தரவை கண்டுபிடிக்க முடியவில்லை'
        
        dispatcher.utter_message(text=output)

        return []


class ActionRespondJoke(Action):

    def name(self) -> Text:
        return "action_respond_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get('https://official-joke-api.appspot.com/random_joke', headers=headers)

        if response.status_code == 200:
            datum =  json.loads(response.content.decode('utf-8'))
            setup = translate(datum['setup'])
            punchline = translate(datum['punchline'])
            joke = 'இங்கே ஒரு நகைச்சுவை' + '\n' + setup + '\n' + punchline
        else:
            joke = "நகைச்சுவை"
        dispatcher.utter_message(text=joke)

        return []

class ActionFindAndShowNews(Action):

    def name(self) -> Text:
        return "action_find_and_show_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topic_name = tracker.get_slot("topic")
        newsapi_apikey = '01dd9bdbb831421da729c605300ec9e2'
        newsapi = NewsApiClient(api_key=newsapi_apikey)
        
        top_headlines=newsapi.get_everything(q=topic_name,page=1)
        if(top_headlines['totalResults']>0):
            news = top_headlines['articles'][0]  
            datum = translate(news["title"])
            link = news["url"]
        else:
            datum = 'என்னை மன்னிக்கவும் ! செய்தித் தரவை என்னால் கண்டுபிடிக்க முடியவில்லை'
            link = ''
        
        dispatcher.utter_message(text=datum,attachment =link)

        return []

class ActionFindAndShowWiki(Action):

    def name(self) -> Text:
        return "action_find_and_show_wiki"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = tracker.get_slot("topic")
        
        try:
            if(query != None):
                result = 'Acccording to wikipedia,'+ wikipedia.summary(query, sentences=2)
                datum = translate(result)
            else:
                result = 'Try again'
                datum = translate(result)
        except:
            datum = 'மன்னிக்கவும் ! இப்போது தகவலைக் கண்டுபிடிக்க முடியவில்லை'
        finally:
            dispatcher.utter_message(text=datum)

        return []