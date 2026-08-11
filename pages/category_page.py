from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):

    CATEGORY_MENU = (
    By.CSS_SELECTOR,
    "a.dropdown-menu-toggle"
    )

    CATEGORY_ITEM = (
    By.CSS_SELECTOR,
    "#menu-item-1237 > a"
    )   

    PRODUCT_LIST = (
    By.CSS_SELECTOR,
    "ul.products li.product-wrap"
    )

    FILTER_SECTION = (
    By.CSS_SELECTOR,
    ".sidebar-content"
    )

    PRICE_FILTER = (
    By.ID,
    "woocommerce_price_filter-2"
    )   

    def open_category_menu(self):
        self.click(self.CATEGORY_MENU)

    def open_first_category(self):
        self.click(self.CATEGORY_ITEM)

    def verify_category_products(self):
        return self.is_displayed(self.PRODUCT_LIST)

    def verify_filter_section(self):
        return self.is_displayed(self.FILTER_SECTION)

    def verify_price_filter(self):
        return self.is_displayed(self.PRICE_FILTER)