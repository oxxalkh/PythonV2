import pytest
import yaml
from module import Site
from Send_log import send_log_email
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture()
def browser():
    if testdata["browser"] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata["browser"] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
#
#
# @pytest.fixture()
# def selector_log():
#     return '//*[@id="login"]/div[1]/label/input'
#
#
# @pytest.fixture()
# def selector_pass():
#     return '//*[@id="login"]/div[2]/label/input'
#
#
# @pytest.fixture()
# def selector_button():
#     return '//*[@id="login"]/div[3]'
#
#
# @pytest.fixture()
# def selector_err():
#     return '//*[@id="app"]/main/div/div/div[2]/h2'
#
#
# @pytest.fixture()
# def res_authorisation():
#     return '//*[@id="app"]/main/nav/a'
#
#
#
# @pytest.fixture()
# def new_post():
#     return '//*[@id="create-btn"]'
#
#
# @pytest.fixture()
# def input_title():
#     return '//*[@id="create-item"]/div/div/div[1]/div/label/input'
#
#
# @pytest.fixture()
# def input_description():
#     return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def input_content():
#     return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def selector_button2():
#     return '//*[@id="create-item"]/div/div/div[7]/div/button'
#
#
# @pytest.fixture()
# def post_title():
#     return '//*[@id="app"]/main/div/div[1]/h1'
#
#
# @pytest.fixture()
# def post_content():
#     return '//*[@id="app"]/main/div/div[1]/div/div[3]'
#
#
# @pytest.fixture()
# def site():
#     my_site = Site(testdata["address"])
#     yield my_site
#     my_site.close()


@pytest.fixture()
def report():
    yield
    send_log_email()


@pytest.fixture()
def token():
    result = requests.post(url=testdata["url_api"],
                           data={"username": testdata["login"],
                                 "password": testdata["password"]})
    print(result)
    return result.json()["token"]




