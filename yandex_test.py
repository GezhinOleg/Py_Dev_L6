import unittest
from yandex_api import createfolder, get_folder_info

FOLDERNAME = 'test'


class TestYandexAPI(unittest.TestCase):
    def test_createfolder(self):
        result = createfolder(FOLDERNAME)
        self.assertTrue(result == 201, f'Сервер ответил: {result}')

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(FOLDERNAME) == 'dir')
