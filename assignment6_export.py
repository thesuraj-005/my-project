#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

api_key = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", data["message"])


# In[ ]:




