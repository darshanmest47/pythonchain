import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    driver = None

    if browser_name == "chrome":

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        request.cls.driver = driver

        yield
        driver.quit()

    elif browser_name == "firefox":

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()

        request.cls.driver = driver
        yield
        driver.quit()
