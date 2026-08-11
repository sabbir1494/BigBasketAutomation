from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (
        By.NAME,
        "s"
    )

    PRODUCT_LIST = (
        By.CSS_SELECTOR,
        "li.product-wrap"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "li.product-wrap h3.woocommerce-loop-product__title a"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "li.product-wrap span.price"
    )

    def search_product(self, product):
        search_box = self.find_element(self.SEARCH_BOX)

        search_box.clear()
        search_box.click()
        search_box.send_keys(product)
        search_box.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.PRODUCT_LIST)
        )

    def verify_search_results(self):
        return self.is_displayed(self.PRODUCT_LIST)

    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT)

    def open_first_product(self):
        product = self.find_element(self.FIRST_PRODUCT)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            product
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )