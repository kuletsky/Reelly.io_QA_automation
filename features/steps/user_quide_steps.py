from behave import given, when, then


@then('Verify all lesson videos contain titles')
def verify_user_guide_page_open(context):
    context.app.user_guide_page.verify_all_contain_titles()