from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Bulawayo"):
    requests_url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={city}&units=imperial"
    response = requests.get(requests_url)
    
    if response.status_code != 200:
        return {"error": "Unable to fetch weather data"}

    data = response.json()

    return {
        "name": data.get("location", {}).get("name", "Unknown"),
        "country": data.get("location", {}).get("country", "Unknown"),
        "temperature": data.get("current", {}).get("temp_c", "N/A"),
        "description": data.get("current", {}).get("condition", {}).get("text", "N/A"),
        "icon": data.get("current", {}).get("condition", {}).get("icon", ""),
        "humidity": data.get("current", {}).get("humidity", "N/A"),
        "wind_kph": data.get("current", {}).get("wind_kph", "N/A")
    }

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)