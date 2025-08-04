import requests
from datetime import datetime
from app_config import *

WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

def clima(clima_id):
    if clima_id >= 200 and clima_id <= 232:
        return "Tormenta 🌩️"
    elif clima_id >= 300 and clima_id <= 321:
        return "Llovizna 🌧️"
    elif clima_id >= 500 and clima_id <= 531:
        return "Lluvia 🌧️"
    elif clima_id >= 600 and clima_id <= 622:
        return "Nieve 🌨️"
    elif clima_id >= 700 and clima_id <= 781:
        return "No espcificado"
    elif clima_id == 800:
        return "Despejado ☀️"
    elif clima_id >= 801 and clima_id <= 804:
        emojis = ["","🌤️","⛅","🌥️", "☁️"]
        return f"Nuboso {emojis[clima_id - 800]}"

weather_params = {
    "lon" : LONG_POSITION,
    "lat" : LAT_POSTITION,
    "units" : "metric",
    "cnt" : 8,
    "appid" : API_KEY
}

response = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()

# Informacion extraída:
pais = data["city"]["country"]
city_name = data["city"]["name"]
lista_pronosticos = data["list"]
hoy = datetime.now().strftime('%Y-%m-%d')

pronosticos_hoy = [pronostico for pronostico in lista_pronosticos if pronostico['dt_txt'].startswith(hoy)]
pronosticos_hoy.append(lista_pronosticos[len(pronosticos_hoy)])

print(f"Pais: {pais}\nCiudad: {city_name}")

for pronostico in pronosticos_hoy:
    tiempo = pronostico['dt_txt'].split(" ")
    hora_obj = datetime.strptime(tiempo[1], "%H:%M:%S")
    hora_12 = hora_obj.strftime("%I:%M %p")
    temperatura = pronostico["main"]["temp"]
    clima_id = int(pronostico["weather"][0]["id"])
    clima_ahora = clima(clima_id)
    print(f"{hora_12} - {temperatura}° - {clima_ahora}")

# print(pronosticos_hoy)


