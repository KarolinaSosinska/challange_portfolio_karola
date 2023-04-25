from pages.base_page import BasePage
import keyboard


class SortPlayersByAgePage(BasePage):
    players_button_xpath = '//ul[1]/div[2]'
    age_button_xpath = '//th[3]/span/button'

    def click_on_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_on_age_button(self):
        self.click_on_the_element(self.age_button_xpath)
