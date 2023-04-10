from pages.base_page import BasePage
class LoginPage(BasePage):
    login_field_xpath ="/html/body/div/form/div/div[1]/div[1]/div/input"
    password_field_xpath ="/html/body/div/form/div/div[1]/div[2]/div/input"
    sign_in_button_xpath ="/html/body/div/form/div/div[2]/button/span[1]"

#
#     def type_in_email(self, email):
#         self.field_send_keys(self.login_field_xpath, email)
