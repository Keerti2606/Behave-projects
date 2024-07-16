import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def launch_chrome(context):
    # Path to your ChromeDriver executable
    chrome_driver_path = r"C:\Users\HP\PycharmProjects\behaveprojs\pythonProject\chromedriver.exe"

    # Create a Service object
    chrome_service = Service(executable_path=chrome_driver_path)

    # Initialize the WebDriver with the specified options and service
    context.driver = webdriver.Chrome(service=chrome_service)



@when(u'open login page')
def open_login(context):
    context.driver.get("https://practicetestautomation.com/practice-test-login/")


@then(u'verify logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH,"//img[@class='custom-logo']").is_displayed()
    assert status is True

@then(u'Enter username "{user}" and password "{password}"')
def verify_login(context,user,password):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME,"password").send_keys(password)

@then(u'verify login')
def verify_login(context):
    context.driver.find_element(By.ID,"submit").click()
    time.sleep(5)
    output_element = context.driver.find_element(By.XPATH,"//strong[text()='Congratulations student. You successfully logged in!']")
    assert output_element.text == "Congratulations student. You successfully logged in!", \
        f"Expected success message not found. Actual message: {output_element.text}"
    time.sleep(10)
    context.driver.close()

@then(u'Navigate to practice page')
def nav_practice(context):
    practicepage = context.driver.find_element(By.XPATH,'//a[text()="Practice"]').click()

@then(u'Navigate to home page')
def nav_home(context):
    context.driver.find_element(By.XPATH, '//a[text()="Home"]').click()


