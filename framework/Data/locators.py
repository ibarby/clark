from selenium.webdriver.common.by import By
from framework.Data import personal_data_settings as st


class BasePageLocators(object):
    OFFERS_LINK = (By.LINK_TEXT, st.SALES_LINK_TITLE)


class SalesPageLocators(object):
    CATEGORY_LINK = (By.XPATH, f"//p[text()='{st.CATEGORY}']/..")


class CategoryQuestionnairePageLocators(object):
    PROCEED_BUTTON = (By.CSS_SELECTOR, "button._continue_n83it3")
    CATEGORY_TITLE = (By.XPATH, f"//div[@class='_start-screen_n83it3']/p[text()={st.CATEGORY}]")
    QUESTIONNAIRE_OPTIONS = (By.XPATH, "//ul[@id='radioButtonsSingleSelect']//li[1]")
    ADDITIONAL_INFO_INPUT = (By.CSS_SELECTOR, "input.cucumber-text-input")
    REQUEST_OFFER = (By.CSS_SELECTOR, 'button.btn-primary')


class CongratulationsPageLocators(object):
    CONGRATULATIONS_TEXT = (By.XPATH, "//h1[text()='Dein Angebot ist da!']")
    GO_TO_OFFERS_BUTTON = (By.XPATH, "//a[contains(@href, 'offers')][starts-with(@id, 'ember')]")


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    LOGIN_PSWD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class PersonalInfoPageLocators(object):
    SEX_RADIOBUTTON = (By.XPATH, "//input[@value='male']/parent::span")
    NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    SURNAME_INPUT = (By.XPATH, "//input[@name='lastName']")
    BIRTHDATE_INPUT = (By.XPATH, "//input[@name='birthdate']")
    STREET_INPUT = (By.XPATH, "//input[@name='street']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@name='zipcode']")
    HOUSE_NUMBER_INPUT = (By.XPATH, "//input[@name='houseNumber']")
    CITY_INPUT = (By.XPATH, "//input[@name='city']")
    PHONE_NUMBER_INPUT = (By.XPATH, "//input[@name='phoneNumber']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@form='customer-upgrade-profile-form']")


class PaymentMethodPageLocators(object):
    CONFIRMATION_CHECK = (By.CSS_SELECTOR, "label.cucumber-accept-terms-checkbox")
    INPUT_IBAN = (By.CSS_SELECTOR, "input.cucumber-offer-iban-input")
    GO_TO_BUY_TARIF = (By.CSS_SELECTOR, "button.btn-primary")


class ComparingInsuranceOffersPageLocators(object):
    CHOOSE_INSURANCE_OFFER = (By.CSS_SELECTOR, "button[data-test-button-appearance='primary']")


class ContractTermsReviewPageLocators(object):
    GO_TO_BUY_CONTRACT_BUTTON = (By.CSS_SELECTOR, 'button.btn-next-split')


class BuyingConfirmationPageLocators(object):
    GO_TO_PROFILE_BUTTON = (By.CSS_SELECTOR, 'button.btn-primary')


class ProfilePageLocators(object):
    CLOSE_MODAL = (By.CSS_SELECTOR, 'button.cucumber-close-modal')
    CONTRACT = (By.XPATH, f"//div[text()='{st.CATEGORY}']")
