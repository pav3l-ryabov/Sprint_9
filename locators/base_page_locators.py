from selenium.webdriver.common.by import By


class BasePageLocators:
    CREATE_ACCOUNT = (By.XPATH, "//a[text()='Создать аккаунт']")