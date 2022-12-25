from selenium.webdriver.common.by import By


class Order:
    # Локатор полей ввода заказа
    order_input = [By.CLASS_NAME, 'Input_Input__1iN_Z']
    # Локатор поля выбора метро
    order_metro = [By.CLASS_NAME, 'select-search__input']
    # Локатор станций метро в селекторе
    select_metro = [By.CLASS_NAME, 'select-search__select']
    # Локатор кнопки открытия dropdown'а срока аренды
    rental_period_dropdown = [By.CLASS_NAME, 'Dropdown-arrow']
    # Локатор позиций в dropdown срока аренды
    rental_period_dropdown_menu = [By.CLASS_NAME, 'Dropdown-option']
    # Локатор чекбоксов выбора цвета самоката
    color_checkbox = [By.CLASS_NAME, 'Checkbox_Label__3wxSf']
    # Локатор логотипа Самокат
    logo_samokat = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    # Локатор логотипа Яндекс
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    # Локатор контента на странице Яндекса
    content_yandex = [By.CLASS_NAME, 'desktop-layout__content-1S']
