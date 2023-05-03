import os
import time
import unittest
from selenium import webdriver
from pages.dashboard import DashBoard
from pages.login_page import LoginPage
from pages.sort_players_by_age_page import SortPlayersByAgePage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSortPlayersByAgePage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sort_players_by_age(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.header_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = DashBoard(self.driver)
        dashboard_page.title_of_page()
        sort_page = SortPlayersByAgePage(self.driver)
        sort_page.click_on_players_button()
        sort_page.click_on_age_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
