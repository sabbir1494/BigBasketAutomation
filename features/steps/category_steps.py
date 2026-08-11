from behave import when, then

from pages.category_page import CategoryPage


@when("the user opens the category menu")
def step_open_category_menu(context):
    context.category = CategoryPage(context.driver)
    context.category.open_category_menu()


@when("the user opens the first category")
def step_open_first_category(context):
    context.category.open_first_category()


@then("category products should be displayed")
def step_verify_category_products(context):
    assert context.category.verify_category_products()


@then("the filter section should be displayed")
def step_verify_filter_section(context):
    assert context.category.verify_filter_section()


@then("the brand filter should be displayed")
def step_verify_brand_filter(context):
    assert context.category.verify_brand_filter()


@then("the price filter should be displayed")
def step_verify_price_filter(context):
    assert context.category.verify_price_filter()