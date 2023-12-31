import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Import the exception
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


def test_atudios_sort_by_founded_year(driver):
    driver.get("http://localhost:3307/studios/")

    # Set order by 'founded_year'
    order_select = driver.find_element(By.ID, "order")
    order_select.click()
    driver.find_element(By.CSS_SELECTOR, "option[value='founded']").click()

    previous_year = None
    index = 0

    while True:
        try:
            # Find movie items on the page
            studio_items = driver.find_elements(By.CLASS_NAME, "studio_-item")
            if index >= len(studio_items):
                break  # Exit loop if no more studios to process

            # Select the next studio item
            studio_item = studio_items[index]
            studio_item.click()

            # Extract founded year from details page
            studio_details = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "studio-details-text"))
            )
            details_text = studio_details.text
            founded_year = int(details_text.split("Founded: ")[1].split("\n")[0])

            if previous_year is not None and founded_year < previous_year:
                pytest.fail(f"studios are not sorted correctly by founded year.")

            previous_year = founded_year
            driver.back()  # Navigate back to the studios list
            index += 1
        except NoSuchElementException:
            pytest.fail("Could not find expected element on the page.")
