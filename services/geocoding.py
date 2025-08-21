import requests

def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    headers = {
        "User-Agent": "WeatherDashboardApp/1.0 (contact@example.com)"  # Replace with your app name and contact info
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            location = location_data[0]
            print(location)
            return float(location['lat']), float(location['lon'])
        else:
            return None, None
    else:
        return None, None
