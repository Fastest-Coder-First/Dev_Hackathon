import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_weather_valid_city(self, mock_get):
        mock_data = {
            "list": [
                {
                    "main": {"temp": 20},
                    "weather": [{"description": "sunny"}]
                },
                {
                    "dt_txt": "2022-01-01 12:00:00",
                    "main": {"temp": 18},
                    "weather": [{"description": "partly cloudy"}]
                },
                {
                    "dt_txt": "2022-01-02 12:00:00",
                    "main": {"temp": 16},
                    "weather": [{"description": "cloudy"}]
                }
            ]
        }
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = mock_data
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        expected_output = "Current weather in London: 20°C, sunny\n5-day forecast:\n2022-01-01 12:00:00: 18°C, partly cloudy\n2022-01-02 12:00:00: 16°C, cloudy\n"
        self.assertEqual(get_weather("London"), expected_output)

    @patch("weather.requests.get")
    def test_get_weather_invalid_city(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        expected_output = "No weather data found for InvalidCity\n"
        self.assertEqual(get_weather("InvalidCity"), expected_output)

    @patch("weather.requests.get")
    def test_get_weather_request_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Test error")

        expected_output = "An error occurred: Test error\n"
        self.assertEqual(get_weather("London"), expected_output)

    @patch("weather.requests.get")
    def test_get_weather_http_error(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        expected_output = "HTTP error occurred: 500 Server Error: Internal Server Error for url: https://api.openweathermap.org/data/2.5/forecast\n"
        self.assertEqual(get_weather("London"), expected_output)

    @patch("weather.requests.get")
    def test_get_weather_parse_error(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.side_effect = ValueError("Test error")
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        expected_output = "Error parsing response: Test error\n"
        self.assertEqual(get_weather("London"), expected_output)

if __name__ == "__main__":
    unittest.main()