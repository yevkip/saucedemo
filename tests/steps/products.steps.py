import random
from behave import *


@given(u'{user} is logged in')
def step_impl(context, user):
    context.app.login(user)


@given(u'Logged in {user} is on Products page')
def step_impl(context, user):
    context.app.open_base_page()
    context.app.login(user)
    context.app.products_page.is_active()


@given(u'User picks a product')
def step_impl(context):
    context.product = random.choice(context.app.products_page.inventory_items)


@given(u'User clicks on {state} btn')
def step_impl(context, state):
    context.product.action_btn.click()


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
    context.products_in_cart = context.app.products_page.add_product(num=qty)
    context.products_in_cart = context.app.base_page.store_product_values(context.products_in_cart)
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.proceed_to_checkout()


@given(u'User is on Cart page')
def step_impl(context):
    context.app.products_page.navigate_to_cart()
    context.app.cart_page.is_active()


@given(u'Cart contains {qty} product(s)')
def step_impl(context, qty):
    context.products_in_cart = context.app.products_page.add_product(num=qty)


@given(u'Btn state is {state}')
def step_impl(context, state):
    context.app.products_page.verify_btn_state(expected_state=state, product=context.product)


@when(u'{user} is logged in')
def step_impl(context, user):
    context.app.login(user)


@when(u'User adds {qty} product to cart')
def step_impl(context, qty):
    context.products_in_cart = context.app.products_page.add_product(num=qty)
    context.products_in_cart = context.app.base_page.store_product_values(context.products_in_cart)


@when(u'{user} navigates to cart')
def step_impl(context, user):
    context.app.products_page.navigate_to_cart()


@given(u'User clicks on {state} btn on Products page')
def step_impl(context, state):
    context.product.action_btn.click()


@when(u'User clicks on {state} btn on Products page')
def step_impl(context, state):
    context.product.action_btn.click()


@when(u'User clicks on Remove btn for {qty} added product(s)')
def step_impl(context, qty):
    context.products_in_cart = context.app.products_page.remove_product(num=qty)
    context.products_in_cart = context.app.base_page.store_product_values(context.products_in_cart)


@when(u'In cart User clicks on Remove btn for {qty} added product(s)')
def step_impl(context, qty):
    context.products_in_cart = context.app.cart_page.remove_product(qty)
    context.products_in_cart = context.app.base_page.store_product_values(context.products_in_cart)


@then(u'Btn state is {state}')
def step_impl(context, state):
    context.app.products_page.verify_btn_state(expected_state=state, product=context.product)


@then(u'Products in cart are displayed with "Remove" btn')
def step_impl(context):
    pass


@then(u'Cart badge shows {qty} product(s) in cart')
def step_impl(context, qty):
    context.app.products_page.verify_cart_badge_qty(num=qty)


@then(u'All products except affected one are displayed with "{state}" btn')
def step_impl(context, state):
    pass


@then(u'Cart contains {qty} product(s)')
def step_impl(context, qty):
    assert int(qty) == len(context.products_in_cart), f"Expected qty: {qty}, Actual qty {len(context.products_in_cart)}"
    context.products_in_cart = context.app.base_page.store_product_values(context.products_in_cart)
    context.app.cart_page.verify_cart_items(expected_items=context.products_in_cart)


@then(u'Cart is empty')
def step_impl(context):
    expected_items = {}
    context.app.cart_page.verify_cart_items(expected_items=expected_items)
