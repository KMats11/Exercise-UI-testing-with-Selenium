import allure
import pytest
from pages.about_page import AboutPage
from pages.main_page import MainPage
from pages.get_in_touch_page import GetInTouchPage
from pages.locators import MainPageLocators, AboutPageLocators

URL = "https://blog.griddynamics.com/"


@allure.title('Verify that information about Leonard Livschitz is right')
def test_text_about_director_presented(browser):
    page = MainPage(browser, URL)
    page.open()
    page.open_about_page()
    about_page = AboutPage(browser, browser.current_url)
    about_page.open_text_about(*AboutPageLocators.LEONARD_LIVSCHITZ_NAME)
    about_page.should_be_about_text()


@allure.title('Verify that topic filter is working and there more than one article in some topic')
# @pytest.mark.xfail(reason="the element - filter by 'All Topics' - on the page is not clickable any more")
def test_more_than_one_article_in_topic(browser):
    page = MainPage(browser, URL)
    page.open()
    page.select_filter_by_topic()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES_CLOUDDEVOPS)
    page.reset_filters()
    page.should_be_different_titles()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES)


@allure.title('Verify that if not all required text fields are filled,contact button is inactive')
def test_get_in_touch_contact_button_inactive(browser):
    page = MainPage(browser, URL)
    page.open()
    page.open_getintouch_page()
    getintouch_page = GetInTouchPage(browser, browser.current_url)
    getintouch_page.should_be_contact_us_page()
    getintouch_page.fill_user_info()
    getintouch_page.should_be_inactive_contact_button()
