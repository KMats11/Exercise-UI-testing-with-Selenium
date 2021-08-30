import allure
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException



class MainPage(BasePage):
    @allure.step('1')
    def open(self):
        self.browser.get(self.url)

    @allure.step('2')
    def open_about_page(self):
        button_about = self.browser.find_element(*MainPageLocators.ABOUT_BUTTON)
        button_about.click()

    @allure.step('2')
    def is_element_present(self, how, what):
        with allure.step("is element present"):
            try:
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True

    @allure.step('3')
    def select_filter_by_topic(self):
        filter_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", filter_topic)
        filter_topic.click()
        select_topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_CLOUDDEVOPS)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", select_topic)
        select_topic.click()

    @allure.step('4')
    def should_be_more_than_one_article(self, locator):
        articles = self.browser.find_elements(locator)
        assert articles > 1, "Should be more than one article"

    @allure.step('5')
    def reset_filters(self):
        article = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
        article.click()
        reset_article = self.browser.find_element(*MainPageLocators.FILTER_RESET_ARTICLES)
        reset_article.click()
        topic = self.browser.find_element(*MainPageLocators.FILTER_SELECT_BY_ARTICLES)
        topic.click()
        reset_topic = self.browser.find_element(*MainPageLocators.FILTER_RESET_TOPICS)
        reset_topic.click()

    @allure.step('6')
    def should_be_different_titles(self):
        first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE).text
        clouddevops_first_article_text = self.browser.find_element(*MainPageLocators.FIRST_ARTICLE_CLOUDDEVOPS).text
        assert first_article_text != clouddevops_first_article_text, "Should be different articles"

    @allure.step('2')
    def open_getintouch_page(self):
        getintouch_about = self.browser.find_element(*MainPageLocators.GET_IN_TOUCH_BUTTON)
        with allure.step("opening Contacts page"):
            getintouch_about.click()
