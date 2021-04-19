from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@given('Chrome browser is launched')
def initializeWebdriver(context):
    context.driver = webdriver.Chrome(executable_path="/home/michelle/Desktop/Selenium/Drivers/chromedriver_linux64/chromedriver")

@when('Github is loaded')
def launchBrowser(context):
    context.driver.get("https://www.github.com")
    
@when('I click on Sign in')
def clickSignin(context):
    context.driver.find_element_by_link_text('Sign in').click()
    context.driver.implicitly_wait(20)

@then('I am taken to the login page')
def loginPage(context):
    context.driver.implicitly_wait(20)
    verify = context.driver.find_element_by_xpath("//div[@id='login']/div/h1").text
    assert verify == "Sign in to GitHub"

@then('I enter username "{user}" and password "{pwd}"')
def enterCredentials(context, user, pwd):
    context.driver.find_element_by_id("login_field").clear()
    context.driver.find_element_by_id("login_field").send_keys(user)
    context.driver.find_element_by_id("password").send_keys(pwd)

@then('Click the login button')
def clickLogin(context):
    context.driver.find_element_by_name("commit").click()
    context.driver.implicitly_wait(30)

@then('I am shown a message saying "Incorrect username or password"')
def verifyMessage(context):
    context.driver.implicitly_wait(20)
    verify = context.driver.find_element_by_xpath("//div[@id='js-flash-container']/div/div").text
    assert verify == "Incorrect username or password."
    if verify != "Incorrect username or password.":
        print("The text you're looking for is not present on this page.")
    context.driver.close()
  
  