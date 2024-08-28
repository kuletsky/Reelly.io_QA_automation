from behave import given, when, then


@when('Add test password {test_psw} to the input fields')
def add_test_password(context, test_psw):
    context.app.change_psw_page.add_test_password(test_psw)


@then('Verify the “Change password” button is available')
def verify_btn_psw_available(context):
    context.app.change_psw_page.verify_btn_psw_available()
