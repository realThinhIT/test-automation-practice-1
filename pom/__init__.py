from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePO(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(locator[0], locator[1])
        except ElementNotVisibleException and NoSuchElementException:
            return None

    def find_elements(self, locator):
        try:
            return self.driver.find_elements(locator[0], locator[1])
        except ElementNotVisibleException:
            return None

    def wait_click_button(self, locator):
        button = WebDriverWait(self.driver, 10) \
            .until(expected_conditions.element_to_be_clickable(locator))
        button.click()

        return button
