from behave import given, when, then


@then('Verify the right page Verification opens')
def verify_verification(context):
    context.app.verification_page.verify_verification_page()


@then('Verify “upload image” and “Next step” buttons are available')
def verify_btns(context):
    context.app.verification_page.verify_btn()
