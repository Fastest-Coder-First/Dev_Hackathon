import unittest
from unittest.mock import patch, Mock
import weather


class TestWeather(unittest.TestCase):
    @patch("weather.make_api_request")
    def test_validate_input(self, mock_make_api_request):
        # Test valid input
        city = "New York"
        self.assertIsNone(weather.validate_input(city))

        # Test invalid input
        city = "123"
        with self.assertRaises(ValueError):
            weather.validate_input(city)

    @patch("weather.requests.get")
    def test_make_api_request(self, mock_requests_get):
        # Test successful API request
        city = "New York"
        mock_response = Mock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response
        response = weather.make_api_request(city)
        self.assertEqual(response, mock_response)

        # Test invalid API key
        mock_response.status_code = 401
        with self.assertRaises(ValueError):
            weather.make_api_request(city)

        # Test invalid city name
        mock_response.status_code = 404
        with self.assertRaises(ValueError):
            weather.make_api_request(city)

        # Test HTTP error
        mock_response.status_code = 500
        with self.assertRaises(ValueError):
            weather.make_api_request(city)

        # Test connection error
        mock_requests_get.side_effect = Exception("Connection error")
        with self.assertRaises(ValueError):
            weather.make_api_request(city)

        # Test timeout error
        mock_requests_get.side_effect = requests.exceptions.Timeout("Request timed out")
        with self.assertRaises(ValueError):
            weather.make_api_request(city)

    @patch("weather.make_api_request")
    def test_get_weather(self, mock_make_api_request):
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {
            "list": [
                {
                    "dt_txt": "2022-01-01 12:00:00",
                    "main": {"temp": 10},
                    "weather": [{"description": "Cloudy"}],
                },
                {
                    "dt_txt": "2022-01-02 12:00:00",
                    "main": {"temp": 15},
                    "weather": [{"description": "Sunny"}],
                },
                {
                    "dt_txt": "2022-01-03 12:00:00",
                    "main": {"temp": 20},
                    "weather": [{"description": "Rainy"}],
                },
                {
                    "dt_txt": "2022-01-04 12:00:00",
                    "main": {"temp": 25},
                    "weather": [{"description": "Cloudy"}],
                },
                {
                    "dt_txt": "2022-01-05 12:00:00",
                    "main": {"temp": 30},
                    "weather": [{"description": "Sunny"}],
                },
            ]
        }
        mock_make_api_request.return_value = mock_response

        # Call the function with a mock city name
        city = "mock_city"
        weather.get_weather(city)

        # Check that the function prints the expected output
        expected_output = (
            "\nCurrent weather in mock_city:\n"
            "Temperature: 10.0°C\n"
            "Description: Cloudy\n"
            "\n5-day forecast:\n"
            "┌─────────────┬─────────────┬────────────────┐\n"
            "│ Date        │ Temperature │ Description    │\n"
            "├─────────────┼─────────────┼────────────────┤\n"
            "│ 2022-01-02 12:00:00 │ 15.0°C │ Sunny          │\n"
            "│ 2022-01-03 12:00:00 │ 20.0°C │ Rainy          │\n"
            "│ 2022-01-04 12:00:00 │ 25.0°C │ Cloudy         │\n"
            "│ 2022-01-05 12:00:00 │ 30.0°C │ Sunny          │\n"
            "└─────────────┴─────────────┴────────────────┘\n"
        )
        self.assertEqual(expected_output, mock_response.print.call_args[0][0])


if __name__ == "__main__":
    unittest.main()