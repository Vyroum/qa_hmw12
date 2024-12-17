import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach



def pytest_addoption(parser):
    parser.addoption('--browser_version')
    parser.addoption('--browser_type')

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def browser_set(request):
    browser_version = request.config.getoption('--browser_version')
    browser_type = request.config.getoption('--browser_type')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_type,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "setSize": (1280, 1024)
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    options.page_load_strategy = 'eager'
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    #attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
