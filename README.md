# TheBot
RASA bot developed to be a voice assistant 


Steps to Run : 

Create virtual environment

pip install rasa

To train rasa:
  - rasa train
  
To test rasa:
  - rasa test
  
To interact with bot in command line:
  - rasa shell
  
To run action server:
  - rasa run
  

Project Directory :

Data
 - nlu.yml (Holds example for intents Ex : Intent greet has hello, hi)
 - rules.yml (Provides the bot with rules like to respond welcome when user says thank you)
 - stores.yml ( Pathways for the bot to follow)
  
