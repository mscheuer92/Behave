from behave import given, when, then, step
from selenium import webdriver


@given('Chrome browser is launched')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver")

@when('ODU homepage is loaded')
def openHomepage(context):
    context.driver.get("https://www.odu.edu/")


@when('Find Program is clicked')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Find Program is clicked')


@then('I validate that Computer Science & Math hyperlink is present')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I validate that Computer Science & Math hyperlink is present')


@then('I click on the hyper link')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on the hyper link')


@then('I search for Computer Science')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I search for Computer Science')


@then('click on the hyperlink')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click on the hyperlink')


@then('I will be on the Computer Science Program Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will be on the Computer Science Program Page')