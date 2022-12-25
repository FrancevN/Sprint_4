import allure
from pages import order_page


@allure.title('Проверка заказа через кнопку в шапке')
@allure.description('На странице ищем кнопку «Заказать» в шапке, кликаем на неё и проверяем успешность заказа')
def test_order_from_header_button_completed_order(driver):
    completed_text = order_page.click_header_and_order(driver)
    assert completed_text == 'Посмотреть статус'


@allure.title('Проверка заказа через кнопку внизу страницы')
@allure.description('На странице ищем кнопку «Заказать» внизу страницы, кликаем на неё и проверяем успешность заказа')
def test_order_from_middle_button_completed_order(driver):
    completed_text = order_page.click_middle_and_order(driver)
    assert completed_text == 'Посмотреть статус'


@allure.title('Проверка клика на логотип «Самоката», попадаем на главную страницу «Самоката»')
@allure.description('На странице ищем логотип «Самоката», '
                    'кликаем по нему и проверяем что url = https://qa-scooter.praktikum-services.ru/')
def test_click_logo_samokat_open_samokat(driver):
    order_page.click_logo_samokat(driver)
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'


@allure.title('Проверка клика на логотип «Яндекса», попадаем на главную страницу «Яндекса»')
@allure.description('На странице ищем логотип «Яндекса», '
                    'кликаем по нему и проверяем что url = https://dzen.ru/?yredirect=true')
def test_click_logo_yandex_open_yandex(driver):
    order_page.click_logo_yandex(driver)
    assert driver.current_url == 'https://dzen.ru/?yredirect=true'
