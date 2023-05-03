import time
from pages.base_page import BasePage


class LogOutPage(BasePage):
    sign_out_button_xpath = '//ul[2]/div[2]'
    header_xpath = '//div[1]/h5'
    logout_url = 'https://scouts-test.futbolkolektyw.pl/login'
    expected_title = 'Scouts panel - sign in'

    def click_on_the_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        self.click_on_the_element(self.sign_out_button_xpath)

    def title_of_page(self):
        self.visibility_of_element_located(self.header_xpath)
        assert self.get_page_title() == self.expected_title
