from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import BuyingConfirmationPageLocators


class BuyingConfirmationPage(BasePage):
    def go_to_profile(self):
        self.click(*BuyingConfirmationPageLocators.GO_TO_PROFILE_BUTTON)
