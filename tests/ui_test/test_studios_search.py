from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_studios_search(driver):
    driver.get("http://localhost:3307/studios/")
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar")
    search_bar.clear()
    search_bar.send_keys("warner")
    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    search_button.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".studio-item"))
    )

    retries = 3
    for _ in range(retries):
        try:
            studio_cards = driver.find_elements(By.CSS_SELECTOR, ".studio-item h3")
            studio_names = [card.text for card in studio_cards]
            print("Studio Names:", studio_names)
            assert any("warner" in name.lower() for name in studio_names)
            break
        except StaleElementReferenceException:
            if _ == retries - 1:
                raise
