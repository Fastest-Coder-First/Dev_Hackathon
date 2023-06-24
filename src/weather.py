
import argparse
import requests


"Api parameters"
API_KEY = "5e88f2488e93e15b31de9f3b8008dc1d"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()  # raise an exception for 4xx or 5xx status codes
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return
    except requests.exceptions.ConnectionError as err:
        print(f"Connection error occurred: {err}")
        return
    except requests.exceptions.Timeout as err:
        print(f"Request timed out: {err}")
        return
    try:
        data = response.json()
    except ValueError as err:
        print(f"Error parsing response: {err}")
        return
    try:
        current_temp = data["list"][0]["main"]["temp"]
        current_desc = data["list"][0]["weather"][0]["description"]
    except (KeyError, IndexError):
        print(f"No weather data found for {city}")
        return
    print(f"Current weather in {city}: {current_temp}°C, {current_desc}")
    print("5-day forecast:")
    for forecast in data["list"][1:]:  # skip first item (current weather)
        date = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        desc = forecast["weather"][0]["description"]
        print(f"{date}: {temp}°C, {desc}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current weather and 5-day forecast for a city")
    parser.add_argument("city", type=str, help="City name")
    args = parser.parse_args()
    get_weather(args.city)