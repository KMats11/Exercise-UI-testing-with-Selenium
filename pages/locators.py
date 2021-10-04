from selenium.webdriver.common.by import By


class MainPageLocators:
    ABOUT_BUTTON = (By.XPATH, "//a[text()=' About ']")
    FILTER_SELECT_BY_ARTICLES = (By.XPATH, "//div[@id='typelist']")  # "//span[@class='selected'][text()='Articles']")
    FILTER_SELECT_BY_TOPIC = (By.XPATH, "//div[@id='topiclist']")# /div/span[@class='selected']")  # "//span[@class='selected'][text()='All topics']"
    FILTER_SELECT_CLOUDDEVOPS = (By.XPATH, "//span[text()='Cloud and DevOps']")
    FILTER_RESET_ARTICLES = (By.XPATH, "//span[text()='Articles']")
    FILTER_RESET_TOPICS = (By.XPATH, "//span[text()='All topics']")
    FIRST_ARTICLE = (By.CSS_SELECTOR, "h4:nth-child(1) span")
    FIRST_ARTICLE_CLOUDDEVOPS = (By.XPATH, "//section[@class='domainblock cardright all cloud-and-devops']//article[1]//h4[1]")
    ARTICLES_CLOUDDEVOPS = (By.XPATH, "//section[@class='domainblock cardright all cloud-and-devops']//article")
    ARTICLES = (By.XPATH, "//article[1]")
    GET_IN_TOUCH_BUTTON = (By.XPATH, "//span[@class='ui-button-wrapper ui-button-block']") # //a[@aria-label='Get in touch button'][1] this selector isn't working properly


class AboutPageLocators:
    LEONARD_LIVSCHITZ_NAME = (By.XPATH, "//div[text()='Leonard Livschitz']")
    LEONARD_LIVSCHITZ_INFO_TEXT = (By.XPATH, "//p/span")


class GetInTouchLocators:
    REGISTER_NAME = (By.XPATH, "//input[@placeholder='First name*']")
    REGISTER_LASTNAME = (By.XPATH, "//input[@placeholder='Last name*']")
    REGISTER_EMAIL = (By.XPATH, "//input[@placeholder='E-mail*']")
    REGISTER_HOW_HEAR = (By.XPATH, "//gd-select-legacy[@placeholder='How did you hear about us?']")
    REGISTER_HOW_HEAR_ONLINE_ADS = (By.XPATH, "//gd-select-option-legacy[text()=' Online Ads ']")
    I_HAVE_READ_CHECKBOX = (By.XPATH, "//span[text()=' I have read and accepted the ']")
    I_ALLOW_CHECKBOX = (By.XPATH, "//span[text()=' I allow Grid Dynamics to contact me. ']")
    CONTACT_BUTTON = (By.XPATH, "//button [@title='Contact']")

