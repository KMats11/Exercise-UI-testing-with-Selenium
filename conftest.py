import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope="function")
def browser():
    """start browser for each test"""
    logging.info('start chrome browser for test')
    browser = webdriver.Chrome()
    yield browser
    logging.info('quit browser')
    browser.quit()
