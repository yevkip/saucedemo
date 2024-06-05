from behave import *

from tests.lib.pages import page_map


@then('User is on {page_name} page')
def step_impl(context, page_name):
    _page_name = page_map.get(page_name)
    if _page_name is None:
        raise ValueError(f'There is no such page "{page_name}" in pages mapping: {page_map}.')

    page = getattr(context.app, _page_name)
    page.wait()
    page.is_active()


@when(u'{user} logged out')
def step_impl(context, user):
    context.app.base_page.open_menu()
    context.app.menu.logout()





