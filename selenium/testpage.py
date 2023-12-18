from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open(r'./locators.yaml') as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    # for locator in locators["css"].keys():
    #     ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_btn(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f"Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_el(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            logging.error(f"Element {locator} not found")
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # enter text

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_LOGIN_FIELD"],
                                   word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_PASS_FIELD"],
                                   word, description="password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"],
                                   word, description="title form")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"],
                                   word, description="content form")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_DESCRIPTION"], word,
                                   description="description form")

    def enter_name_field(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_YOU_NAME_FIELD"], word,
                                   description="name form")

    def enter_email_field(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_YOU_EMAIL_FIELD"], word,
                                   description="email form")

    def enter_content_field(self, word):
        self.enter_text_into_field(TestSearchLocators.
                                   ids["LOCATOR_CONTENT_FIELD"], word,
                                   description="content field form")

    # get
    def get_err_text(self):
        return self.get_text_from_el(TestSearchLocators.
                                     ids["LOCATOR_ERROR_FIELD"],
                                     description="error lbl")

    def get_text(self):
        return self.get_text_from_el(TestSearchLocators.
                                     ids["LOCATOR_RES_LOGIN"],
                                     description="result login")

    def get_title(self):
        return self.get_text_from_el(TestSearchLocators.
                                     ids["LOCATOR_POST_TITLE"],
                                     description="post title")

    def get_content(self):
        return self.get_text_from_el(TestSearchLocators.
                                     ids["LOCATOR_POST_CONTENT"],
                                     description="post content")

    def text_alert(self):
        logging.info('Switch alert')
        text = self.switch_to_alert()
        logging.info(text)
        return text

    # click
    def click_contactus_send_button(self):
        self.click_btn(
            TestSearchLocators.ids["LOCATOR_CONTACT_US_SEND_BTN"],
            description="contactus send")

    def click_contactus_button(self):
        self.click_btn(
            TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"],
            description="contactus")

    def click_login_btn(self):
        self.click_btn(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"],
            description="login")

    def click_post_btn(self):
        self.click_btn(
            TestSearchLocators.ids["LOCATOR_POST_BTN"],
            description="post")

    def click_create_post_btn(self):
        self.click_btn(
            TestSearchLocators.ids["LOCATOR_CREATE_POST"],
            description="create post")




