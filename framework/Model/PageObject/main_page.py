from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_sales_funnel(self):
        self.click(*BasePageLocators.OFFERS_LINK)
