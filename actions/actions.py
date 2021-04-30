# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions"

from typing import Any, Text, Dict, List
import json
import requests

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
            quote = "Fake it till you make it"
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
            output = 'Current weather is ' + weather['weather'][0]['description'] + ' with temperature of '+celsius+'° Celsius'
        else:
            output = 'I m sorry ! I was not able to find the weather data'
        
        dispatcher.utter_message(text=output)

        return []