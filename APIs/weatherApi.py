import json,requests

api_key = "df6d7566e1ff99c3e1f91ec11f22d5e9"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = 'chennai'
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
weather = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if weather["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    datum = weather["main"]
    celsius = str(int(datum['temp'])-273) + ""
    print('Current weather : ' + weather['weather'][0]['description'] + ' with temperature = '+celsius+'° Celsius')
     
    print(datum)
    # # store the value corresponding 
    # # to the "temp" key of y 
    # current_temperature = datum["temp"] 
  
    # # store the value corresponding 
    # # to the "pressure" key of y 
    # current_pressure = datum["pressure"] 
  
    
    # # store the value of "weather" 
    # # key in variable z 
    # current_weather = datum["weather"] 
    
    # # store the value corresponding  
    # # to the "description" key at  
    # # the 0th index of z 
    # weather_description = datum[0]["description"] 

    # print('Temperature : '+current_temperature + '\n Pressure : '+current_pressure)
    # print('Weather is '+current_weather)
    # print('\n'+weather_description)    
   
    