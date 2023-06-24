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

 

Github Copilot code explanation


The code is a Python script that retrieves weather data from the OpenWeatherMap API.
It imports the argparse and requests modules.
It sets the API key and URL for the OpenWeatherMap API.
It defines a function get_weather that takes a city name as an argument.
The get_weather function sends a GET request to the OpenWeatherMap API with the city name and API key as parameters.
The function retrieves the current temperature and weather description for the city from the API response.
The function then prints the current weather and a 5-day forecast for the city.
