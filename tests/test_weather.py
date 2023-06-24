import unittest
from unittest.mock import patch
from weather import get_weather

class TestGetWeather(unittest.TestCase):
    @patch("builtins.print")
    def test_invalid_input(self, mock_print):
        # Test invalid input
        get_weather(123)
        mock_print.assert_called_with("City name must be a string")
        get_weather("New York City!")
        mock_print.assert_called_with("City name must contain only alphabetical characters")
        get_weather("LA")
        mock_print.assert_called_with("City name must be at least 3 characters long")
        get_weather("This is a very long city name that exceeds the maximum length allowed")
        mock_print.assert_called_with("City name must be no more than 50 characters long")
    
    @patch("builtins.print")
    @patch("requests.get")
    def test_api_error(self, mock_get, mock_print):
        # Test API error
        mock_get.return_value.status_code = 401
        get_weather("London")
        mock_print.assert_called_with("Invalid API key or unauthorized access. Please check your API key.")
        mock_get.return_value.status_code = 404
        get_weather("Paris")
        mock_print.assert_called_with("No weather data found for Paris")
        mock_get.side_effect = requests.exceptions.Timeout
        get_weather("Tokyo")
        mock_print.assert_called_with("Request timed out: ")
    
    @patch("builtins.print")
    @patch("requests.get")
    def test_valid_input(self, mock_get, mock_print):
        # Test valid input
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "list": [
                {
                    "dt_txt": "2022-01-01 12:00:00",
                    "main": {"temp": 10.0},
                    "weather": [{"description": "clear sky"}],
                },
                {
                    "dt_txt": "2022-01-02 12:00:00",
                    "main": {"temp": 15.0},
                    "weather": [{"description": "few clouds"}],
                },
                {
                    "dt_txt": "2022-01-03 12:00:00",
                    "main": {"temp": 20.0},
                    "weather": [{"description": "scattered clouds"}],
                },
                {
                    "dt_txt": "2022-01-04 12:00:00",
                    "main": {"temp": 25.0},
                    "weather": [{"description": "broken clouds"}],
                },
                {
                    "dt_txt": "2022-01-05 12:00:00",
                    "main": {"temp": 30.0},
                    "weather": [{"description": "overcast clouds"}],
                },
            ]
        }
        get_weather("London")
        mock_print.assert_called_with(
            "\nCurrent weather in London:\n"
            "┌─────────────┬────────────────┐\n"
            "│ Temperature │ 10.0°C         │\n"
            "├─────────────┼────────────────┤\n"
            "│ Description │ clear sky      │\n"
            "└─────────────┴────────────────┘\n"
            "\n5-day forecast:\n"
            "┌─────────────┬─────────────┬────────────────┐\n"
            "│ Date        │ Temperature │ Description    │\n"
            "├─────────────┼─────────────┼────────────────┤\n"
            "│ 2022-01-02 12:00:00 │ 15.0°C         │ few clouds     │\n"
            "│ 2022-01-03 12:00:00 │ 20.0°C         │ scattered clouds │\n"
            "│ 2022-01-04 12:00:00 │ 25.0°C         │ broken clouds  │\n"
            "│ 2022-01-05 12:00:00 │ 30.0°C         │ overcast clouds│\n"
            "└─────────────┴─────────────┴────────────────┘\n"
        )

if __name__ == "__main__":
    unittest.main()