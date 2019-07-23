from selenium.webdriver.common.by import By

from pom import BasePO


class TermsAndConditionsModal(BasePO):
    # Locators
    self_locator = By.CSS_SELECTOR, '#modal-terms-and-conditions'
    terms_and_conditions_next_button_locator = By.CSS_SELECTOR, \
        '#modal-terms-and-conditions button.gi-Button--lg.gi-Button--accent'

    # Element getters
    def get_self(self):
        return self.find_element(self.self_locator)

    # Element interactions
    def click_next_button(self):
        self.wait_click_button(self.terms_and_conditions_next_button_locator)
