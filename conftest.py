import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    with allure.step('Открываем браузер Firefox'):
        driver = webdriver.Firefox()
    with allure.step('Открываем страницу {https://qa-scooter.praktikum-services.ru/}'):
        driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    with allure.step('Закрываем браузер Firefox'):
        driver.quit()
