import unittest
import helper_functions


class TestNoneHandler(unittest.TestCase):
    def test_str_is_not_none(self):
        self.assertEqual(helper_functions.none_handler("abc"), "abc")

    def test_str_is_none(self):
        self.assertIsNotNone((helper_functions.none_handler(None)))


if __name__ == '__main__':
    unittest.main()
