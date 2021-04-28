# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

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
