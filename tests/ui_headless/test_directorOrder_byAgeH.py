import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


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


def test_director_ordering_by_date_of_birth(driver):
    driver.get("http://localhost:3307/directors")

    # Set order by 'by_date_of_birth'
    order_select = driver.find_element(By.ID, "order")
    order_select.click()
    driver.find_element(
        By.CSS_SELECTOR, "option[value='director_date_of_birth']"
    ).click()

    previous_date = None
    index = 0

    while True:
        try:
            # Find items
            director_items = driver.find_elements(By.CLASS_NAME, "director-item")
            if index >= len(director_items):
                break  # Exit loop if no more directors to process

            # Select the next director item
            director_item = director_items[index]
            director_item.click()

            # Extract release year from details page
            director_details = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "director-details-text"))
            )
            details_text = director_details.text
            director_date_of_birth_str = details_text.split("Date of Birth: ")[1].split(
                "\n"
            )[0]
            director_date_of_birth = datetime.strptime(
                director_date_of_birth_str, "%Y-%m-%d"
            ).date()

            if previous_date is not None and director_date_of_birth > previous_date:
                pytest.fail(f"directors are not sorted correctly by birth date.")

            previous_date = director_date_of_birth
            driver.back()  # Navigate back to the directors list
            index += 1
        except NoSuchElementException:
            pytest.fail("Could not find expected element on the page.")
