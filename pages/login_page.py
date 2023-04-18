import time
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//div[1]/div/input"
    password_field_xpath = "//form/div/div[1]/div[2]/div/input"
    sign_in_button_xpath = "//span[1]"
    header_xpath = '//div[1]/h5'
    element_text = 'Scouts Panel'
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        time.sleep(2)
        self.get_page_title(self.login_url) == self.expected_title

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def header_of_page(self):
        self.assert_element_text(self, xpath='//div[1]/h5', expected_text='Scouts Panel')
