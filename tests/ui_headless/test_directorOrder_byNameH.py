import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_director_ordering_by_name(driver):
    # Navigate to the Movies window
    driver.get("http://localhost:3307/directors/")

    # Function to select an order from the dropdown
    def get_directors_names(order_value):
        try:
            order_select = driver.find_element(By.ID, "order")
            order_select.click()
            driver.find_element(
                By.CSS_SELECTOR, f"option[value='{order_value}']"
            ).click()

            # Wait for the page to update with sorted directors
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, "director-item"))
            )

            # Fetch titles of the directors listed
            director_items = driver.find_elements(By.CLASS_NAME, "director-item")
            return [
                director.find_element(By.TAG_NAME, "h3").text
                for director in director_items
            ]
        except NoSuchElementException:
            pytest.fail(f"Failed to find element, check if the UI has changed")

    # Verify ordering by name
    names_sorted_by_name = get_directors_names("director_name")
    assert names_sorted_by_name == sorted(
        names_sorted_by_name
    ), "directors are not sorted by name correctly"
