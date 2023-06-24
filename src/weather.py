
import argparse
import requests


"Api parameters"
API_KEY = "5e88f2488e93e15b31de9f3b8008dc1d" # Replace with your own API key
API_URL = "https://api.openweathermap.org/data/2.5/forecast"



def validate_input(city):
    """
    Validates the input city name.

    Args:
        city (str): The name of the city to validate.

    Raises:
        ValueError: If the city name is invalid.
    """
    if not isinstance(city, str):
        raise ValueError("City name must be a string")
    if not city.isalpha():
        raise ValueError("City name must contain only alphabetical characters")
    if len(city) < 3:
        raise ValueError("City name must be at least 3 characters long")
    if len(city) > 50:
        raise ValueError("City name must be no more than 50 characters long")


def make_api_request(city):
    """
    Sends an API request to OpenWeatherMap and returns the response object.

    Args:
        city (str): The name of the city to get weather data for.

    Returns:
        requests.Response: The response object from the API request.

    Raises:
        ValueError: If an error occurs while making the API request.
    """
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(API_URL, params=params, timeout=5)
        response.raise_for_status()  # raise an exception for 4xx or 5xx status codes
    except requests.exceptions.HTTPError as err:
        if response.status_code == 401:
            raise ValueError("Invalid API key or unauthorized access. Please check your API key.")
        elif response.status_code == 404:
            raise ValueError(f"No weather data found for {city}")
        else:
            raise ValueError(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        raise ValueError(f"An error occurred: {err}")
    except requests.exceptions.ConnectionError as err:
        raise ValueError(f"Connection error occurred: {err}")
    except requests.exceptions.Timeout as err:
        raise ValueError(f"Request timed out: {err}")
    return response


def get_weather(city):
    """
    Gets the current weather and 5-day forecast for a city.

    Args:
        city (str): The name of the city to get weather data for.
    """
    try:
        validate_input(city)
        response = make_api_request(city)
        data = response.json()
        current_temp = data["list"][0]["main"]["temp"]
        current_desc = data["list"][0]["weather"][0]["description"]
        forecast_data = data["list"][1:]
        print(f"\nCurrent weather in {city}:")
        print(f"Temperature: {current_temp:.1f}°C")
        print(f"Description: {current_desc}")
        print("\n5-day forecast:")
        print(f"┌─────────────┬─────────────┬────────────────┐")
        print(f"│ Date        │ Temperature │ Description    │")
        print(f"├─────────────┼─────────────┼────────────────┤")
        for forecast in forecast_data:
            date = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            desc = forecast["weather"][0]["description"]
            print(f"│ {date} │ {temp:.1f}°C │ {desc:<14}│")
        print(f"└─────────────┴─────────────┴────────────────┘")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current weather and 5-day forecast for a city")
    parser.add_argument("city", type=str, help="City name")
    args = parser.parse_args()
    get_weather(args.city)