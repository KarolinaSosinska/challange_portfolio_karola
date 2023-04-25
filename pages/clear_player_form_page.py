from pages.base_page import BasePage


class ClearPlayerFormPage(BasePage):
    player_button_xpath = '//ul[1]/div[2]'
    search_input_xpath = '//div[2]/input'
    selected_player_xpath = '//tbody/tr'
    clear_button_xpath = '//button[2]'

    def click_on_player_button(self):
        self.click_on_the_element(self.player_button_xpath)

    def type_in_player_name(self, player_name):
        self.field_send_keys(self.search_input_xpath, player_name)

    def click_on_selected_player(self):
        self.click_on_the_element(self.selected_player_xpath)

    def click_on_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)
