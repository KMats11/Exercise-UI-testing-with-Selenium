import logging
import sys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import GetInTouchLocators, MainPageLocators

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class GetInTouchPage(BasePage):

    def should_be_contact_us_page(self):
        """Check if the opened page is 'Contact us' page."""
        assert "contact" in self.browser.current_url, "NOT contact us url"

    def fill_user_info(self):
        """Fill information fields about user and click on checkboxes."""
        input1 = self.browser.find_element(*GetInTouchLocators.REGISTER_NAME)
        logger.info("fill name form with 'Anna'")
        input1.send_keys('Anna')
        input2 = self.browser.find_element(*GetInTouchLocators.REGISTER_LASTNAME)
        logger.info("fill last name form with 'Smith'")
        input2.send_keys('Smith')
        input3 = self.browser.find_element(*GetInTouchLocators.REGISTER_EMAIL)
        logger.info("fill e-mail form with 'annasmith@griddynamics.com'")
        input3.send_keys('annasmith@griddynamics.com')
        logger.info("click on 'How did you hear about us?'")
        self.click_on_element(*GetInTouchLocators.REGISTER_HOW_HEAR, "how_hear_list", 10)
        logger.info("click on 'Online Ads'")
        self.click_on_element(*GetInTouchLocators.REGISTER_HOW_HEAR_ONLINE_ADS, "online_ads_option", 10)

        logger.info("Click on checkbox 'I have read and accepted the Terms & Conditions and Privacy Policy'")
        BasePage.click_on_element(self, *GetInTouchLocators.I_HAVE_READ_CHECKBOX, "i_have_read_checkbox", 10)
        logger.info("Click on checkbox 'I allow Grid Dynamics to contact me'")
        BasePage.click_on_element(self, *GetInTouchLocators.I_ALLOW_CHECKBOX, "i_allow_checkbox", 10)

    def should_be_inactive_contact_button(self):
        """Check if the 'Contact' button is inactive."""
        contact_button = self.browser.find_element(*GetInTouchLocators.CONTACT_BUTTON)
        assert not contact_button.is_enabled(), "contact button should be inactive"
