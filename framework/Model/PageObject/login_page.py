from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import LoginPageLocators
from framework.Helpers.utilities import GeneratorUtilities


class LoginPage(BasePage):
    def register_new_user(self, password):
        self.send_login()
        self.send_password(password)
        self.click(*LoginPageLocators.LOGIN_BTN)

    def send_login(self):
        email = GeneratorUtilities.get_random_email(4)
        self.send_keys(*LoginPageLocators.LOGIN_EMAIL, email)

    def send_password(self, password):
        self.send_keys(*LoginPageLocators.LOGIN_PSWD, password)
