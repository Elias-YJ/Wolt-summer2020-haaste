import unittest
import json


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        with open('restaurants.json') as json_file:
            self.restaurant_data = json.loads(json_file.read())

    def test_name_data_type(self):
        self.assertIsInstance(self.restaurant_data["restaurants"][1]["name"], type("str"))


if __name__ == '__main__':
    unittest.main()
