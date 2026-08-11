from behave import given, when, then


@when("the user opens the cart")
def step_open_cart(context):
    context.cart.open_cart()


@then("the cart should contain the product")
def step_verify_cart_product(context):

    # Product add করার পরে Cart page open করা
    context.cart.open_cart()

    assert context.cart.verify_cart_product()


@when("the user removes the product")
def step_remove_product(context):
    context.cart.remove_product()


@then("the cart should be empty")
def step_verify_empty_cart(context):
    assert context.cart.verify_empty_cart()