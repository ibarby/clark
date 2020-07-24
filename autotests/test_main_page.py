'''
I wrote e2e test with a small number of asserts, assuming that it's not a good idea to write UI sanity autotests.
If it is required on the project, I should be familiar with priorities and other details to write them.
Also, I have more experience with API-tests. I wrote some e2e tests for our application,
but we don't have any problems with the page loading. So I use here time.sleep(),
cause I've never faced this behavior before. I know that it's not a right thing to do.
On the real project, I'd discuss it with my colleagues to resolve it.
'''


from framework.Model.PageObject.category_questionnaire_page import CategoryQuestionnairePage
from framework.Model.PageObject.congratulations_page import CongratulationsPage
from framework.Model.PageObject.contract_terms_review_page import ContractTermsReviewPage
from framework.Model.PageObject.login_page import LoginPage
from framework.Model.PageObject.buying_confirmation_page import BuyingConfirmationPage
from framework.Model.PageObject.comparing_insurance_offers_page import ComparingInsuranceOffersPage
from framework.Model.PageObject.payment_method_page import PaymentMethodPage
from framework.Model.PageObject.personal_info_page import PersonalInfoPage
from framework.Model.PageObject.profile_page import ProfilePage
from framework.Model.PageObject.sales_page import SalesPage
from framework.Data.links import Urls
from framework.Model.PageObject.main_page import MainPage
import framework.Data.personal_data_settings as st


def test_bying_insurance_positive(browser):
    info = 'some additional info'
    landing_page = MainPage(browser, Urls.MAIN_PAGE_URL)
    landing_page.open()
    landing_page.go_to_sales_funnel()

    sales_page = SalesPage(browser, browser.current_url)
    sales_page.should_be_category()
    sales_page.click_category()

    category_questionnaire_page = CategoryQuestionnairePage(browser, browser.current_url)
    category_questionnaire_page.answering_questionnaire(info)

    congratulations_page = CongratulationsPage(browser, browser.current_url)
    congratulations_page.should_be_congrats_text()
    congratulations_page.go_to_comparing_insurance_offers_page()

    comparing_insurance_offers_page = ComparingInsuranceOffersPage(browser, browser.current_url)
    comparing_insurance_offers_page.go_to_register_new_user()

    register_new_user_page = LoginPage(browser, browser.current_url)
    register_new_user_page.register_new_user(st.CORRECT_PASSWORD)

    provide_info_page = PersonalInfoPage(browser, browser.current_url)
    provide_info_page.provide_additional_info(st.CORRECT_BIRTHDATE, st.CORRECT_CITY, st.CORRECT_ZIPCODE, st.CORRECT_PHONE_NUMBER)

    payment_method_page = PaymentMethodPage(browser, browser.current_url)
    payment_method_page.go_to_review_contracts_term(st.CORRECT_IBAN)

    contract_terms_review_page = ContractTermsReviewPage(browser, browser.current_url)
    contract_terms_review_page.go_to_buy_contract()

    buying_confirmation_page = BuyingConfirmationPage(browser, browser.current_url)
    buying_confirmation_page.go_to_profile()

    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.should_be_contract()
