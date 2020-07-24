from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import CongratulationsPageLocators


class CongratulationsPage(BasePage):
    def should_be_congrats_text(self):
        assert self.is_element_present(*CongratulationsPageLocators.CONGRATULATIONS_TEXT), \
            'Congratulations text is absent'

    def go_to_comparing_insurance_offers_page(self):
        self.click(*CongratulationsPageLocators.GO_TO_OFFERS_BUTTON)