import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='session')
def browser_setup():
    browser.config.window_height = 1600
    browser.config.window_width = 1600
    browser.open('https://google.com')


def test_search_true(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_search_neg(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('e32e2dewf314r2rfd3w').press_enter()
    browser.element('.card-section').should(have.text('По запросу e32e2dewf314r2rfd3w ничего не найдено.'))
