import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
