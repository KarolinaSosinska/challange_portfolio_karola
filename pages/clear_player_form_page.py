from pages.base_page import BasePage


class ClearPlayerFormPage(BasePage):
    player_button_xpath = '//ul[1]/div[2]'
    search_input_xpath = '//div[2]/input'
    selected_player_xpath = '//tbody/tr'
    clear_button_xpath = '//button[2]'
    main_page_button_xpath = '//ul[1]/div[1]'
    last_updated_player_ur = 'https://scouts-test.futbolkolektyw.pl/en/players/644788fd7ccfb69252f3136e/edit'
    expected_title = 'Edit player zaawodnik testowy'
    header_xpath = '//span[text()="Edit player zaawodnik testowy"]'

    def click_on_player_button(self):
        self.wait_for_element_to_be_clickable(self.player_button_xpath)
        self.click_on_the_element(self.player_button_xpath)

    def type_in_player_name(self, player_name):
        self.field_send_keys(self.search_input_xpath, player_name)

    def click_on_selected_player(self):
        self.wait_for_element_to_be_clickable(self.selected_player_xpath)
        self.click_on_the_element(self.selected_player_xpath)

    def click_on_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.click_on_the_element(self.clear_button_xpath)

    def click_on_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        self.click_on_the_element(self.main_page_button_xpath)

    def title_of_page(self):
        self.visibility_of_element_located(self.header_xpath)
        assert self.get_page_title() == self.expected_title
