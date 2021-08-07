# TheBot
RASA bot developed to be a voice assistant in english and Chat assistant in tamil.

It is a contextual assistant that can use Natural Language Processing and Understanding to assist personalized user queries  in their regional language.

Project Presentation :  https://drive.google.com/file/d/1ywyzdqIwIUX9anLSt0GpgoTxU0b9wJt4/view?usp=sharing

## System Architecture

![arch](https://user-images.githubusercontent.com/47826916/128602459-6230671f-a321-4f74-8a93-9bf19c2d041e.JPG)

## Use Case Diagram

![usecase](https://user-images.githubusercontent.com/47826916/128602485-0f5b19a4-64d8-4185-8399-6f1df62c5334.JPG)

## Class Diagram

![ClassDiagram](https://user-images.githubusercontent.com/47826916/128602688-46e5aa2f-4238-414a-bbb7-86c87f919cd3.JPG)

## Sequence Diagram

![sequence](https://user-images.githubusercontent.com/47826916/128602697-0f310310-029c-4ed1-b081-3ccd5cbadad4.JPG)

## Collaboration Diagram

![collaborate](https://user-images.githubusercontent.com/47826916/128602718-2553e9f3-069d-49f8-bd51-946f73146149.JPG)

## Activity Diagram

![activity](https://user-images.githubusercontent.com/47826916/128602747-a1b14191-e5c0-40bf-b595-9194410ca559.JPG)

## Component Diagram

![image](https://user-images.githubusercontent.com/47826916/128602779-0b6222aa-7ec0-4d8e-99fe-643f10f93158.png)

## Deployment Diagram

![deployment](https://user-images.githubusercontent.com/47826916/128602799-efa81f2e-081e-4f20-a542-9cbb9ec48206.JPG)


# Modules 

## Translation

![translatess](https://user-images.githubusercontent.com/47826916/128602935-7a4aae41-632b-4644-9520-874f29c4c24f.JPG)

## News

![newsss](https://user-images.githubusercontent.com/47826916/128602850-8c98b09c-bcaf-401c-b26e-1c7a581b2504.JPG)

## Weather

![weatherss](https://user-images.githubusercontent.com/47826916/128602886-37eb02e8-c2ee-491b-aef6-1ff04a16744e.JPG)

## Jokes

![jokess](https://user-images.githubusercontent.com/47826916/128602906-6f9486f2-bd40-4180-9d38-000d9a93ad9e.JPG)

## Quotes

![quotess](https://user-images.githubusercontent.com/47826916/128602915-fe081fb6-3608-4151-8757-2c49bd35056e.JPG)

# Steps to Run : 

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
  

## Project Directory :

 ### Data
 - nlu.yml (Holds example for intents Ex : Intent greet has hello, hi)
 - rules.yml (Provides the bot with rules like to respond welcome when user says thank you)
 - stores.yml ( Pathways for the bot to follow)


 ### Project Workflow:

 rasa run - for action server

 Ngrok port mapping to port 5005 (Check at once)
 Then use url for app

 ### For website 

 rasa run -m models --enable-api --cors "*" --debug 
  
