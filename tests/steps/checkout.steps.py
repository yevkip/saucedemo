from behave import *


@given(u'User complete checkout info and proceed to Checkout Overview page')
def step_impl(context):
    context.app.checkout_page.complete_checkout_info_and_submit()


@when(u'User complete checkout info and proceed to Checkout Overview page')
def step_impl(context):
    context.app.checkout_page.complete_checkout_info_and_submit()


@when(u'User proceeds to checkout')
def step_impl(context):
    context.app.cart_page.proceed_to_checkout()


@when(u'User clicks on "Finish" btn')
def step_impl(context):
    context.app.checkout_overview_page.finish_checkout()


@then(u'"Cart is empty" error is displayed')
def step_impl(context):
    context.app.cart_page.verify_empty_cart_error()


@then(u'Checkout Overview page contains {qty} product(s) with expected prices')
def step_impl(context, qty):
    expected_items = context.app.products_page.products_in_cart
    context.app.checkout_overview_page.verify_checkout_overview_inventory_items(expected_items)


@then(u'Price Total has expected calculation')
def step_impl(context):
    items_total_price = context.app.checkout_overview_page.items_total_price
    context.app.checkout_overview_page.verify_checkout_overview_total_price(items_total_price)


@then(u'Checkout complete message is displayed')
def step_impl(context):
    context.app.checkout_complete_page.verify_checkout_complete()