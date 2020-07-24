import time

from framework.Model.PageObject.base_page import BasePage
from framework.Data.locators import CategoryQuestionnairePageLocators


class CategoryQuestionnairePage(BasePage):
    def answering_questionnaire(self, info):
        self.check_title_questionnaire()
        self.proceed_to_questionnaire()
        self.choose_option()
        time.sleep(10)
        self.choose_option()
        time.sleep(10)
        self.choose_option()
        self.send_additional_info(info)
        self.press_request_offer_button()

    def proceed_to_questionnaire(self):
        self.click(*CategoryQuestionnairePageLocators.PROCEED_BUTTON)

    def check_title_questionnaire(self):
        assert self.get_element(*CategoryQuestionnairePageLocators.CATEGORY_TITLE)

    def choose_option(self):
        self.click(*CategoryQuestionnairePageLocators.QUESTIONNAIRE_OPTIONS)

    def send_additional_info(self, info):
        self.send_keys(*CategoryQuestionnairePageLocators.ADDITIONAL_INFO_INPUT, info)

    def press_request_offer_button(self):
        self.click(*CategoryQuestionnairePageLocators.REQUEST_OFFER)
