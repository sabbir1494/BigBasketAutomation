from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        config = ConfigReader()

        options = webdriver.ChromeOptions()

        if config.get_headless():
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.implicitly_wait(0)

        return driver