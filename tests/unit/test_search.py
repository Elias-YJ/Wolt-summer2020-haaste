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
        self.assertEqual(json.loads(response.data), self.restaurant_data)

    def test_limited_query(self):
        response = self.app.get('/restaurants/search?q=eliel')
        response2 = self.app.get('restaurants/search?q=Momotoko')
        self.assertEqual(json.loads(response.data)['restaurants'][0]['blurhash']
                         , 'UFCsQ;M|slM~$kfloLsA02xsR.xWxuslW:W=')
        self.assertEqual(len(json.loads(response2.data)['restaurants']), 1)


if __name__ == '__main__':
    unittest.main()
