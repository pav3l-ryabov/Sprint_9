import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    selenium_url = os.getenv("SELENIUM_REMOTE_URL", "http://selenoid:4444/wd/hub")

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver_instance = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )

    yield driver_instance
    driver_instance.quit()