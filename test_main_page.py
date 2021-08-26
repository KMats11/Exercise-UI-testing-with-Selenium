import pytest
from pages.about_page import AboutPage
from pages.main_page import MainPage
from pages.get_in_touch_page import GetInTouchPage
from pages.locators import MainPageLocators


@pytest.mark.case3
def test_get_in_touch(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_getintouch_page()
    getintouch_page = GetInTouchPage(browser, browser.current_url)
    getintouch_page.should_be_contact_us_page()
    getintouch_page.fill_user_info()
    getintouch_page.should_be_inactive_contact_button()


@pytest.mark.case1
def test_text_about_director_presented(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_about_page()
    about_page = AboutPage(browser, browser.current_url)
    about_page.open_text_about()
    about_page.should_be_about_text()


@pytest.mark.case2
def test_cloud_devops(browser):
    link = "https://blog.griddynamics.com/"
    page = MainPage(browser, link)
    page.open()
    page.select_filter_by_topic()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES_CLOUDDEVOPS)
    page.reset_filters()
    page.should_be_different_titles()
    page.should_be_more_than_one_article(MainPageLocators.ARTICLES)