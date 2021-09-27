import sys
import pytest
from selenium import webdriver
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


@pytest.fixture(scope="function")
def browser():
    """start browser for each test"""
    logger.info('start chrome browser for test')
    browser = webdriver.Chrome()
    yield browser
    logger.info('quit browser')
    browser.quit()
