import logging
import sys
from .base_page import BasePage
from .locators import AboutPageLocators

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class AboutPage(BasePage):
    def open_text_about(self, how, what):
        """Click on the name and open text about him.

        Keyword arguments:
        how -- method to find an element
        what -- locator of an element on the page"""
        logger.info("click on name to open text about")
        BasePage.click_on_element(self, how, what, "director_name", 10)

    def should_be_about_text(self):
        """Check is there expected text in the 'About text'."""
        logger.info("finding info About text on the page")
        actual_text = self.browser.find_element(*AboutPageLocators.LEONARD_LIVSCHITZ_INFO_TEXT).text
        expected_text = ("director of Grid Dynamics’ board of directors since 2006 and the Chief "
                         "Executive Officer of Grid Dynamics since 2014")
        assert expected_text in actual_text, f'actual result:{actual_text}, expected text: {expected_text}'
