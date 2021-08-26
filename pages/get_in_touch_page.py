from .base_page import BasePage
from .locators import GetInTouchLocators


class GetInTouchPage(BasePage):

    def should_be_contact_us_page(self):
        # проверка на корректный url адрес
        assert "contact" in self.browser.current_url, "NO contact us url"

    def fill_user_info(self):
        input1 = self.browser.find_element(*GetInTouchLocators.REGISTER_NAME)
        input1.send_keys('Anna')
        input2 = self.browser.find_element(*GetInTouchLocators.REGISTER_LASTNAME)
        input2.send_keys('Smith')
        input3 = self.browser.find_element(*GetInTouchLocators.REGISTER_EMAIL)
        input3.send_keys('annasmith@griddynamics.com')
        how_hear_list = self.browser.find_element(*GetInTouchLocators.REGISTER_HOW_HEAR)
        how_hear_list.click()
        online_ads_option = self.browser.find_element(*GetInTouchLocators.REGISTER_HOW_HEAR_ONLINE_ADS)
        online_ads_option.click()

        i_have_read_checkbox = self.browser.find_element(*GetInTouchLocators.I_HAVE_READ_CHECKBOX)
        i_have_read_checkbox.click()
        i_allow_checkbox = self.browser.find_element(*GetInTouchLocators.I_ALLOW_CHECKBOX)
        i_allow_checkbox.click()

    def should_be_inactive_contact_button(self):
        contact_button = self.browser.find_element(*GetInTouchLocators.CONTACT_BUTTON)
        assert not contact_button.is_enabled(), "contact button should be inactive"
