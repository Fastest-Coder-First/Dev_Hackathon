import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch('weather.requests.Session.get')
    def test_valid_city(self, mock_get):
        mock_data = {
            "city": {"name": "London"},
            "list": [
                {"dt_txt": "2022-01-01 12:00:00", "main": {"temp": 10}, "weather": [{"description": "sunny"}]},
                {"dt_txt": "2022-01-02 12:00:00", "main": {"temp": 15}, "weather": [{"description": "cloudy"}]},
                {"dt_txt": "2022-01-03 12:00:00", "main": {"temp": 20}, "weather": [{"description": "rainy"}]}
            ]
        }
        mock_response = type('MockResponse', (object,), {'status_code': 200, 'json': lambda self: mock_data})
        mock_get.return_value = mock_response

        city = "London"
        city_name, forecast = get_weather(city)
        self.assertEqual(city_name, "London")
        self.assertGreater(len(forecast), 0)

    @patch('weather.requests.Session.get')
    def test_invalid_city(self, mock_get):
        mock_response = type('MockResponse', (object,), {'status_code': 404})
        mock_get.return_value = mock_response

        city = "InvalidCityName"
        with self.assertRaises(ValueError):
            get_weather(city)

    def test_non_string_city(self):
        city = 123
        with self.assertRaises(ValueError):
            get_weather(city)

    def test_short_city_name(self):
        city = "LA"
        with self.assertRaises(ValueError):
            get_weather(city)

if __name__ == '__main__':
    unittest.main()