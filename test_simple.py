import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope='session')
def browser_setup():
    browser.config.window_height = 1440
    browser.config.window_width = 768
    browser.open('https://google.com')


@pytest.fixture()
def input_clear():
    browser.element('[name="q"]').clear()


def test_search_true(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_neg(browser_setup, input_clear):
    browser.element('[name="q"]').should(be.blank).type('e32e2dewf314r2rfd3w').press_enter()
    browser.element('.card-section').should(have.text('По запросу e32e2dewf314r2rfd3w ничего не найдено.'))
