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


def test_movies_sort_by_credits_score(driver):
    driver.get("http://localhost:3307/")

    # Set order by 'credits_score'
    order_select = driver.find_element(By.ID, "order")
    order_select.click()
    driver.find_element(By.CSS_SELECTOR, "option[value='credits_score']").click()

    previous_score = None
    index = 0

    while True:
        try:
            # Find movie items on the page
            movie_items = driver.find_elements(By.CLASS_NAME, "movie-item")
            if index >= len(movie_items):
                break  # Exit loop if no more movies to process

            # Select the next movie item
            movie_item = movie_items[index]
            movie_item.click()

            # Extract score from details page
            movie_details = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "movie-details-text"))
            )
            details_text = movie_details.text
            credits_score = float(
                details_text.split("IMDB Score: ")[1].split("\n")[0]
            )  # Adjust parsing as per your UI

            if previous_score is not None and credits_score < previous_score:
                pytest.fail(
                    f"Movies are not sorted correctly by credit score. score {credits_score} is lower than {previous_score}"
                )

            previous_score = credits_score
            driver.back()  # Navigate back to the movie list
            index += 1
        except NoSuchElementException:
            pytest.fail("Could not find expected element on the page.")
