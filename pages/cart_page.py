from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ICON = (
        By.CSS_SELECTOR,
        "a.cart-toggle"
    )

    VIEW_CART_BUTTON = (
        By.CSS_SELECTOR,
        "a.button.wc-forward"
    )

    PLUS_BUTTON = (
        By.CSS_SELECTOR,
        "button.quantity-plus"
    )

    MINUS_BUTTON = (
        By.CSS_SELECTOR,
        "button.quantity-minus"
    )

    REMOVE_BUTTON = (
        By.CSS_SELECTOR,
        "a.remove"
    )

    EMPTY_CART_MESSAGE = (
        By.CSS_SELECTOR,
        "div.woocommerce-info"
    )

    BODY = (
        By.TAG_NAME,
        "body"
    )

    def open_cart_sidebar(self):
        cart = self.find_element(self.CART_ICON)

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )

        time.sleep(2)

    def open_cart_page(self):
        buttons = self.driver.find_elements(
            *self.VIEW_CART_BUTTON
        )

        if not buttons:
            raise Exception("VIEW CART button was not found.")

        self.driver.execute_script(
            "arguments[0].click();",
            buttons[0]
        )

        time.sleep(3)

    def open_cart(self):
        self.open_cart_sidebar()
        self.open_cart_page()

    def increase_quantity(self):
        plus = self.find_element(self.PLUS_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            plus
        )

        ActionChains(self.driver).move_to_element(plus).perform()

        self.driver.execute_script(
            "arguments[0].click();",
            plus
        )

        time.sleep(2)

    def decrease_quantity(self):
        minus = self.find_element(self.MINUS_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            minus
        )

        ActionChains(self.driver).move_to_element(minus).perform()

        self.driver.execute_script(
            "arguments[0].click();",
            minus
        )

        time.sleep(2)

    def remove_product(self):
        remove = self.find_element(self.REMOVE_BUTTON)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            remove
        )

        self.driver.execute_script(
            "arguments[0].click();",
            remove
        )

        time.sleep(3)

    def verify_cart_page(self):
        return "/cart" in self.get_current_url()

    def get_cart_url(self):
        return self.get_current_url()

    def get_cart_title(self):
        return self.get_title()

    def verify_cart_empty(self):
        try:
            message = self.find_element(
                self.EMPTY_CART_MESSAGE
            )

            return (
                "Your cart is currently empty."
                in message.text
            )

        except Exception:
            return False
        
    def verify_empty_cart(self):
        return self.verify_cart_empty()
    
    def verify_cart_product(self):
        return "/cart" in self.get_current_url() or "cart" in self.get_current_url().lower()