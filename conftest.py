import pytest
from selenium import webdriver
import logging


@pytest.fixture(scope="function")
def browser():
    # logging.basicConfig(level=logging.INFO)
    logging.info('start chrome browser for test')
    browser = webdriver.Chrome()
    yield browser
    logging.info('quit browser')
    browser.quit()
