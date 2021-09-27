import logging
import sys
import allure
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class MainPage(BasePage):
    def open(self):
        """Open page by url."""
        logger.info("opening url")
        self.browser.get(self.url)

    def open_about_page(self):
        """Open page 'About' by clicking the button."""
        logger.info("finding element ABOUT_BUTTON")
        button_about = self.browser.find_element(*MainPageLocators.ABOUT_BUTTON)
        logger.info("clicking the button About")
        button_about.click()

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
        filter_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", filter_topic)
        logger.info("clicking on Filter by topic")
        filter_topic.click()
        select_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_CLOUDDEVOPS)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", select_topic)
        logger.info("clicking on Filter 'Cloud and devops'")
        select_topic.click()

    def should_be_more_than_one_article(self, locator):
        """Check is there more than one article on the page."""
        logger.info("finding all articles on the page")
        articles = self.browser.find_elements(locator)
        assert articles > 1, "Should be more than one article"

    def reset_filters(self):
        """Set filters for articles on the first position."""
        article = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        logger.info("clicking on 'Filter by topic'")
        article.click()
        reset_article = self.browser.find_element(*MainPageLocators.FILTER_RESET_ARTICLES)
        logger.info("clicking on 'All topics' filter to reset filter")
        reset_article.click()
        topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_ARTICLES)
        logger.info("clicking on 'Filter by article'")
        topic.click()
        reset_topic = self.browser.find_element(*MainPageLocators.FILTER_RESET_TOPICS)
        logger.info("clicking on Articles to reset filter")
        reset_topic.click()

    def should_be_different_titles(self):
        """Check that titles of two articles are different."""
        logger.info("get text of the first article on page")
        first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE).text
        logger.info("get text of the first article by topic Cloud And Devops")
        clouddevops_first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE_CLOUDDEVOPS).text
        assert first_article_text != clouddevops_first_article_text, "Should be different articles"

    def open_getintouch_page(self):
        """Open 'Get in touch' page."""
        getintouch_about = self.browser.find_element(*MainPageLocators.GET_IN_TOUCH_BUTTON)
        logger.info("clicking on Get In Touch button")
        with allure.step("opening Contacts page"):
            getintouch_about.click()
