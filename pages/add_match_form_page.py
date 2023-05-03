from pages.base_page import BasePage


class AddMatchFormPage(BasePage):
    header_scouts_panel_xpath = "//header/div/h6"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    selected_player_xpath = "//ul[2]/div[1]"
    matches_button_xpath = "//ul[2]/div[2]"
    add_match_button_xpath = '//div[1]/main/a/button'
    reports_button_xpath = "//ul[2]/div[3]"
    language_selection_xpath = "//ul[3]/div[1]"
    sign_out_button_xpath = "//ul[3]/div[2]"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//button[2]"
    match_at_home_xpath = "//*[@class ='MuiFormControlLabel-root'][1]"
    match_out_home_xpath = "//*[@class ='MuiFormControlLabel-root'][2]"
    my_team_space_xpath = "//*[@name ='myTeam']"
    enemy_team_space_xpath = "//*[@name ='enemyTeam']"
    my_team_score_space_xpath = "//*[@name ='myTeamScore']"
    enemy_score_space_xpath = "//*[@name ='enemyTeamScore']"
    tshirt_color_space_xpath = "//*[@name ='tshirt']"
    league_space_xpath = "//*[@name ='league']"
    time_played_space_xpath = "//*[@name ='timePlayed']"
    number_space_xpath = "//*[@type='number' and @name= 'number']"
    web_match_space_xpath = "//div[11]/div/div/input"
    general_space_xpath = "//*[@name='general']"
    rating_space_xpath = "//*[@max='5']"
    date_input_xpath = '//div[5]/div/div/input'
    main_page_button_xpath = '//ul[1]/div[1]'
    add_match_ur = 'https://scouts-test.futbolkolektyw.pl/en/players/6026b48956c79737b3f3c624/matches/add'
    expected_title = 'Adding match player Brzęczyszcykiewić Zażółć Gęślą Jaźń'

    def click_on_matches_button(self):
        self.wait_for_element_to_be_clickable(self.matches_button_xpath)
        self.click_on_the_element(self.matches_button_xpath)

    def click_on_add_match_button(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)
        self.click_on_the_element(self.add_match_button_xpath)

    def title_of_page(self):
        self.visibility_of_element_located(self.header_scouts_panel_xpath)
        assert self.get_page_title() == self.expected_title

    def type_in_my_team(self, my_team_name):
        self.field_send_keys(self.my_team_space_xpath, my_team_name)

    def type_in_enemy_team(self, enemy_team_name):
        self.field_send_keys(self.enemy_team_space_xpath, enemy_team_name)

    def type_in_my_team_score(self, my_team_score):
        self.field_send_keys(self.my_team_score_space_xpath, my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_score_space_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_input_xpath, date)

    def click_on_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        self.click_on_the_element(self.main_page_button_xpath)
