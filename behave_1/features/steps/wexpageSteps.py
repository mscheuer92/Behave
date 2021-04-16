from behave import given, when, then, step
from selenium import webdriver

@given('chrome browser is launched')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver")

@when('Wex homepage is loaded')
def openHomepage(context):
    context.driver.get("https://www.wexinc.com/")

@then('verify the title of the webpage')
def verifyTitle(context):
    title = context.driver.title
    if title == "Game-changing payment solutions for every business | WEX Inc.":
        print("title matches")   

@then('close browsers')
def closeBrowser(context):
    context.driver.close()
