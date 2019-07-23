from behave import when, then

from utils import generate_unique_email
from pom.modals.sign_up_modal import SignUpModal
from pom.modals.terms_and_conditions_modal import TermsAndConditionsModal
from pom.modals.congratulations_modal import CongratulationsModal

from config import Config

######################
# Sign up using email and password
######################
@when("I type in valid email and password")
def step_imp(context):
    sign_up_modal = SignUpModal(context.browser)
    sign_up_modal.enter_email(generate_unique_email())
    sign_up_modal.enter_passwords(Config.test_password)


@when("I click Sign Up button")
def step_imp(context):
    sign_up_modal = SignUpModal(context.browser)
    sign_up_modal.click_sign_up_button()

