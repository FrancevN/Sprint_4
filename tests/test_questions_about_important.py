import allure
from pages import main_page


@allure.title('Проверка ответа на 1 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_1(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 1)
    assert ask_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 'Текст ответа не правильный'


@allure.title('Проверка ответа на 2 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_2(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 2)
    assert ask_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
                       'можете просто сделать несколько заказов — один за другим.', 'Текст ответа не правильный'


@allure.title('Проверка ответа на 3 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_3(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 3)
    assert ask_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт ' \
                       'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                       'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 'Текст ответа не правильный'


@allure.title('Проверка ответа на 4 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_4(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 4)
    assert ask_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 'Текст ответа не правильный'


@allure.title('Проверка ответа на 5 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_5(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 5)
    assert ask_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по ' \
                       'красивому номеру 1010.', 'Текст ответа не правильный'


@allure.title('Проверка ответа на 6 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_6(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 6)
    assert ask_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете ' \
                       'кататься без передышек и во сне. Зарядка не понадобится.', 'Текст ответа не правильный '


@allure.title('Проверка ответа на 7 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_7(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 7)
    assert ask_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все ' \
                       'же свои.', 'Текст ответа не правильный '


@allure.title('Проверка ответа на 8 вопрос')
@allure.description('На странице ищем вопрос, кликаем на него и проверяем текст ответа')
def test_questions_about_important_questions_8(driver):
    ask_text = main_page.questions_scroll_and_click(driver, 8)
    assert ask_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.', 'Текст ответа не правильный'
