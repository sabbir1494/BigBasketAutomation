from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        "h1.product_title"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "p.price"
    )

    PRODUCT_IMAGE = (
        By.CSS_SELECTOR,
        ".woocommerce-product-gallery img"
    )

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button.single_add_to_cart_button"
    )

    def verify_product_name(self):
        return self.is_displayed(self.PRODUCT_TITLE)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_TITLE)

    def verify_product_title(self):
        return self.is_displayed(self.PRODUCT_TITLE)

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def verify_product_price(self):
        return self.is_displayed(self.PRODUCT_PRICE)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)

    def verify_product_image(self):
        return self.is_displayed(self.PRODUCT_IMAGE)

    def verify_product_availability(self):
        return self.is_displayed(self.ADD_TO_CART_BUTTON)

    def verify_add_to_cart_button(self):
        return self.is_displayed(self.ADD_TO_CART_BUTTON)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)