# ☁️ Weather-Advisor

**Weather-Advisor** es un script automatizado en Python que consulta el clima del día actual en una ubicación específica y envía un resumen detallado directamente a un usuario de Telegram.

---

## 🚀 Características

- Obtiene datos del clima desde la API de OpenWeather.
- Filtra automáticamente solo las predicciones del día actual.
- Traduce los estados del clima a descripciones con emojis 🌦️.
- Envía el pronóstico a través de un bot de Telegram 🤖.
- Manejo de horas en formato 12h (AM/PM).

---

## 📦 Requisitos

- Python 3.7+
- Cuenta de Telegram y bot creado con [@BotFather](https://t.me/BotFather)
- API key de [OpenWeather](https://openweathermap.org/)
- Librerías:
  - `requests`
  - `datetime`

### Instalación de dependencias

```bash
pip install requests
````

---

## ⚙️ Configuración

Agrega tus credenciales en un archivo `app_config.py` (que debe estar en `.gitignore`):

```python
API_KEY = "tu_api_key_de_openweather"
TELEGRAM_BOT_KEY = "tu_token_de_telegram"
TELEGRAM_USER = "tu_chat_id"
LAT_POSTITION = 51.507351  # Ejemplo: Londres
LONG_POSITION = -0.127758
```

---

## 📝 Uso

Ejecuta el script con:

```bash
python main.py
```

---

## 🖼️ Ejemplo de mensaje

```
Pronóstico del clima:
2025-08-05 Londres UK
06:00 AM 16.4° ☁️
09:00 AM 15.8° ⛅
12:00 PM 15.8° ⛅
03:00 PM 17.5° ⛅
```

```

---
