import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath = '//div[2]/div/div/a/button/span[1]'
    expected_title = 'Add player'
    add_player_ur = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(2)
        assert self.get_page_title(self.add_player_ur) == self.expected_title
