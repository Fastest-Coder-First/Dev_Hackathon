# Problem Statement
Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Language
Python


 # How to run

 1. Download the code file and Open terminal at Dev_Hackathon/src folder
 2. Run Python weather.py <cityname as parameter>
 3. Review Changes at terminal

**Screen Shot**
![image](https://github.com/Fastest-Coder-First/Dev_Hackathon/assets/36884631/46555ad7-2893-405c-a652-fcd9d341c993)

 

#Github Generate dDocumentation

#Weather App
This is a Python script that retrieves weather data from the OpenWeatherMap API and displays the current weather and a 5-day forecast for a given city.

#Usage
To use the script, run the following command:
python weather.py <city>
Replace <city> with the name of the city you want to retrieve weather data for.
For example, to retrieve weather data for New York, run:
python weather.py "New York"

#Input Validation
The script validates the input city name to ensure that it is a valid string. If the input is not a valid string, the script will raise a ValueError with an appropriate error message.

#Error Handling
The script handles various error scenarios that may occur when making requests to the OpenWeatherMap API. If an error occurs, the script will raise a ValueError with an appropriate error message.

#The following error scenarios are handled:

Invalid API key: If the API key is invalid, the API will return a 401 Unauthorized status code. The script will raise a ValueError with an error message indicating that the API key is invalid.
Invalid city name: If the city name is invalid, the API will return a 404 Not Found status code. The script will raise a ValueError with an error message indicating that the city name is invalid.
HTTP error: If the API returns an HTTP error status code (other than 401 or 404), the script will raise a ValueError with an error message indicating that an HTTP error occurred.
Connection error: If the script is unable to connect to the API due to a network error, the script will raise a ValueError with an error message indicating that a connection error occurred.
Timeout error: If the API request times out, the script will raise a ValueError with an error message indicating that the request timed out.

#API Key
To use the OpenWeatherMap API, you will need to obtain an API key from the OpenWeatherMap website. Once you have obtained an API key, you can either store it in a separate configuration file or as an environment variable.

To store the API key in a configuration file, create a file called config.ini in the same directory as the weather.py file, with the following contents:
[openweathermap]
api_key = YOUR_API_KEY_HERE
Replace YOUR_API_KEY_HERE with your actual API key.

To store the API key as an environment variable, set the OPENWEATHERMAP_API_KEY environment variable to your API key.

#Testing
To run the unit tests for the script, run the following command:

This will run a series of tests to ensure that the script functions correctly and handles errors appropriately.

#License
This script is licensed under the MIT License. See the LICENSE file for more information.
