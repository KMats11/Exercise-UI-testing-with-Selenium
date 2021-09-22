class BasePage():
    def __init__(self, browser, url):
        """Start Chrome browser for testing."""

        self.browser = browser
        self.url = url
