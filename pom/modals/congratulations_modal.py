from selenium.webdriver.common.by import By

from pom import BasePO


class CongratulationsModal(BasePO):
    # Locators
    self_locator = By.CSS_SELECTOR, '#modal-lnd-signup-success'

    # Element getters
    def get_self(self):
        return self.find_element(self.self_locator)
