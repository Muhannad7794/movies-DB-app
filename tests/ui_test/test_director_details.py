from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
)  # Import the exception
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_directors_details_search(driver):
    driver.get("http://localhost:3307/directors/")

    # Input a search term
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar")
    search_bar.clear()
    search_bar.send_keys("Martin Scorsese")

    # Click the search button
    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    search_button.click()

    # Wait for search results to load and stabilize
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".movie-item"))
    )

    # Retry logic for fetching elements
    retries = 3
    for _ in range(retries):
        try:
            director_cards = driver.find_elements(By.CSS_SELECTOR, ".movie-item h3")
            director_names = [card.text for card in director_cards]
            print("Director Names:", director_names)
            assert any("martin scorsese" in name.lower() for name in director_names)
            break
        except StaleElementReferenceException:
            if _ == retries - 1:
                raise

    # Click on the first director card
    director_cards[0].click()
    # Wait for the director details page to load
    director_details = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "movie-details"))
    )
    # assert the presence of the director details
    assert "Martin Scorsese" in director_details.text
    assert "1942" in director_details.text
    assert "The Departed" in director_details.text
    assert "BAFTA Award" in director_details.text
