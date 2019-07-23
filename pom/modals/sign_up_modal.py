from selenium.webdriver.common.by import By

from pom import BasePO


class SignUpModal(BasePO):
    # Locators
    self_locator = By.CSS_SELECTOR, '#modal-signup'
    email_input_locator = By.CSS_SELECTOR, '.gi-AccountModal input[name="email"]'
    password_input_locator = By.CSS_SELECTOR, '.gi-AccountModal input[type="password"]'
    sign_up_button_locator = By.ID, 'sign-up-button'
    sign_up_with_google_button_locator = By.CSS_SELECTOR, '.gi-Button--Google'

    # Element getters
    def get_self(self):
        return self.find_element(self.self_locator)

    def get_email_input(self):
        return self.find_element(self.email_input_locator)

    def get_password_inputs(self):
        return self.find_elements(self.password_input_locator)

    def get_sign_up_button(self):
        return self.find_element(self.sign_up_button_locator)

    # Element interactions
    def click_sign_up_button(self):
        self.wait_click_button(self.sign_up_button_locator)

    def click_sign_up_with_google_button(self):
        self.wait_click_button(self.sign_up_with_google_button_locator)

    def enter_email(self, email):
        input_ = self.get_email_input()
        input_.send_keys(email)

    def enter_passwords(self, password):
        inputs = self.get_password_inputs()
        for input_ in inputs:
            input_.send_keys(password)
