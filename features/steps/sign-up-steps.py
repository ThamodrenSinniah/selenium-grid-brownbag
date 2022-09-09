from behave import When, Then
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@When('I am at VSM Login Page')
def go_to_login_page(context):
    context.driver.get('https://e2e.login.vistasoftmonitor.com/')
    context.wait.until(ec.presence_of_element_located((By.ID, "email")))


@Then('I see title is "{vsm_title}"')
def verify_title(context, vsm_title):
    assert_that(context.driver.title).is_equal_to(vsm_title)


@When('I click Password Forgotten')
def click_password_forgot(context):
    context.driver.find_element(By.XPATH, '//a[@data-cy="forgot_password_link"]').click()


@Then('I see Password Reset Page')
def password_reset_page_visible(context):
    context.wait.until(ec.presence_of_element_located((By.ID, 'reset_password_submit')))


@Then('I see Contact Number is "{contact_number}"')
def valid_contact_number(context, contact_number):
    element = context.driver.find_element(By.XPATH, './/a[contains(@href,"callto")]')
    context.wait.until(ec.visibility_of(element))
    assert_that(element.text).is_equal_to(contact_number)


@Then('I see Contact Email is "{contact_email}"')
def valid_contact_email(context, contact_email):
    element = context.driver.find_element(By.XPATH, './/a[contains(@href,"mailto")]')
    context.wait.until(ec.visibility_of(element))
    assert_that(element.text).is_equal_to(contact_email)
