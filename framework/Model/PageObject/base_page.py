import selenium.common.exceptions


class BasePage(object):
    def __init__(self, browser, url, timeout=25):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except selenium.common.exceptions.NoSuchElementException:
            return False, f'Element {what} not found by {how}'
        return True

    def get_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except selenium.common.exceptions.NoSuchElementException:
            return False, f'Element {what} not found by {how}'
        return element

    def click(self, how, what):
        self.browser.find_element(how, what).click()

    def send_keys(self, how, what, key):
        self.browser.find_element(how, what).send_keys(key)
