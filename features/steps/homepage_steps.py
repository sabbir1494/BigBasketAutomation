from behave import given, then

from pages.home_page import HomePage


@given("the user opens the BigBasket Bangladesh website")
def step_open_homepage(context):
    context.home = HomePage(context.driver)
    context.home.open_homepage()


@then("the homepage should load successfully")
def step_homepage_loaded(context):
    assert context.home.verify_homepage_loaded()


@then("the homepage title should be displayed")
def step_verify_title(context):
    assert context.home.get_homepage_title() != ""


@then("the homepage URL should be correct")
def step_verify_url(context):
    assert "bigbasket" in context.home.get_homepage_url().lower()


@then("the search box should be visible")
def step_verify_search_box(context):
    assert context.home.verify_search_box()


@then("the website logo should be visible")
def step_verify_logo(context):
    assert context.home.verify_logo()