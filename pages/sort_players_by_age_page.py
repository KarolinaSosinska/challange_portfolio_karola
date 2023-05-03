from pages.base_page import BasePage


class SortPlayersByAgePage(BasePage):
    players_button_xpath = '//ul[1]/div[2]'
    age_button_xpath = '//th[3]/span/button'

    def click_on_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        self.click_on_the_element(self.players_button_xpath)

    def click_on_age_button(self):
        self.wait_for_element_to_be_clickable(self.age_button_xpath)
        self.click_on_the_element(self.age_button_xpath)
