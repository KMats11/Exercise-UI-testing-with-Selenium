import logging
import sys
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class MainPage(BasePage):
    def open(self):
        """Open page by url."""
        logger.info("open url")
        self.browser.get(self.url)

    def open_about_page(self):
        """Open page 'About' by clicking the button."""
        logger.info("find element ABOUT_BUTTON")
        BasePage.click_on_element(self, *MainPageLocators.ABOUT_BUTTON, "button_about", 10)
        logger.info("click the button About")

    def is_element_present(self, how, what):
        """Check is there an element on the page.

        Keyword arguments:
        how -- method to find an element
        what -- locator of an element on the page"""
        with allure.step("check is element present"):
            try:
                logger.info(f"checking is element {what} present on the page")
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True

    def select_filter_by_topic(self):
        """Filter articles on the page by topic."""
        self.is_element_present(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        filter_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        ActionChains(self.browser).move_to_element(filter_topic).perform()
        BasePage.click_on_element(self, *MainPageLocators.FILTER_SELECT_BY_TOPIC, "filter_topic", 10)
        logger.info("click on Filter by topic")
        select_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_CLOUDDEVOPS)
        ActionChains(self.browser).move_to_element(select_topic).perform()
        BasePage.click_on_element(self, *MainPageLocators.FILTER_SELECT_CLOUDDEVOPS, "select_topic", 10)
        logger.info("click on Filter 'Cloud and devops'")

    def should_be_more_than_one_article(self, locator):
        """Check is there more than one article on the page."""
        logger.info("finding all articles on the page")
        articles = self.browser.find_elements(locator)
        assert articles > 1, "Should be more than one article"

    def reset_filters(self):
        """Set filters for articles on the first position."""

        logger.info("click on 'Filter by topic'")
        BasePage.click_on_element(self, *MainPageLocators.FILTER_SELECT_BY_ARTICLES, "article", 10)
        logger.info("click on 'All topics' filter to reset filter")
        BasePage.click_on_element(self, *MainPageLocators.FILTER_RESET_ARTICLES, "reset_article", 10)

        logger.info("click on 'Filter by article'")
        BasePage.click_on_element(self, *MainPageLocators.FILTER_SELECT_BY_TOPIC, "topic", 10)
        logger.info("click on Articles to reset filter")
        BasePage.click_on_element(self, *MainPageLocators.FILTER_RESET_TOPICS, "reset_topic", 10)

    def should_be_different_titles(self):
        """Check that titles of two articles are different."""
        logger.info("get text of the first article on page")
        first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE).text
        logger.info("get text of the first article by topic Cloud And Devops")
        clouddevops_first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE_CLOUDDEVOPS).text
        assert first_article_text != clouddevops_first_article_text, "Should be different articles"

    def open_getintouch_page(self):
        """Open 'Get in touch' page."""
        logger.info("clicking on Get In Touch button")
        with allure.step("opening Contacts page"):
            BasePage.click_on_element(self, *MainPageLocators.GET_IN_TOUCH_BUTTON, "getintouch_about", 10)
