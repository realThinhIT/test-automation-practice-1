from behave import given, then, when

from config import Config
from pom.landing_page import LandingPage
from pom.modals.sign_up_modal import SignUpModal
from pom.modals.terms_and_conditions_modal import TermsAndConditionsModal
from pom.modals.congratulations_modal import CongratulationsModal


@given("I am looking at the landing page")
def step_impl(context):
    context.browser.get(Config.base_url)
    assert True


@given("I click on Sign Up button")
def step_impl(context):
    landing_page = LandingPage(context.browser)
    landing_page.click_sign_up_button()


@given("that the signup modal is visible")
def step_imp(context):
    sign_up_modal = SignUpModal(context.browser)

    assert sign_up_modal.get_self() is not None


@then("I should see a terms & conditions modal")
def step_imp(context):
    term_and_conditions = TermsAndConditionsModal(context.browser)
    is_terms_and_conditions_modal_visible = term_and_conditions.get_self() is not None

    # If terms and conditions modal not found, look for avatar to make sure the user has logged in
    is_avatar_visible = None
    if not is_terms_and_conditions_modal_visible:
        landing_page = LandingPage(context.browser)
        is_avatar_visible = landing_page.get_avatar_element() is not None

    # Update context for other steps
    context.is_terms_and_conditions_modal_visible = is_terms_and_conditions_modal_visible

    assert is_terms_and_conditions_modal_visible or is_avatar_visible


@when("I agree with terms & conditions")
def step_imp(context):
    if context.is_terms_and_conditions_modal_visible:
        terms_and_conditions_modal = TermsAndConditionsModal(context.browser)
        terms_and_conditions_modal.click_next_button()


@then("I should see the Congratulations modal")
def step_imp(context):
    landing_page = LandingPage(context.browser)
    congratulations_modal = CongratulationsModal(context.browser)

    if context.is_terms_and_conditions_modal_visible:
        assert congratulations_modal.get_self() is not None
    else:
        assert landing_page.get_avatar_element() is not None
