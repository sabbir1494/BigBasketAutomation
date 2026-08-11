from behave import when, then

from pages.search_page import SearchPage


@when('the user searches for "{product}"')
def step_search_product(context, product):
    context.search = SearchPage(context.driver)
    context.search.search_product(product)


@then("search results should be displayed")
def step_verify_search_results(context):
    assert context.search.verify_search_results()


@when("the user opens the first product")
def step_open_first_product(context):
    context.search.open_first_product()