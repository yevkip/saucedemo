from behave import *


@given(u'{user} is logged in')
def step_impl(context, user):
    context.app.login(user)


@given(u'Logged in {user} is on Products page')
def step_impl(context, user):
    context.app.open_base_page()
    context.app.login(user)
    context.app.products_page.is_active()


@given(u'Logged in {user} is on Cart page. Cart Empty')
def step_impl(context, user):
    context.app.open_base_page()
    context.app.login(user)
    context.app.products_page.is_active()
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.is_active()
    expected_items = {}
    context.app.cart_page.verify_cart_items(expected_items=expected_items)


@given(u'User proceed to Checkout page with {qty} product(s) in cart')
def step_impl(context, qty):
    context.app.products_page.add_product(num=qty)
    context.app.products_page.update_cart()
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.proceed_to_checkout()


@given(u'User is on Cart page')
def step_impl(context):
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.is_active()


@given(u'Cart contains {qty} product(s)')
def step_impl(context, qty):
    context.app.products_page.add_product(num=qty)
    context.app.products_page.update_cart()


@given(u'{state} btn is displayed for product')
def step_impl(context, state):
    pass


@when(u'{user} is logged in')
def step_impl(context, user):
    context.app.login(user)


@when(u'User adds {qty} product to cart')
def step_impl(context, qty):
    context.app.products_page.add_product(num=qty)
    context.app.products_page.update_cart()


@when(u'{user} navigates to cart')
def step_impl(context, user):
    context.app.products_page.navigate_to_cart()


@when(u'User clicks on {state} btn')
def step_impl(context, state):
    pass


@when(u'User clicks on Remove btn for {qty} added product(s)')
def step_impl(context, qty):
    context.app.products_page.remove_product(num=qty)
    context.app.products_page.update_cart()


@when(u'In cart User clicks on Remove btn for {qty} added product(s)')
def step_impl(context, qty):
    removed_products = context.app.cart_page.remove_product(qty)
    context.app.products_page.update_cart(force_update=removed_products)


@then(u'Products in cart are displayed with "Remove" btn')
def step_impl(context):
    pass


@then(u'Cart badge shows {qty} product(s) in cart')
def step_impl(context, qty):
    context.app.products_page.verify_cart_badge_qty(num=qty)


@then(u'Btn changes state to {state}')
def step_impl(context, state):
    pass


@then(u'All products except affected one are displayed with "{state}" btn')
def step_impl(context, state):
    pass


@then(u'Cart contains {qty} product(s)')
def step_impl(context, qty):
    expected_items = context.app.products_page.products_in_cart
    assert int(qty) == len(expected_items), f"Expected qty: {qty}, Expected_items {len(expected_items)}"
    context.app.cart_page.verify_cart_items(expected_items=expected_items)


@then(u'Cart is empty')
def step_impl(context):
    expected_items = {}
    context.app.cart_page.verify_cart_items(expected_items=expected_items)