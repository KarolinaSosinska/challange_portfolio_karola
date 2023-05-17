import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//div[1]/div/input"
    password_field_xpath = "//form/div/div[1]/div[2]/div/input"
    sign_in_button_xpath = "//span[1]"
    header_xpath = '//div[1]/h5'
    header_text = 'Scouts Panel'
    login_url = 'https://scouts.futbolkolektyw.pl/en/'
    expected_title = 'Scouts panel - sign in'
    last_created_player_xpath = '//div[3]/div/div/a[1]/button'
    expected_player = 'JOHNN SMITH'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        self.visibility_of_element_located(self.header_xpath)
        assert self.get_page_title() == self.expected_title

    def header_of_page(self):
        self.visibility_of_element_located(self.header_xpath)
        self.assert_element_text(self.driver, self.header_xpath, self.header_text)

    def last_created_player(self):
        self.visibility_of_element_located(self.last_created_player_xpath)
        self.assert_element_text(self.driver, self.last_created_player_xpath, self.expected_player)
