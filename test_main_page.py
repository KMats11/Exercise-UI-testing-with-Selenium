import pytest
import allure
from pages.about_page import AboutPage
from pages.main_page import MainPage
from pages.get_in_touch_page import GetInTouchPage
from pages.locators import MainPageLocators


@allure.title('Verify that information about Leonard Livschitz is right')
def test_text_about_director_presented(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_about_page()
    about_page = AboutPage(browser, browser.current_url)
    about_page.open_text_about()
    about_page.should_be_about_text()


@allure.title('Verify that topic filter is working and there more than one article in some topic')
def test_more_than_one_article_in_topic(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.is_element_present(*MainPageLocators.FILTER_SELECT_BY_TOPIC)
    page.select_filter_by_topic()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES_CLOUDDEVOPS)
    page.reset_filters()
    page.should_be_different_titles()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES)


@allure.title('Verify that if not all required text fields are filled,contact button is inactive')
def test_get_in_touch_contact_button_inabled(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_getintouch_page()
    getintouch_page = GetInTouchPage(browser, browser.current_url)
    getintouch_page.should_be_contact_us_page()
    getintouch_page.fill_user_info()
    getintouch_page.should_be_inactive_contact_button()
