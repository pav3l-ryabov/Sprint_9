from locators.reg_page_locators import RegPageLocators
from pages.base_page import BasePage


class RegPage(BasePage):
    def set_first_name(self, name):
        self.add_text_to_element(RegPageLocators.FIRST_NAME_INPUT, name)

    def set_last_name(self, last_name):
        self.add_text_to_element(RegPageLocators.LAST_NAME_INPUT, last_name)

    def set_username(self, username):
        self.add_text_to_element(RegPageLocators.USERNAME_INPUT, username)

    def set_email(self, email):
        self.add_text_to_element(RegPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.add_text_to_element(RegPageLocators.PASSWORD_INPUT, password)

    def fill_registration_form(self, first_name, last_name, username, email, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)

    def click_to_create_account(self):
        self.click_to_element(RegPageLocators.CREATE_ACCOUNT_BUTTON)