from behave import given, when, then


@given('Website is loaded')
def step_impl_load_website(context):
    context.app.open_base_page()


@when(u'User enter {user} username to username field')
def step_impl(context, user):
    context.app.login_page.enter_username(username=user)


@when('User enter {password} password to password field')
def step_impl(context, password):
    context.app.login_page.enter_password(password=password)


@when('User click on "Login" btn')
def step_impl(context):
    context.app.login_page.click_login_btn()


@then('User see an error {error}')
def step_impl(context, error):
    context.app.login_page.check_error_msg(error)

