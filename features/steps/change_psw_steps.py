from behave import given, when, then


@then('Add some test password to the input fields')
def add_test_password(context):
    context.app.