import unittest
from fetch_weather import fetch_weather_by_coords


class TestWeatherFetcher(unittest.TestCase):
    def test_valid_api_key(self):
        result = fetch_weather_by_coords(35,139)
        print("Test Result",result)
        self.assertIn("temperature", result)

    def test_invalid_api_key(self):
        result = fetch_weather_by_coords(35, 139, "invalid_key_123")
        print("Test Result (invalid):", result)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
