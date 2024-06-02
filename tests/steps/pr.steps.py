from behave import *


@given(u'User is logged in')
def step_impl(context):
    context.app.login(username='standard_user', password='secret_sauce')


@given(u'User is on Products page')
def step_impl(context):
    context.app.products_page.is_active()


@given(u'User is on Cart page')
def step_impl(context):
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.is_active()

@when(u'User is on Cart page')
def step_impl(context):
    pass

@given(u'Cart contains added product')
def step_impl(context):
    pass


@given(u'Cart contains {qty} product(s)')
def step_impl(context, qty):
    context.app.products_page.add_product(num=qty)
    context.app.products_page.update_cart()


@given(u'{state} btn is displayed for product')
def step_impl(context, state):
    pass


@when(u'User adds {qty} product to cart')
def step_impl(context, qty):
    context.app.products_page.add_product(num=qty)
    context.app.products_page.update_cart()


@when(u'User navigates to cart')
def step_impl(context):
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
    context.app.products_page.update_cart(update_with=removed_products)


@when(u'User removes {qty} product(s)')
def step_impl(context, qty):
    pass


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
    context.app.cart_page.verify_cart_items(expected_items=expected_items)
