from locators.main_page_locators import QuestionsAboutImportant
from locators.order_page_locators import Order
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from util import wait_for_click_not_intercepted


@allure.step('Кликаем по кнопке "Заказать" в шапке, заполняем форму заказа, '
             'проверяем появление окна созданного заказа')
def click_header_and_order(driver):
    driver.find_element(*QuestionsAboutImportant.order_button).click()
    driver.find_elements(*Order.order_input)[1].send_keys('Петров')
    driver.find_elements(*Order.order_input)[2].send_keys('Илюша')
    driver.find_elements(*Order.order_input)[3].send_keys('Илюшин дом')
    driver.find_element(*Order.order_metro).click()
    driver.find_element(*Order.select_metro).click()
    driver.find_elements(*Order.order_input)[4].send_keys('33333333333')
    driver.find_elements(*QuestionsAboutImportant.order_button)[2].click()
    driver.find_elements(*Order.order_input)[1].send_keys('01.01.1990')
    driver.find_element(*Order.rental_period_dropdown).click()
    driver.find_elements(*Order.rental_period_dropdown_menu)[-1].click()
    driver.find_element(*Order.color_checkbox).click()
    driver.find_elements(*QuestionsAboutImportant.order_button)[3].click()
    driver.find_elements(*QuestionsAboutImportant.order_button)[5].click()
    completed_text = driver.find_elements(*QuestionsAboutImportant.order_button)[4].text
    return completed_text


@allure.step('Кликаем по кнопке "Заказать" внизу страницы, заполняем форму заказа, '
             'проверяем появление окна созданного заказа')
def click_middle_and_order(driver):
    element = driver.find_elements(*QuestionsAboutImportant.order_button)[2]
    driver.execute_script("arguments[0].scrollIntoView();", element)
    wait_for_click_not_intercepted(element)
    driver.find_elements(*QuestionsAboutImportant.order_button)[2].click()
    driver.find_elements(*Order.order_input)[1].send_keys('Баширов')
    driver.find_elements(*Order.order_input)[2].send_keys('Димитрий')
    driver.find_elements(*Order.order_input)[3].send_keys('Димкин дом')
    driver.find_element(*Order.order_metro).click()
    driver.find_element(*Order.select_metro).click()
    driver.find_elements(*Order.order_input)[4].send_keys('11111111111')
    driver.find_elements(*QuestionsAboutImportant.order_button)[2].click()
    driver.find_elements(*Order.order_input)[1].send_keys('31.12.2022')
    driver.find_element(*Order.rental_period_dropdown).click()
    driver.find_element(*Order.rental_period_dropdown_menu).click()
    driver.find_element(*Order.color_checkbox).click()
    driver.find_elements(*QuestionsAboutImportant.order_button)[3].click()
    driver.find_elements(*QuestionsAboutImportant.order_button)[5].click()
    completed_text = driver.find_elements(*QuestionsAboutImportant.order_button)[4].text
    return completed_text


@allure.step('Кликаем по логотипу "Самокат" в шапке')
def click_logo_samokat(driver):
    driver.find_element(*Order.logo_samokat).click()


@allure.step('Кликаем по логотипу "Яндекс" в шапке, переключаемся на новую вкладку, ждем загрузки страницы')
def click_logo_yandex(driver):
    driver.find_element(*Order.logo_yandex).click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Order.content_yandex))
