from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def set_email(self, email):
        self.wait_for_element_to_be_clickable(AuthPageLocators.EMAIL_INPUT)
        self.add_text_to_element(AuthPageLocators.EMAIL_INPUT, email)

    def set_password(self, password):
        self.wait_for_element_to_be_clickable(AuthPageLocators.PASSWORD_INPUT)
        self.add_text_to_element(AuthPageLocators.PASSWORD_INPUT, password)

    def fill_auth_form(self, email, password):
        self.wait_for_element_to_be_clickable(AuthPageLocators.EMAIL_INPUT)
        self.wait_for_element_to_be_clickable(AuthPageLocators.PASSWORD_INPUT)
        self.set_email(email)
        self.set_password(password)

    def click_to_auth_button(self):
        self.click_to_element(AuthPageLocators.LOGIN_BUTTON)