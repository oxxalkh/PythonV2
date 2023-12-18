import time
import yaml
from testpage import OperationsHelper
import logging
from testAPI import APIHelper


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_btn()
    assert testpage.get_err_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_btn()
    assert testpage.get_text() == "Home"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser, testdata["url"])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_btn()
    testpage.click_post_btn()
    testpage.enter_title(testdata["title"])
    testpage.enter_content(testdata["content"])
    testpage.enter_description(testdata["description"])
    testpage.click_create_post_btn()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_title() == testdata["title"]
    assert testpage.get_content() == testdata["content"]


def test_step4(browser):
    logging.info('Test 4 start')
    testpage = OperationsHelper(browser, testdata['url'])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_btn()
    testpage.click_contactus_button()
    testpage.enter_name_field(testdata["name"])
    testpage.enter_email_field(testdata["email"])
    testpage.enter_content_field(testdata["content_ann"])
    testpage.click_contactus_send_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.text_alert() == 'Form successfully submitted'


def test_api_step5(token):
    logging.info('Test 5 start')
    test_api = APIHelper()
    result = test_api.get_my_post(token)
    description_list = test_api.check_description(result)
    assert testdata['description'] in description_list
    assert result.status_code == 200


def test_api_step6(token):
    logging.info('Test 6 start')
    test_api = APIHelper()
    result = test_api.get_not_my_posts(token)
    title_list = test_api.check_title(result)
    assert (testdata['not_my_title'] in title_list and testdata['title']
            not in title_list)
    assert result.status_code == 200


def test_api_step7(token, report):
    logging.info('Test 7 start')
    test_api = APIHelper()
    result = test_api.get_my_post(token)
    title_list = test_api.check_title(result)
    assert testdata['title'] in title_list
    assert result.status_code == 200


