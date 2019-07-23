import time

from behave import when, then

from config import Config
from pom.landing_page import LandingPage
from pom.modals.sign_up_modal import SignUpModal
from pom.windows.google_authentication import GoogleAuthenticationWindow
from pom.modals.terms_and_conditions_modal import TermsAndConditionsModal
from pom.modals.congratulations_modal import CongratulationsModal

######################
# Sign up using Google Account
######################
@when("I click the Sign Up with Google button")
def step_imp(context):
    # Set landing page context for the current test
    landing_page = LandingPage(context.browser)
    context.landing_page = landing_page

    # Click login with Google button
    sign_up_modal = SignUpModal(context.browser)
    sign_up_modal.click_sign_up_with_google_button()


@then("I should see a Google Login window open up")
def step_imp(context):
    # Check if google auth popup is present
    assert len(context.browser.window_handles) == 2


@then("I switch to that window")
def step_imp(context):
    context.landing_page.switch_to_new_window()


@when("I type in my Google email address")
def step_imp(context):
    google_auth = GoogleAuthenticationWindow(context.browser)
    google_auth.enter_email(Config.google_email)


@when("I click Next to switch to password prompt page")
def step_imp(context):
    google_auth = GoogleAuthenticationWindow(context.browser)
    google_auth.click_email_next_button()


@then("I should see the password input page coming up")
def step_imp(context):
    google_auth = GoogleAuthenticationWindow(context.browser)
    assert google_auth.get_password_input() is not None


@when("I type in my Google password")
def step_imp(context):
    google_auth = GoogleAuthenticationWindow(context.browser)
    google_auth.enter_password(Config.google_password)


@when("I click Next to confirm my authentication")
def step_imp(context):
    google_auth = GoogleAuthenticationWindow(context.browser)
    google_auth.click_password_next_button()


@then("The popup window should be closed")
def step_imp(context):
    context.landing_page.switch_to_parent()

    tries_count = 1

    while True:
        tries_count = tries_count + 1

        if tries_count == 30:
            assert False

        if len(context.browser.window_handles) == 1:
            assert True
            break
        else:
            time.sleep(0.5)
