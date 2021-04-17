from behave import given, when, then, step
from selenium import webdriver



@given('Chrome browser is launched')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver")

@when('ODU homepage is loaded')
def openHomepage(context):
    context.driver.get("https://www.odu.edu/")


@when('Find Program is clicked')
def find_and_click(context):
    #context.driver.find_element_by_xpath("//body[@id='uni-home']/div[2]/section/div/ul/li[2]/a/span").click()
    #text = context.driver.find_element_by_partial_link_text('Program').is_present()
    #assert text is True
    #text.click()

@then('I validate that Computer Science & Math hyperlink is present')
def validatePresence(context):
    csmLink = context.driver.find_element_by_link_text("Computer Science & Math").is_present()
    assert csmLink is True

@then('I click on the hyper link')
def clickCSM(context):
    context.driver.find_element_by_link_text("Computer Science & Math").click()


@then('I search for Computer Science')
def searchCS(context):
    CS = context.driver.find_element_by_link_text("Computer Science").is_present()
    assert CS is True
    

@then('click on the hyperlink')
def step_impl(context):
    context.driver.find_element_by_link_text("Computer Science").click()


@then('I will be on the Computer Science Program Page')
def closeBrowser(context):
    context.browser.close()




