from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_movies_search(driver):
    driver.get("http://localhost:3307/")  # Navigate to the Movies page

    # Input a search term
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar")
    search_bar.clear()
    search_bar.send_keys("Inception")  # Example movie title

    # Click the search button
    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    search_button.click()

    # Wait for search results to load
    movie_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "movie-item"))
    )

    # Assert that the search results are displayed
    assert "Inception" in movie_card.text
