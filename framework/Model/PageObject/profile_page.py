from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def should_be_contract(self):
        self.close_modal()
        assert self.is_element_present(*ProfilePageLocators.CONTRACT), 'New contract not found'

    def close_modal(self):
        self.click(*ProfilePageLocators.CLOSE_MODAL)