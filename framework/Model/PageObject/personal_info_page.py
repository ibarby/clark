from framework.Helpers.utilities import GeneratorUtilities
from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import PersonalInfoPageLocators


class PersonalInfoPage(BasePage):
    def provide_additional_info(self, birthdate, city, zipcode, phonenumber):
        self.index = GeneratorUtilities.get_random_digit_number(6)
        self.send_name()
        self.send_surname()
        self.click(*PersonalInfoPageLocators.SEX_RADIOBUTTON)
        self.send_birthdate(birthdate)
        self.send_street()
        self.send_city(city)
        self.send_housenumber()
        self.send_zipcode(zipcode)
        self.send_phone_number(phonenumber)
        self.click(*PersonalInfoPageLocators.SUBMIT_BUTTON)

    def send_name(self):
        name = f'Name{self.index}'
        self.send_keys(*PersonalInfoPageLocators.NAME_INPUT, name)

    def send_surname(self):
        surname = f'Surname{self.index}'
        self.send_keys(*PersonalInfoPageLocators.SURNAME_INPUT, surname)

    def send_birthdate(self, birthdate):
        self.send_keys(*PersonalInfoPageLocators.BIRTHDATE_INPUT, birthdate)

    def send_street(self):
        street = f'Street{self.index}'
        self.send_keys(*PersonalInfoPageLocators.STREET_INPUT, street)

    def send_city(self, city):
        self.send_keys(*PersonalInfoPageLocators.CITY_INPUT, city)

    def send_housenumber(self):
        housenumber = GeneratorUtilities.get_random_digit_number(3)
        self.send_keys(*PersonalInfoPageLocators.HOUSE_NUMBER_INPUT, housenumber)

    def send_zipcode(self, zipcode):
        self.send_keys(*PersonalInfoPageLocators.ZIPCODE_INPUT, zipcode)

    def send_phone_number(self, phonenumber):
        self.send_keys(*PersonalInfoPageLocators.PHONE_NUMBER_INPUT, phonenumber)