import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch("weather.requests.get")
    def test_get_weather(self, mock_get):
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

        # Test valid city
        expected_output = "Current weather in London: 20°C, sunny\n5-day forecast:\n2022-01-01 12:00:00: 18°C, partly cloudy\n2022-01-02 12:00:00: 16°C, cloudy\n"
        self.assertEqual(get_weather("London"), expected_output)

        # Test invalid city
        expected_output = "No weather data found for InvalidCity\n"
        self.assertEqual(get_weather("InvalidCity"), expected_output)

if __name__ == "__main__":
    unittest.main()