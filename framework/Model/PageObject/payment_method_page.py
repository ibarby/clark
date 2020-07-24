import time
from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import PaymentMethodPageLocators


class PaymentMethodPage(BasePage):
    def go_to_review_contracts_term(self, iban):
        self.send_iban(iban)
        self.confirmation_terms_check()
        self.go_to_buy_tarif()
        time.sleep(10)

    def send_iban(self, iban):
        self.send_keys(*PaymentMethodPageLocators.INPUT_IBAN, iban)

    def confirmation_terms_check(self):
        checkbox = self.browser.find_element(*PaymentMethodPageLocators.CONFIRMATION_CHECK)
        self.browser.execute_script("arguments[0].click();", checkbox)

    def go_to_buy_tarif(self):
        self.click(*PaymentMethodPageLocators.GO_TO_BUY_TARIF)
