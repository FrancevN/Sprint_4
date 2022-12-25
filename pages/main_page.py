from locators.main_page_locators import QuestionsAboutImportant
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.step('Скроллим и кликаем на 1 вопрос')
def questions_1_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_1)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_1))
    driver.find_element(*QuestionsAboutImportant.questions_1).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_1).text
    return ask_text


@allure.step('Скроллим и кликаем на 2 вопрос')
def questions_2_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_2)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_2))
    driver.find_element(*QuestionsAboutImportant.questions_2).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_2).text
    return ask_text


@allure.step('Скроллим и кликаем на 3 вопрос')
def questions_3_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_3)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_3))
    driver.find_element(*QuestionsAboutImportant.questions_3).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_3).text
    return ask_text


@allure.step('Скроллим и кликаем на 4 вопрос')
def questions_4_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_4)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_4))
    driver.find_element(*QuestionsAboutImportant.questions_4).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_4).text
    return ask_text


@allure.step('Скроллим и кликаем на 5 вопрос')
def questions_5_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_5))
    driver.find_element(*QuestionsAboutImportant.questions_5).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_5).text
    return ask_text


@allure.step('Скроллим и кликаем на 6 вопрос')
def questions_6_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_6)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_6))
    driver.find_element(*QuestionsAboutImportant.questions_6).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_6).text
    return ask_text


@allure.step('Скроллим и кликаем на 7 вопрос')
def questions_7_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_7)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_7))
    driver.find_element(*QuestionsAboutImportant.questions_7).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_7).text
    return ask_text


@allure.step('Скроллим и кликаем на 8 вопрос')
def questions_8_scroll_and_click(driver):
    element = driver.find_element(*QuestionsAboutImportant.questions_8)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        QuestionsAboutImportant.questions_8))
    driver.find_element(*QuestionsAboutImportant.questions_8).click()
    ask_text = driver.find_element(*QuestionsAboutImportant.ask_8).text
    return ask_text
