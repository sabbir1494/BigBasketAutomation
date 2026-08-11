from behave import when, then

from pages.login_page import LoginPage


@when("the user opens the login page")
def step_open_login_page(context):
    context.login = LoginPage(context.driver)
    context.login.open_login()


@then("the email field should be displayed")
def step_verify_email(context):
    assert context.login.verify_email_field()


@then("the mobile field should be displayed")
def step_verify_mobile(context):
    assert context.login.verify_mobile_field()


@then("the password field should be displayed")
def step_verify_password(context):
    assert context.login.verify_password_field()


@when('the user enters email "{email}"')
def step_enter_email(context, email):
    context.login.enter_email(email)


@when('the user enters password "{password}"')
def step_enter_password(context, password):
    context.login.enter_password(password)


@when("the user clicks the login button")
def step_click_login(context):
    context.login.click_login()


@then("an error message should be displayed")
def step_verify_error(context):
    assert context.login.get_error_message() != ""