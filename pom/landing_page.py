from selenium.webdriver.common.by import By

from pom import BasePO


class LandingPage(BasePO):
    # Locators
    sign_up_button_locator = By.CSS_SELECTOR, '.gi-navBar-Login .gi-Button'
    avatar_locator = By.XPATH, '//*[contains(@class, "zmdi-account-circle")]'

    def __init__(self, driver):
        super(LandingPage, self).__init__(driver)

        self.parent_handler = self.driver.current_window_handle

    # Element getters
    def get_avatar_element(self):
        return self.find_element(self.avatar_locator)

    # Element interactions
    def click_sign_up_button(self):
        self.find_element(self.sign_up_button_locator).click()

    # Windows interactions
    def switch_to_new_window(self):
        # Switch to new window
        windows = self.driver.window_handles
        for window in windows:
            if window not in self.parent_handler:
                self.driver.switch_to.window(window)

    def switch_to_parent(self):
        self.driver.switch_to.window(self.parent_handler)
