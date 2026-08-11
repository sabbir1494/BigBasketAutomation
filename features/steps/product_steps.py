from behave import when, then

from pages.product_page import ProductPage


@when("the user adds the product to the cart")
def step_add_product_to_cart(context):
    context.product = ProductPage(context.driver)
    context.product.add_to_cart()


@then("the product name should be displayed")
def step_verify_product_name(context):
    context.product = ProductPage(context.driver)
    assert context.product.verify_product_name()


@then("the product price should be displayed")
def step_verify_product_price(context):
    assert context.product.verify_product_price()


@then("the product image should be displayed")
def step_verify_product_image(context):
    assert context.product.verify_product_image()


@then("the product availability should be displayed")
def step_verify_product_availability(context):
    assert context.product.verify_product_availability()


@then("the product should be added successfully")
def step_product_added(context):
    assert True