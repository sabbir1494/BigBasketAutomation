from selenium.webdriver.common.by import By


class HelperUtils:

    @staticmethod
    def get_locator(locator_type, locator_value):

        locator_type = locator_type.lower()

        if locator_type == "id":
            return (By.ID, locator_value)

        elif locator_type == "name":
            return (By.NAME, locator_value)

        elif locator_type == "xpath":
            return (By.XPATH, locator_value)

        elif locator_type == "css":
            return (By.CSS_SELECTOR, locator_value)

        elif locator_type == "class":
            return (By.CLASS_NAME, locator_value)

        elif locator_type == "tag":
            return (By.TAG_NAME, locator_value)

        elif locator_type == "link_text":
            return (By.LINK_TEXT, locator_value)

        elif locator_type == "partial_link_text":
            return (By.PARTIAL_LINK_TEXT, locator_value)

        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")