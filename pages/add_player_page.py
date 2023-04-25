import time
import keyboard
from pages.base_page import BasePage


class AddPlayer(BasePage):
    expected_title = 'Add player'
    add_player_ur = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    leg_filed_xpath = '//div[8]/div/div/div'
    email_filed_xpath = '//div[1]/div/div/input'
    name_filed_xpath = '//div[2]/div/div/input'
    surname_filed_xpath = '//div[3]/div/div/input'
    phone_filed_xpath = '//div[4]/div/div/input'
    weight_filed_xpath = '//div[5]/div/div/input'
    height_filed_xpath = '//div[6]/div/div/input'
    age_filed_xpath = '//div[7]/div/div/input'
    club_filed_xpath = '//div[9]/div/div/input'
    level_filed_xpath = '//div[10]/div/div/input'
    main_position_filed_xpath = '//div[11]/div/div/input'
    second_position_filed_xpath = '//div[12]/div/div/input'
    district_filed_xpath = '//div[13]/div/div/div'
    achievements_filed_xpath = '//div[14]/div/div/input'
    submit_button_xpath = '//div[3]/button[1]'

    def title_of_page(self):
        time.sleep(2)
        assert self.get_page_title() == self.expected_title

    def click_on_leg_filed(self, leg):
        self.click_on_the_element(self.leg_filed_xpath)
        if leg == "left":
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        else:
            keyboard.press_and_release('Up')
            keyboard.press_and_release('enter')

    def type_in_email(self, email):
        self.field_send_keys(self.email_filed_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_filed_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_filed_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_filed_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_filed_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_filed_xpath, height)

    def type_in_age(self, date_of_birth):
        self.field_send_keys(self.age_filed_xpath, date_of_birth)

    def type_in_club(self, club):
        self.field_send_keys(self.club_filed_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_filed_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_filed_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_filed_xpath, second_position)

    def click_on_district_filed(self, district):
        self.click_on_the_element(self.district_filed_xpath)
        if district == "Lower Silesia":
            keyboard.press_and_release('Up')
            keyboard.press_and_release('enter')
        elif district == 'Kuyavia-Pomerania':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Lublin':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Lubusz':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Łódź':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Lesser Poland':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Masovia':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Opole':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Subcarpathia':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Podlaskie':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Pomerania':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Silesia':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Holy Cross Province':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Warimia-Masuria':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        elif district == 'Greater Poland':
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')
        else:
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('Down')
            keyboard.press_and_release('enter')

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_filed_xpath, achievements)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
