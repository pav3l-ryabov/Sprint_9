from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_to_create_account(self):
        self.click_to_element(BasePageLocators.CREATE_ACCOUNT)