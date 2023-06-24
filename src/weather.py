
import argparse
import requests


"Api parameters"
API_KEY = "5e88f2488e93e15b31de9f3b8008dc1d"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    # Validate input
    if not isinstance(city, str):
        print("City name must be a string")
        return
    if not city.isalpha():
        print("City name must contain only alphabetical characters")
        return
    if len(city) < 3:
        print("City name must be at least 3 characters long")
        return
    if len(city) > 50:
        print("City name must be no more than 50 characters long")
        return
    
    # Make API request
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()  # raise an exception for 4xx or 5xx status codes
    except requests.exceptions.HTTPError as err:
        if response.status_code == 401:
            print("Invalid API key or unauthorized access. Please check your API key.")
        elif response.status_code == 404:
            print(f"No weather data found for {city}")
        else:
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
    
    # Parse response data
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
    
    # Print current weather
    print(f"\nCurrent weather in {city}:")
    print(f"┌─────────────┬────────────────┐")
    print(f"│ Temperature │ {current_temp:.1f}°C │")
    print(f"├─────────────┼────────────────┤")
    print(f"│ Description │ {current_desc:<14}│")
    print(f"└─────────────┴────────────────┘")
    
    # Print 5-day forecast
    print("\n5-day forecast:")
    print(f"┌─────────────┬─────────────┬────────────────┐")
    print(f"│ Date        │ Temperature │ Description    │")
    print(f"├─────────────┼─────────────┼────────────────┤")
    for forecast in data["list"][1:]:  # skip first item (current weather)
        try:
            date = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            desc = forecast["weather"][0]["description"]
        except (KeyError, IndexError):
            print(f"Error parsing forecast data for {city}")
            return
        print(f"│ {date} │ {temp:.1f}°C │ {desc:<14}│")
    print(f"└─────────────┴─────────────┴────────────────┘")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current weather and 5-day forecast for a city")
    parser.add_argument("city", type=str, help="City name")
    args = parser.parse_args()
    get_weather(args.city)