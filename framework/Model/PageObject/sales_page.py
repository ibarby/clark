from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import SalesPageLocators


class SalesPage(BasePage):
    def should_be_category(self):
        assert self.get_element(*SalesPageLocators.CATEGORY_LINK), 'Category is absent'

    def click_category(self):
        self.click(*SalesPageLocators.CATEGORY_LINK)
