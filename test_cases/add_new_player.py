import unittest
import os
from selenium import webdriver

from pages.add_player import AddPlayer
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_ad_player(self):
        TestLoginPage.test_log_in_to_the_system(self)
        selection = AddPlayer(self.driver)
        selection.click_on_the_add_player_button()
        selection.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
