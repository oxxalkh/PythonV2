from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.XPATH, '//*[@id="login"]/div[3]')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_RES_LOGIN = (By.XPATH, '//*[@id="app"]/main/nav/a')
    LOCATOR_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE = (By.XPATH,
                     '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESCRIPTION = \
        (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT = \
        (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_CREATE_POST = (By.XPATH,
                           '//*[@id="create-item"]/div/div/div[7]/div/button')
    LOCATOR_POST_TITLE = (By.XPATH,
                          '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_POST_CONTENT = (By.XPATH,
                            '//*[@id="app"]/main/div/div[1]/div/div[3]')
    LOCATOR_CONTACT_US_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_YOU_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_YOU_EMAIL_FIELD = (By.XPATH,
                               '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT_FIELD = (By.XPATH,
                             '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_US_SEND_BTN = (By.XPATH,
                                   '//*[@id="contact"]/div[4]/button/span')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element "
                     f"{TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(
            f"Send {word} to element "
            f"{TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_btn(self):
        logging.info("Click logging button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_err_text(self):
        err_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD,
                                      time=3)
        text = err_field.text
        logging.info(
            f"We find text {text} in error field "
            f"{TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_text(self):
        get_field = self.find_element(TestSearchLocators.LOCATOR_RES_LOGIN,
                                      time=3)
        text = get_field.text
        logging.info(
            f"We find text {text} in field "
            f"{TestSearchLocators.LOCATOR_RES_LOGIN[1]}")
        return text

    def click_post_btn(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to element "
                     f"{TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to element "
                     f"{TestSearchLocators.LOCATOR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to element "
                     f"{TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def click_create_post_btn(self):
        logging.info("Click create post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST).click()

    def get_title(self):
        get_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE,
                                      time=3)
        text = get_field.text
        logging.info(
            f"We find text {text} in field "
            f"{TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        return text

    def get_content(self):
        get_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT,
                                      time=3)
        text = get_field.text
        logging.info(
            f"We find text {text} in field "
            f"{TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        return text

    def click_contactus_button(self):
        logging.info('Click Contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def enter_name_field(self, word):
        logging.info(
            f'Send {word} to element {TestSearchLocators.LOCATOR_YOU_NAME_FIELD[1]}')
        name_field = self.find_element(
            TestSearchLocators.LOCATOR_YOU_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email_field(self, word):
        logging.info(
            f'Send {word} to element {TestSearchLocators.LOCATOR_YOU_EMAIL_FIELD[1]}')
        email_field = self.find_element(
            TestSearchLocators.LOCATOR_YOU_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content_field(self, word):
        logging.info(
            f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        content_field = self.find_element(
            TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_contactus_send_button(self):
        logging.info('Click Send button')
        self.find_element(
            TestSearchLocators.LOCATOR_CONTACT_US_SEND_BTN).click()

    def text_alert(self):
        logging.info('Switch alert')
        return self.switch_to_alert()



