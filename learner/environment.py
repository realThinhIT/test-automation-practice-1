from behave import use_fixture

from learner.fixtures import browser_chrome


def before_tag(context, tag):
    if tag.startswith('fixture.'):
        if tag == 'fixture.chrome':
            use_fixture(browser_chrome, context)
