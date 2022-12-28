from locators.main_page_locators import QuestionsAboutImportant
import allure
from util import wait_for_click_not_intercepted


@allure.step('Скроллим и кликаем на вопрос')
def questions_scroll_and_click(driver, question_index=1):
    locator_question = getattr(QuestionsAboutImportant, f"questions_{question_index}")
    element = driver.find_element(*locator_question)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    wait_for_click_not_intercepted(element)
    locator_ask = getattr(QuestionsAboutImportant, f"ask_{question_index}")
    ask_text = driver.find_element(*locator_ask).text
    return ask_text
