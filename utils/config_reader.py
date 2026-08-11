import configparser
import os


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config.ini"
        )

        self.config.read(config_path)

    def get_base_url(self):
        return self.config.get("website", "base_url")

    def get_browser(self):
        return self.config.get("website", "browser")

    def get_headless(self):
        return self.config.getboolean("website", "headless")

    def get_search_product(self):
        return self.config.get("test_data", "search_product")

    def get_explicit_wait(self):
        return self.config.getint("timeouts", "explicit_wait")

    def get_log_level(self):
        return self.config.get("logging", "log_level")

    def get_log_file(self):
        return self.config.get("logging", "log_file")

    def get_report_directory(self):
        return self.config.get("reports", "report_directory")

    def get_screenshot_directory(self):
        return self.config.get("reports", "screenshot_directory")