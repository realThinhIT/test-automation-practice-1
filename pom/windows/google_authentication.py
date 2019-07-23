from selenium.webdriver.common.by import By

from pom import BasePO


class GoogleAuthenticationWindow(BasePO):
    # Locators
    self_locator = By.CSS_SELECTOR, '#modal-lnd-signup-success'
    username_input_locator = By.CSS_SELECTOR, 'input[name="identifier"]'
    username_next_button_locator = By.ID, 'identifierNext'
    password_input_locator = By.CSS_SELECTOR, 'input[name="password"]'
    password_next_button_locator = By.ID, 'passwordNext'

    # Element getters
    def get_self(self):
        return self.find_element(self.self_locator)

    def get_email_input(self):
        return self.find_element(self.username_input_locator)

    def get_password_input(self):
        return self.find_element(self.password_input_locator)

    def get_email_next_button(self):
        return self.find_element(self.username_next_button_locator)

    def get_password_next_button(self):
        return self.find_element(self.password_next_button_locator)

    # Element interactions
    def enter_email(self, email):
        input_ = self.get_email_input()
        input_.send_keys(email)

    def enter_password(self, password):
        input_ = self.get_password_input()
        input_.send_keys(password)

    def click_email_next_button(self):
        self.wait_click_button(self.username_next_button_locator)

    def click_password_next_button(self):
        button = self.find_element(self.password_next_button_locator)
        self.driver.execute_script("arguments[0].click();", button)
