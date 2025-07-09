from pathlib import Path

import data
from credentials_generator import generate_credentials
from locators.recipes_page_locators import RecipesPageLocators
from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.reg_page import RegPage


class RecipesPage(BasePage):
    def create_account_and_auth(self,driver):
        main_page = MainPage(driver)
        main_page.get_url_page(f'{data.BASE_URL}')
        main_page.click_to_create_account()

        creds = generate_credentials()
        email = creds['email']
        password = creds['password']

        reg_page = RegPage(driver)
        reg_page.fill_registration_form(**creds)
        reg_page.click_to_create_account()
        reg_page.wait_for_url_to_be(f'{data.BASE_URL}{data.AUTH_URL}')

        auth_page = AuthPage(driver)
        auth_page.fill_auth_form(email, password)
        auth_page.click_to_auth_button()

    def click_create_recipe_tab(self):
        self.wait_for_element_to_be_clickable(RecipesPageLocators.CREATE_RECIPE_TAB)
        self.click_to_element(RecipesPageLocators.CREATE_RECIPE_TAB)

    def set_recipe_name(self, name):
        self.add_text_to_element(RecipesPageLocators.RECIPE_NAME_INPUT, name)

    def set_ingredient(self):
        self.add_text_to_element(RecipesPageLocators.INGREDIENT_NAME_INPUT, 'а')
        self.click_to_element(RecipesPageLocators.APRICOT_JAM_ITEM)
        self.add_text_to_element(RecipesPageLocators.INGREDIENT_AMOUNT_INPUT, '1')
        self.click_to_element(RecipesPageLocators.ADD_INGREDIENT_BUTTON)

    def set_cooking_time(self, time):
        self.add_text_to_element(RecipesPageLocators.COOKING_TIME_INPUT, time)

    def set_description(self, description):
        self.add_text_to_element(RecipesPageLocators.DESCRIPTION_INPUT, description)

    def upload_apricot_jam(self):
        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "assets" / "apricot_jam.png"
        file_input = self.driver.find_element(*RecipesPageLocators.IMAGE_UPLOAD_INPUT)
        file_input.send_keys(str(file_path))

    def fill_and_create_recipe(self, name, time, description):
        self.add_text_to_element(RecipesPageLocators.RECIPE_NAME_INPUT, name)

        self.add_text_to_element(RecipesPageLocators.INGREDIENT_NAME_INPUT, 'а')
        self.click_to_element(RecipesPageLocators.APRICOT_JAM_ITEM)
        self.add_text_to_element(RecipesPageLocators.INGREDIENT_AMOUNT_INPUT, '1')
        self.click_to_element(RecipesPageLocators.ADD_INGREDIENT_BUTTON)

        self.add_text_to_element(RecipesPageLocators.COOKING_TIME_INPUT, time)

        self.add_text_to_element(RecipesPageLocators.DESCRIPTION_INPUT, description)

        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "assets" / "apricot_jam.png"
        file_input = self.driver.find_element(*RecipesPageLocators.IMAGE_UPLOAD_INPUT)
        file_input.send_keys(str(file_path))

        self.click_to_element(RecipesPageLocators.CREATE_RECIPE_BUTTON)

    def click_create_recipe(self):
        self.click_to_element(RecipesPageLocators.CREATE_RECIPE_BUTTON)