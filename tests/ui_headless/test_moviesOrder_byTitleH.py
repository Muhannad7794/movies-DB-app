import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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


def test_movie_ordering(driver):
    # Navigate to the Movies window
    driver.get("http://localhost:3307/")  # Replace with your application's URL

    # Function to select an order from the dropdown and return movie titles
    def get_movie_titles(order_value):
        try:
            order_select = driver.find_element(By.ID, "order")
            order_select.click()
            driver.find_element(
                By.CSS_SELECTOR, f"option[value='{order_value}']"
            ).click()

            # Wait for the page to update with sorted movies
            WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.CLASS_NAME, "movie-item"))
            )

            # Fetch titles of the movies listed
            movie_items = driver.find_elements(By.CLASS_NAME, "movie-item")
            return [movie.find_element(By.TAG_NAME, "h3").text for movie in movie_items]
        except NoSuchElementException:
            pytest.fail(f"Failed to find element, check if the UI has changed")

    # Verify ordering by Title
    titles_sorted_by_title = get_movie_titles("title")
    assert titles_sorted_by_title == sorted(
        titles_sorted_by_title
    ), "Movies are not sorted by title correctly"
