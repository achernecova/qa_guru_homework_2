import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_selenium_web_site_selenium(driver):
    url = "https://www.selenium.dev/"
    driver.get(url)
    assert driver.title == "Selenium"
    assert driver.current_url == url


def test_selenium_web_site_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"
    assert driver.current_url == url


def test_open_page_github(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert driver.current_url == url


def test_search_selenium_in_google_page(driver):
    url = "https://www.google.com/"
    driver.get(url)

    search_field = driver.find_element(By.XPATH, "//*[@aria-label='Найти']")
    search_field.send_keys("selenium")
    search_field.send_keys(Keys.ENTER)

    time.sleep(10)
    result_field = driver.find_element(By.XPATH, "(//h3[text()='Selenium'])[1]")
    assert result_field.text == "Selenium"
