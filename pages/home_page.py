from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class HomePage(BasePage):

    SEARCH_BOX = (
        By.NAME,
        "s"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-search"
    )

    LOGO = (
    By.CSS_SELECTOR,
    "a[href='https://bigbasket.com.bd/'] img"
    )

    BODY = (
        By.TAG_NAME,
        "body"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigReader()

    def open_homepage(self):
        self.open_url(self.config.get_base_url())

    def get_homepage_title(self):
        return self.get_title()

    def get_homepage_url(self):
        return self.get_current_url()

    def verify_homepage_loaded(self):
        return self.is_displayed(self.BODY)

    def verify_search_box(self):
        return self.is_displayed(self.SEARCH_BOX)

    def verify_logo(self):
        return self.is_displayed(self.LOGO)

    def search_product(self, product):
        search_box = self.find_element(self.SEARCH_BOX)

        search_box.clear()
        search_box.click()
        search_box.send_keys(product)
        search_box.send_keys(Keys.ENTER)