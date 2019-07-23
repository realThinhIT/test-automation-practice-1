from behave.fixture import fixture
from selenium import webdriver


@fixture
def browser_chrome(context):
    # Setup tests
    context.browser = webdriver.Chrome(
        executable_path='./drivers/chromedriver'
    )

    context.browser.implicitly_wait(10)

    yield context.browser

    # Breakdown tests
    context.browser.quit()
