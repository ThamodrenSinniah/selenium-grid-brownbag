from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--lang=en')
    options.add_argument('--window-size=1920,1080')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
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
