import unittest
import re
from selenuim_yandex import selenium_login, correct_login


class TestYandexAuth(unittest.TestCase):
    def test_login(self):
        self.assertTrue(correct_login())

    def test_auth(self):
        result = selenium_login()
        self.assertTrue(re.match(r".*welcome.*", result.get('login')))
        self.assertTrue(re.match(r".*(challenge|profile).*", result.get('password')))
