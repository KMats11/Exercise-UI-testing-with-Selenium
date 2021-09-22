from .base_page import BasePage
from .locators import AboutPageLocators


class AboutPage(BasePage):
    def open_text_about(self):
        """Click on the Leonard Livschitz name and opens text about him."""

        director_name = self.browser.find_element(*AboutPageLocators.LEONARD_LIVSCHITZ_NAME)
        director_name.click()

    def should_be_about_text(self):
        """Check is there expected text in the 'About Leonard Livschitz text'."""

        fact_text = self.browser.find_element(*AboutPageLocators.LEONARD_LIVSCHITZ_INFO_TEXT).text
        expected_text = "director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014"
        assert expected_text in fact_text, 'wrong text in the "about director" form'
