# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture
# def driver():
#     driver_instance = webdriver.Chrome()
#     yield driver_instance
#     driver_instance.quit()

import os
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Создаёт Remote WebDriver для Selenoid.
    Читает URL из переменной окружения SELENIUM_REMOTE_URL (например, http://selenoid:4444/wd/hub).
    """
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://selenoid:4444/wd/hub")
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver_instance = webdriver.Remote(
        command_executor=selenium_url,
        desired_capabilities=capabilities
    )

    yield driver_instance
    driver_instance.quit()