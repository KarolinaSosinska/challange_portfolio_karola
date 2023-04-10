from pages.base_page import BasePage


class DashBoard(BasePage):
    main_page_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    language_selection_xpath = "//ul[2]/div[1]"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    dev_team_contact_button_xpath = "//a[1][@target='_blank']"
    add_player_button_xpath = "//*[@class='MuiButton-label' and text()='Add player']"
    header_scouts_panel_xpath = "/html/body/div/div/header/div/h6"
    scouts_panel_logo_xpath = "//*[@title='Logo Scouts Panel']"
    header_below_logo_xpath = "/html/body/div/div[1]/main/div[3]/div[1]/div/div[2]/h2"
    description_under_logo_xpath = "/html/body/div/div[1]/main/div[3]/div[1]/div/div[2]/p"
    players_count_xpath = "//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][1]"
    matches_count_xpath = "//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][2]"
    reports_count_xpath = "//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][3]"
    events_count_xpath = "//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'][4]"
    shortcuts_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
    activity_header_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    pass