import requests

def get_weather_data(lat, lon, hours):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,relative_humidity_2m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&forecast_days=2"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
