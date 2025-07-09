from selenium.webdriver.common.by import By


class RecipesPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[text()='Создать рецепт']/parent::li")
    RECIPE_NAME_INPUT = (By.XPATH, "//input[@type='text' and contains(@class, 'styles_inputField__3eqTj')]")
    INGREDIENT_NAME_INPUT = (By.XPATH,
                        "//input[contains(@class, 'styles_inputField__3eqTj') and contains(@class, 'styles_ingredientsInput__1zzql')]")
    APRICOT_JAM_ITEM = (By.XPATH, "//div[text()='абрикосовое варенье']")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/following::input[1]")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField__1wfhC')]")
    IMAGE_UPLOAD_INPUT = (By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput__3HjP3')]")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH,
                               "//input[contains(@class, 'styles_inputField__3eqTj') and contains(@class, 'styles_ingredientsAmountValue__2matT')]")
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card__title__2QMPq')]")