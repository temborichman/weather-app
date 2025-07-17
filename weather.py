from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Bulawayo"):
    print(os.getenv('WEATHER_API_KEY'))
    requests_url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={city}&units=imperial"
    response = requests.get(requests_url)
    print(requests_url)
    
    data = response.json()

    return data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)