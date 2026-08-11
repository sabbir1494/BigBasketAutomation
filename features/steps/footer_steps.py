from behave import when, then

from pages.footer_page import FooterPage


@when("the user scrolls to the footer")
def step_scroll_to_footer(context):
    context.footer = FooterPage(context.driver)
    context.footer.scroll_to_footer()


@then("the footer should be displayed")
def step_verify_footer(context):
    assert context.footer.verify_footer()


@then("the footer links should be displayed")
def step_verify_footer_links(context):
    assert context.footer.verify_footer_links()


@when("the user opens the About Us page")
def step_open_about_us(context):
    context.footer.open_about_us()


@then("the About Us page should open successfully")
def step_verify_about_page(context):
    assert "about-us" in context.driver.current_url.lower()


@when("the user opens the Contact Us page")
def step_open_contact_us(context):
    context.footer.open_contact_us()


@then("the Contact Us page should open successfully")
def step_verify_contact_page(context):
    assert "contact-us" in context.driver.current_url.lower()