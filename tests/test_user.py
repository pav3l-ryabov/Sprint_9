import allure

import data
from credentials_generator import generate_credentials
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.reg_page import RegPage
from locators.auth_page_locators import AuthPageLocators
from locators.recipes_page_locators import RecipesPageLocators


class TestUser:
    @allure.title('Тест создания аккаунта')
    def test_create_account(self, driver):
        main_page = MainPage(driver)
        main_page.get_url_page(f'{data.BASE_URL}')
        main_page.click_to_create_account()

        reg_page = RegPage(driver)
        reg_page.fill_registration_form(**generate_credentials())
        reg_page.click_to_create_account()

        assert reg_page.wait_for_url_to_be(
            f'{data.BASE_URL}{data.AUTH_URL}'), 'Переход на страницу авторизации не произошел'
        assert reg_page.find_element_with_wait(
            AuthPageLocators.LOGIN_TITLE), 'Заголовок "Войти на сайт" не отображается'

    @allure.title('Тест авторизации и открытия главной страницы')
    def test_auth(self, driver):
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

        assert reg_page.wait_for_url_to_be(
            f'{data.BASE_URL}{data.RECIPES_URL}'), 'Переход на главную страницу с рецептами не произошел'
        assert reg_page.find_element_with_wait(
            RecipesPageLocators.LOGOUT_BUTTON), 'Заголовок "Войти на сайт" не отображается'