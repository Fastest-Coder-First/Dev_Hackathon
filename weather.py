
import argparse
import requests

"Api parameters"
API_KEY = "5e88f2488e93e15b31de9f3b8008dc1d"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        current_temp = data["list"][0]["main"]["temp"]
        current_desc = data["list"][0]["weather"][0]["description"]
        print(f"Current weather in {city}: {current_temp}°C, {current_desc}")
        print("5-day forecast:")
        for forecast in data["list"][1:]:  # skip first item (current weather)
            date = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            desc = forecast["weather"][0]["description"]
            print(f"{date}: {temp}°C, {desc}")
    else:
        print(f"Error getting weather data: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current weather and 5-day forecast for a city")
    parser.add_argument("city", type=str, help="City name")
    args = parser.parse_args()
    get_weather(args.city)