import time
import unittest
import os

import pyautogui
import pyscreeze
from selenium import webdriver

from pages.add_player_page import AddPlayer
from pages.dashboard import DashBoard
from pages.login_page import LoginPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_ad_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = DashBoard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        selection = AddPlayer(self.driver)
        selection.type_in_email('abc@gmail.com')
        selection.type_in_name('Johnn')
        selection.type_in_surname('Smith')
        selection.type_in_phone('555675894')
        selection.type_in_weight('78')
        selection.type_in_height('177')
        selection.type_in_age('12051992')
        selection.click_on_leg_filed('right')
        selection.type_in_club('TC')
        selection.type_in_level('2')
        selection.type_in_main_position('Goalkeeper')
        selection.type_in_second_position('Center-back')
        selection.click_on_district_filed('Greater Poland')
        selection.type_in_achievements('Top 10 best goalkeeper in 2020')
        selection.click_on_submit_button()
        selection.click_on_main_page_button()
        login_page = LoginPage(self.driver)
        login_page.last_created_player()

    @classmethod
    def tearDown(self):
        self.driver.quit()
