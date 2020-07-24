import time
from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import ContractTermsReviewPageLocators


class ContractTermsReviewPage(BasePage):
    def go_to_buy_contract(self):
        self.click(*ContractTermsReviewPageLocators.GO_TO_BUY_CONTRACT_BUTTON)
        time.sleep(10)
