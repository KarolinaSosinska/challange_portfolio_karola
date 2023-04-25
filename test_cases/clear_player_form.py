import os
import time
import unittest
import keyboard
from selenium import webdriver

from pages.clear_player_form_page import ClearPlayerFormPage
from pages.dashboard import DashBoard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestClearPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_clear_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.header_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = DashBoard(self.driver)
        dashboard_page.title_of_page()
        clear_player = ClearPlayerFormPage(self.driver)
        clear_player.click_on_player_button()
        clear_player.type_in_player_name('zaawodnik')
        keyboard.press_and_release('enter')
        clear_player.click_on_selected_player()
        clear_player.click_on_clear_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
