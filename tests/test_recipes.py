import allure

import data
from pages.recipes_page import RecipesPage
from locators.recipes_page_locators import RecipesPageLocators


class TestRecipes:
    @allure.title('Тест создания рецепта')
    def test_create_recipe(self, driver):
        recipes_page = RecipesPage(driver)
        recipes_page.create_account_and_auth(driver)

        recipes_page.click_create_recipe_tab()
        recipe = data.RECIPE
        expected_recipe_name = recipe['name']
        recipes_page.fill_and_create_recipe(**data.RECIPE)
        actual_recipe_name = recipes_page.get_text_from_element(RecipesPageLocators.RECIPE_TITLE)

        assert recipes_page.find_element_with_wait(
            RecipesPageLocators.RECIPE_TITLE), 'Карточка рецепта не отобразилась'
        assert expected_recipe_name == actual_recipe_name,\
            f'Название рецепта не совпадает'