import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import generate_unique_email


class Test:
    base_url = 'https://learningbyo.got-it.io/'
    driver = None

    random_email = None
    test_password = 'TeStPa4SsWord@'
    google_email = 'lapdedkhost@gmail.com'
    google_password = 'n4won6qj'

    success_text = 'Your account has been successfully created'
    sign_in_google_text = 'Sign up with Google'

    def __init__(self):
        """Init Chrome selenium driver and setup implicit wait time"""

        self.driver = webdriver.Chrome(
            executable_path='./drivers/chromedriver'
        )
        self.driver.implicitly_wait(10)

    def start_test(self):
        """Start all tests"""

        self.test_valid_email_password()
        self.test_google_sign_up()
        self.breakdown_test()

    def prepare_test(self):
        """Prepare test sessions
        This function is to open home
        """
        # Clear sessions
        if self.driver.current_url != 'data:,':
            self.driver.execute_script('window.localStorage.clear();')

        # Open a new webpage
        self.driver.get(self.base_url)

        # Find sign up button and click to open modal
        sign_up_button = self.driver.find_element_by_xpath('//button[contains(text(), "Sign up")]')
        sign_up_button.click()

        # Generate random email
        self.random_email = generate_unique_email()

    def breakdown_test(self):
        """Breakdown tests"""

        # Close Chrome session
        self.driver.quit()

    def agree_terms_and_conditions(self):
        """Agree with terms and conditions"""

        # Find NEXT button
        self.wait_click_button(By.XPATH, '//button[contains(text(), "NEXT")]')

    def is_registered_successfully(self):
        """Checks if registration succeeded"""

        # Find the notification body

        try:
            self.driver.find_element_by_xpath(
                '//div[@class="modal-body" and contains(text(), "{}")]'.format(self.success_text)
            )

            return True
        except ElementNotVisibleException:
            return False

    def wait_click_button(self, by, selector):
        button = WebDriverWait(self.driver, 3) \
            .until(EC.element_to_be_clickable((by, selector)))
        button.click()

        return button

    def test_valid_email_password(self):
        """Test valid username and password
        Email will be randomly generated using the format: test.automation+{}@got-it.com
        """

        print('TEST 1: Register by valid email and password')

        # Prepare test
        self.prepare_test()

        # Input email and password
        email_input = self.driver.find_element_by_xpath('//*[@class="gi-AccountModal"]//input[@name="email"]')
        email_input.send_keys(self.random_email)

        password_inputs = self.driver.find_elements_by_xpath('//*[@class="gi-AccountModal"]//input[@type="password"]')
        for password_input in password_inputs:
            password_input.send_keys(self.test_password)

        # Click sign up button
        self.wait_click_button(By.ID, 'sign-up-button')

        # Agree terms & conditions
        self.agree_terms_and_conditions()

        success = self.is_registered_successfully()

        if success:
            print('-> Successfully!')
        else:
            print('-> Failed!')

    def test_google_sign_up(self):
        """Test sign up using Google"""

        print('TEST 2: Register by valid Google account')

        # Prepare test
        self.prepare_test()

        # Click on Google login button
        self.wait_click_button(By.XPATH, '//button[contains(text(), "{}")]'.format(self.sign_in_google_text))

        # Remember parent window
        parent_window = self.driver.current_window_handle

        # Switch to new window
        windows = self.driver.window_handles
        for window in windows:
            if window not in parent_window:
                self.driver.switch_to.window(window)

        # Input email and click next
        email_input = self.driver.find_element_by_xpath('//input[@name="identifier"]')
        email_input.send_keys(self.google_email)
        self.wait_click_button(By.ID, 'identifierNext')

        # Input password and click login
        password_input = self.driver.find_element_by_xpath('//input[@name="password"]')
        password_input.send_keys(self.google_password)

        # Click on login button
        time.sleep(2)
        login_button = self.driver.find_element_by_id('passwordNext')
        self.driver.execute_script("arguments[0].click();", login_button)

        # Switch to parent window
        time.sleep(3)
        self.driver.switch_to.window(parent_window)

        # Determine if user logs in or signs up
        try:
            # Agree terms & conditions
            self.agree_terms_and_conditions()

            success = self.is_registered_successfully()

            if success:
                return print('-> Successfully!')
        except ElementNotVisibleException and TimeoutException:
            # Look for user avatar
            avatar = self.driver.find_element_by_xpath('//*[contains(@class, "zmdi-account-circle")]')

            if avatar.is_displayed():
                return print('-> Successfully!')

        # If no action was taken, print out Failed
        print('-> Failed!')

