# Problem Statement
Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

# Language
Python

# How Github copilot Helped me Implemented Solutions
 1. Connect With weather Api (Generated python cli app that accpet parameters and connect to Open weather Api)
 2. Error handling mechanisms Implementaation(ex :401, timeout etc)
 3. code generation for Data Validations (city Variable type check, length check )
 4. Generated Unit testcases for written code block (first generated test cases for ame file , later enhanced to separate file)
 5. Enhanced modularity by splitting single large method to 3 small methods
 6. Generated code comments for written code
 7. Generated Readme documentation file for written application (License section and other aspects we got from copilot docs)
 8. Suggested best practces like use of config files , separation of unit test cases to new file etc
 9. suggested solutuon for missed library installations (not installed requestes library , git hub suggested fix)
 10. Formatted cli output to tabular (Json list is modified as tabular one)
 11. suggested security vulnerbilties anf fixes for errors ( Ex api key should not be hardcoded etc keep it in os environment etc)
 12.  # Suggested fix to prevent injection attacks added regex to validate input

# How Github copilot Helped scenarios but not implemented due to limited development knowedge

1. Git hub suggested enable logging instead of print
2. Suggested redis based cache mechanism whenasked for performance enhancement


 # How to run

 1. Download the code file and Open terminal at Dev_Hackathon/src folder
 2. Run Python weather.py <cityname as parameter>
 3. Review Changes at terminal

# Usage
1. To use the script, run the following command: 
python weather.py <city>
2. Replace <city> with the name of the city you want to retrieve weather data for.
For example, to retrieve weather data for New York, run:
python weather.py "New York"

**Screen Shot**
1.Success Scenario

![image](https://github.com/Fastest-Coder-First/Dev_Hackathon/assets/36884631/46555ad7-2893-405c-a652-fcd9d341c993)

2.Giving invalid city input

![image](https://github.com/Fastest-Coder-First/Dev_Hackathon/assets/36884631/e88cf343-52ac-47ab-8f74-9441b75a972f)

# Architecture 

![image](https://github.com/Fastest-Coder-First/Dev_Hackathon/assets/36884631/e4da91a0-e223-4451-b8ed-14d009e97d18)

# Github Generated Documentation
# Weather App
This is a Python script that retrieves weather data from the OpenWeatherMap API and displays the current weather and a 5-day forecast for a given city.

# Input Validation
The script validates the input city name to ensure that it is a valid string. If the input is not a valid string, the script will raise a ValueError with an appropriate error message.

# Dependencies
The weather.py module has the following dependencies:

requests: This module is used to make HTTP requests to the OpenWeatherMap API to retrieve weather data.
You can install these dependencies using pip, the Python package manager. To install requests, run the following command:

pip install requests
This will install the latest version of the requests module.

Note that the weather.py module also requires an API key from OpenWeatherMap to retrieve weather data.

# Error Handling
The script handles various error scenarios that may occur when making requests to the OpenWeatherMap API. If an error occurs, the script will raise a ValueError with an appropriate error message.

# The following error scenarios are handled:

Invalid API key: If the API key is invalid, the API will return a 401 Unauthorized status code. The script will raise a ValueError with an error message indicating that the API key is invalid.
Invalid city name: If the city name is invalid, the API will return a 404 Not Found status code. The script will raise a ValueError with an error message indicating that the city name is invalid.
HTTP error: If the API returns an HTTP error status code (other than 401 or 404), the script will raise a ValueError with an error message indicating that an HTTP error occurred.
Connection error: If the script is unable to connect to the API due to a network error, the script will raise a ValueError with an error message indicating that a connection error occurred.
Timeout error: If the API request times out, the script will raise a ValueError with an error message indicating that the request timed out.

# API Key
To use the OpenWeatherMap API, you will need to obtain an API key from the OpenWeatherMap website. Once you have obtained an API key, you can either store it in a separate configuration file or as an environment variable.

To store the API key in a configuration file, create a file called config.ini in the same directory as the weather.py file, with the following contents:
[openweathermap]
api_key = YOUR_API_KEY_HERE
Replace YOUR_API_KEY_HERE with your actual API key.

To store the API key as an environment variable, set the OPENWEATHERMAP_API_KEY environment variable to your API key.

# Testing
To run the unit tests for the script, run the following command:

This will run a series of tests to ensure that the script functions correctly and handles errors appropriately.

# License
This script is licensed under the MIT License. See the LICENSE file for more information.
