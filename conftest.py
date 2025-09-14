import pytest
from selene import browser


@pytest.fixture()
def open_browser():

    browser.driver.maximize_window()
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    yield browser

    browser.quit()


