import requests
from datetime import datetime
from app_config import *

# Funcion para colocar el clima de manera mas descriptiva
def clima(clima_id):
    if clima_id >= 200 and clima_id <= 232:
        return "Tormenta 🌩️"
    elif clima_id >= 300 and clima_id <= 321:
        return "Llovizna 🌧️"
    elif clima_id >= 500 and clima_id <= 531:
        return "Lluvia 🌧️"
    elif clima_id >= 600 and clima_id <= 622:
        return "Nevado 🌨️"
    elif clima_id >= 700 and clima_id <= 781:
        return "No espcificado"
    elif clima_id == 800:
        return "Despejado ☀️"
    elif clima_id >= 801 and clima_id <= 804:
        emojis = ["","🌤️","⛅","🌥️", "☁️"]
        return f"Nuboso {emojis[clima_id - 800]}"


WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lon" : LONG_POSITION,
    "lat" : LAT_POSTITION,
    "units" : "metric",
    "cnt" : 8, # aproximado de datos del clima por dia
    "appid" : API_KEY
}

# Haciendo el llamado a la API del clima
response_weather = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
response_weather.raise_for_status()
data = response_weather.json()

# Informacion extraída:
pais = data["city"]["country"]
city_name = data["city"]["name"]
lista_pronosticos = data["list"]
hoy = datetime.now().strftime('%Y-%m-%d')

pronosticos_hoy = [pronostico for pronostico in lista_pronosticos if pronostico['dt_txt'].startswith(hoy)]
pronosticos_hoy.append(lista_pronosticos[len(pronosticos_hoy)])

# Creacion del mensaje a enviar
mensaje = "Pronóstico del clima:\n"
mensaje += f"{hoy} {city_name} {pais}\n"

for pronostico in pronosticos_hoy:
    tiempo = pronostico['dt_txt'].split(" ")
    hora_obj = datetime.strptime(tiempo[1], "%H:%M:%S")
    hora_12 = hora_obj.strftime("%I:%M %p")
    temperatura = pronostico["main"]["temp"]
    clima_id = int(pronostico["weather"][0]["id"])
    clima_ahora = clima(clima_id)
    mensaje += f"{hora_12} {temperatura}° {clima_ahora}\n"


TELEGRAM_API_ENDPOINT = f'https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage'
telegram_params = {
    'chat_id': TELEGRAM_USER, # empezar la conversación con el bot preciviamente en telegram
    'text': mensaje
}

# Haciendo el llamado a la API de telegram
response_telegram = requests.post(TELEGRAM_API_ENDPOINT, data=telegram_params)

# Verificacion de la llegada del mensaje
if response_telegram.status_code == 200:
    print("Mensaje enviado correctamente")
else:
    print("Error al enviar el mensaje", response_telegram.text)
