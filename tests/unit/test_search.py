import unittest
import json
from api import app


class TestBasic(unittest.TestCase):
    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True

        # Load test data
        with open('restaurants.json') as json_file:
            self.restaurant_data = json.loads(json_file.read())

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_restaurants_page(self):
        response = self.app.get('/restaurants')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
