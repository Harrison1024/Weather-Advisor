import requests
from app_config import *

WEATHER_API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lon" : LONG_POSITION,
    "lat" : LAT_POSTITION,
    "units" : "metric",
    "appid" : API_KEY
}

response = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
data = response.json()

print(data)

