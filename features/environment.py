from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.desired_capabilities import CHROME_DESIRED_CAPS, FIREFOX_DESIRED_CAPS

@fixture
def browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--lang=en')
    options.add_argument('--window-size=1920,1080')
    context.driver = webdriver.Remote('http://localhost:4444', CHROME_DESIRED_CAPS, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(0.5)

    context.wait = WebDriverWait(context.driver, 60)


def before_scenario(context, scenario):
    print(f'Scenario Started: {scenario.name}')
    use_fixture(browser, context)


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        print(f'Scenario Failure: {scenario.name}')
    else:
        print(f'Scenario Passed and Quiting: {scenario.name}')
    context.driver.quit()
