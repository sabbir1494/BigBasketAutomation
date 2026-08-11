from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.driver_factory import DriverFactory


driver = DriverFactory.get_driver()

home = HomePage(driver)
search = SearchPage(driver)
product = ProductPage(driver)
cart = CartPage(driver)

home.open_homepage()

print("===================================")
print("BigBasket Automation Started")
print("===================================")

# ===== Home Page =====

print("Title :", home.get_homepage_title())
print("URL :", home.get_homepage_url())
print("Homepage :", home.verify_homepage_loaded())
print("Search Box :", home.verify_search_box())

# ===== Search Product =====

print("\nSearching Product...")

home.search_product("Milk")

print("\nSearch Results :", search.verify_search_results())
print("First Product :", search.get_first_product_name())

search.open_first_product()

print("\nOpened First Product Successfully")

print("Current URL :", driver.current_url)
print("Current Title :", driver.title)

# ===== Product Page Verification =====

print("\nProduct Page Verification")

print("Product Title Visible :", product.verify_product_title())
print("Product Title :", product.get_product_title())

print("Product Price Visible :", product.verify_product_price())
print("Product Price :", product.get_product_price())

print("Product Image :", product.verify_product_image())

print("Add To Cart Button :", product.verify_add_to_cart_button())

# ===== Add To Cart =====

print("\nAdding Product To Cart...")

product.click_add_to_cart()

print("Product Added Successfully")

# ===== Cart =====

print("\nOpening Cart...")

cart.open_cart_sidebar()
cart.open_cart_page()

print("Cart Page :", cart.verify_cart_page())
print("Cart URL :", cart.get_cart_url())
print("Cart Title :", cart.get_cart_title())

print("\nIncreasing Quantity...")

cart.increase_quantity()

print("Quantity Increased Successfully")

print("\nDecreasing Quantity...")

cart.decrease_quantity()

print("Quantity Decreased Successfully")

print("\nRemoving Product From Cart...")

cart.remove_product()

print("Product Removed Successfully")

print("Cart Empty :", cart.verify_cart_empty())