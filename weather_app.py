import requests
API_key="a1c4ae7e3b86d4559ff1bd2e32a53215"
state_code=country_code=lat=limit=lon=None
city_name=input("Search.. ")

API_call_geo=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}"
response_geo=requests.get(API_call_geo)
response_geo.raise_for_status()
data_geo=response_geo.json()
if len(data_geo) >0:
    lat=data_geo[0]['lat']
    lon=data_geo[0]['lon']
    
    API_call_open_weather=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    response_open_weather=requests.get(API_call_open_weather)
    response_open_weather.raise_for_status()
    data_open_weather=response_open_weather.json()
    print(f"The weather desciption is: {data_open_weather['weather'][0]['description']} and the temperature is {data_open_weather['main']['temp']} celsius :) ")
  
else:
    print("Not Found. Try Again!")
