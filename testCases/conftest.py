from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import pytest


def  pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise  ValueError("unsupported browser")
    return  driver

########## for pytest html reports #########
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Ecommerce Project, nopcommerece'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Priyanka'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Packages',None)
    metadata.pop('Plugins', None)

