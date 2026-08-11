from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FooterPage(BasePage):

    FOOTER = (
        By.TAG_NAME,
        "footer"
    )

    FOOTER_LINKS = (
        By.CSS_SELECTOR,
        "footer a"
    )

    # IMPORTANT:
    # Actual href is absolute URL, so use contains()

    ABOUT_US = (
        By.XPATH,
        "//a[contains(@href, '/about-us/')]"
    )

    CONTACT_US = (
        By.XPATH,
        "//a[contains(@href, '/contact-us/')]"
    )

    PRIVACY_POLICY = (
        By.XPATH,
        "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'privacy')]"
    )

    TERMS = (
        By.XPATH,
        "//a[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'terms')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # -------------------------
    # Footer
    # -------------------------

    def scroll_to_footer(self):
        self.scroll_to_element(self.FOOTER)

    def verify_footer(self):
        return self.is_displayed(self.FOOTER)

    def verify_footer_links(self):
        return len(
            self.driver.find_elements(*self.FOOTER_LINKS)
        ) > 0

    # -------------------------
    # About Us
    # -------------------------

    def open_about_us(self):

        elements = self.driver.find_elements(*self.ABOUT_US)

        if not elements:
            raise Exception("About Us link was not found")

        element = elements[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # -------------------------
    # Contact Us
    # -------------------------

    def open_contact_us(self):

        elements = self.driver.find_elements(*self.CONTACT_US)

        if not elements:
            raise Exception("Contact Us link was not found")

        element = elements[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # -------------------------
    # Privacy Policy
    # -------------------------

    def open_privacy_policy(self):

        elements = self.driver.find_elements(*self.PRIVACY_POLICY)

        if not elements:
            raise Exception("Privacy Policy link was not found")

        element = elements[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # -------------------------
    # Terms
    # -------------------------

    def open_terms(self):

        elements = self.driver.find_elements(*self.TERMS)

        if not elements:
            raise Exception("Terms link was not found")

        element = elements[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )