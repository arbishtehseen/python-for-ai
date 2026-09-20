# import requests 
# request library in python, we use it to interact with APis.

# We need coordinates to get weather data
# latitude = 48.85
# longitude = 2.35

# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m "

# Make the request
# response = requests.get(url)
# data = response.json()

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data["current"]["temperature_2m"]

# get temp for diff cities.
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
print(f"Paris : {paris_temp}C")
print(f"London : {london_temp}C")
print(f"Tokyo : {tokyo_temp}C")