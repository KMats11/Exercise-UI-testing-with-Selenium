import logging
import sys
import time

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
        logger.info("Find element ABOUT_BUTTON")
        self.click_on_element(*MainPageLocators.ABOUT_BUTTON, "button_about", 10)

    def is_element_present(self, how, what):
        """Check is there an element on the page.

        Keyword arguments:
        how -- method to find an element
        what -- locator of an element on the page"""
        with allure.step("Check is element present"):
            try:
                logger.info(f"Check is element {what} present on the page")
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((how, what))
                )
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True

    def scroll_to_element(self, how, what):
        element = self.browser.find_element(how, what)
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.browser.execute_script('return window.innerHeight') / 2) + self.browser.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        self.browser.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def select_filter_by_topic(self):
        """Filter articles on the page by topic."""
        self.is_element_present(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        self.scroll_to_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        time.sleep(3)
        self.click_on_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC, "filter_topic", 10)
        select_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_CLOUDDEVOPS)
        ActionChains(self.browser).move_to_element(select_topic).perform()
        self.click_on_element(*MainPageLocators.FILTER_SELECT_CLOUDDEVOPS, "select_topic 'Cloud and devops'", 10)

    def should_be_more_than_one_article(self, locator):
        """Check is there more than one article on the page."""
        logger.info("Find all articles on the page")
        articles = self.browser.find_elements(*locator)
        assert len(articles) > 1, "Should be more than one article"

    def reset_filters(self):
        """Set filters for articles on the first position."""

        self.click_on_element(*MainPageLocators.FILTER_SELECT_BY_ARTICLES, "article", 10)
        self.click_on_element(*MainPageLocators.FILTER_RESET_ARTICLES, "'All articles' reset_article", 10)

        self.click_on_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC, "topic", 10)
        self.click_on_element(*MainPageLocators.FILTER_RESET_TOPICS, "'All topics' reset_topic", 10)

    def should_be_different_titles(self):
        """Check that titles of two articles are different."""
        logger.info("Get text of the first article on page")
        first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE).text
        logger.info("Get text of the first article by topic Cloud And Devops")
        clouddevops_first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE_CLOUDDEVOPS).text
        assert first_article_text != clouddevops_first_article_text, "Should be different articles"

    def open_getintouch_page(self):
        """Open 'Get in touch' page."""
        with allure.step("Open Contacts page"):
            self.click_on_element(*MainPageLocators.GET_IN_TOUCH_BUTTON, "'Get in touch' button", 10)
