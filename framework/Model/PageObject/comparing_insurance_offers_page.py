from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import ComparingInsuranceOffersPageLocators


class ComparingInsuranceOffersPage(BasePage):
    def go_to_register_new_user(self):
        self.click(*ComparingInsuranceOffersPageLocators.CHOOSE_INSURANCE_OFFER)
