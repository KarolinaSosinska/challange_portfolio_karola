from pages.base_page import BasePage


class AddMatchForm(BasePage):
    header_scouts_panel_xpath = "/header/div/h6"
    main_page_button_xpath = "//ul[1]/div[1]"
    players_button_xpath = "//ul[1]/div[2]"
    selected_player_xpath = "//ul[2]/div[1]"
    matches_xpath = "//ul[2]/div[2]"
    reports_xpath = "//ul[2]/div[3]"
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
    pass
