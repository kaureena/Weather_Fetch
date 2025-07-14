import requests

def fetch_weather_by_coords(lat: float, lon: float, api_key: str) -> dict:
    url = f'https://api.agromonitoring.com/agro/1.0/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "coordinates": f"{lat}, {lon}",
            "temperature": data.get('main', {}).get('temp', 'N/A'),
            "weather": data.get('weather', [{}])[0].get('description', 'N/A')
        }
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}


# Optional manual run (for testing)
if __name__ == "__main__":
    API_KEY = '823109c6390b5e06e2169d638805ac6e'
    lat = 35
    lon = 139
    result = fetch_weather_by_coords(lat, lon, API_KEY)
    print(result)
