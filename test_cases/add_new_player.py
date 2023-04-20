import unittest
import os
from selenium import webdriver

from pages.add_player import AddPlayer
from pages.dashboard import DashBoard
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddNewPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_ad_player(self):
        TestLoginPage.test_log_in_to_the_system(self)
        dashboard_page = DashBoard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        selection = AddPlayer(self.driver)
        selection.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()
