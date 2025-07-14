import unittest
from fetch_weather import fetch_weather_by_coords

class TestWeatherFetcher(unittest.TestCase):
    def test_invalid_api_key(self):
        result = fetch_weather_by_coords(35, 139, "fake_api_key")
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
