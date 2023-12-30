import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_movies_sort_by_release_year(driver):
    driver.get("http://localhost:3307/")  # Replace with your application's URL

    # Set order by 'release_year'
    order_select = driver.find_element(By.ID, "order")
    order_select.click()
    driver.find_element(By.CSS_SELECTOR, "option[value='release_year']").click()

    previous_year = None
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

            # Extract release year from details page
            movie_details = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "movie-details-text"))
            )
            details_text = movie_details.text
            release_year = int(
                details_text.split("Release Year: ")[1].split("\n")[0]
            )  # Adjust parsing as per your UI

            if previous_year is not None and release_year < previous_year:
                pytest.fail(
                    f"Movies are not sorted correctly by release year. Year {release_year} came after {previous_year}"
                )

            previous_year = release_year
            driver.back()  # Navigate back to the movie list
            index += 1
        except NoSuchElementException:
            pytest.fail("Could not find expected element on the page.")

