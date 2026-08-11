from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "a.login.inline-type"
    )

    EMAIL_FIELD = (
        By.ID,
        "username"
    )

    PASSWORD_FIELD = (
        By.ID,
        "password"
    )

    SUBMIT_BUTTON = (
        By.NAME,
        "login"
    )

    CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button.mfp-close"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "p.submit-status"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_login(self):
        self.click(self.LOGIN_BUTTON)

    def verify_email_field(self):
        return self.is_displayed(self.EMAIL_FIELD)

    def verify_mobile_field(self):
        return False

    def verify_password_field(self):
        return self.is_displayed(self.PASSWORD_FIELD)

    def enter_email(self, email):
        self.type(self.EMAIL_FIELD, email)

    def enter_mobile(self, mobile):
        pass

    def enter_password(self, password):
        self.type(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.SUBMIT_BUTTON)

    def close_login_popup(self):
        self.click(self.CLOSE_BUTTON)

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except Exception:
            return ""