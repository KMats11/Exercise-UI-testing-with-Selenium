import logging
import sys
from pexpect import TIMEOUT
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class BasePage:
    def __init__(self, browser, url):
        """Start Chrome browser for testing."""
        self.browser = browser
        self.url = url

    def click_on_element(self, how, what, alias, timeout=TIMEOUT):
        try:
            logger.info(f'Click on element: {alias}')
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except (TimeoutException, NoSuchElementException):
            logger.warning(f'Element not found: {alias}')
            return False
        element.click()
        return
