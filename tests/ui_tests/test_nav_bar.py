from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_movies_navigation(driver):
    driver.get("http://localhost:3307")
    movies_link = driver.find_element(By.CSS_SELECTOR, "nav .nav-links a:first-child")
    movies_link.click()
    assert driver.find_element(By.CLASS_NAME, "movie-list")


def test_directors_navigation(driver):
    driver.get("http://localhost:3307")
    directors_link = driver.find_element(
        By.CSS_SELECTOR, "nav .nav-links a[href='/directors']"
    )
    directors_link.click()
    assert driver.find_element(By.CLASS_NAME, "directors-list")


def test_studios_navigation(driver):
    driver.get("http://localhost:3307")
    studios_link = driver.find_element(
        By.CSS_SELECTOR, "nav .nav-links a[href='/studios']"
    )
    studios_link.click()
    assert driver.find_element(By.CLASS_NAME, "studios-list")
