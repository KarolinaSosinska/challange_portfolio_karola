from pages.base_page import BasePage


class LogOutPage(BasePage):
    sign_out_button_xpath = '//ul[2]/div[2]'

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)
