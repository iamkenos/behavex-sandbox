from behave import given, when, then

@given('I have something')
def step_impl(context):
   print('given')

@when('I do something')
def step_impl(context):
   print('when')

@then('I expect something')
def step_impl(context):
   print('then')