from selenium.webdriver.common.by import By
from data.data_for_creating_authorized_user import name_ad

class MainWebsite: # Главное меню сайта
    login_registration_button = (By.XPATH, "//div[@class='header_shell__zlCGj']//button[text()='Вход и регистрация']") # Кнопка "Вход и регистрация"
    avatar_img = (By.CLASS_NAME, "circleSmall") # Аватарка
    user_name = (By.CSS_SELECTOR, ".profileText.name") # Имя юзера "User."
    logout_button = (By.XPATH, "//div[@class='columnSmall']//button[text()='Выйти']")  # Кнопка "Выйти" из профиля
    place_ad = (By.XPATH, "//button[text()='Разместить объявление']") # Кнопка "Разместить объявление"

class LoginRegistrationModal: # Модальное окно "Войти"
    no_account_button = (By.XPATH, "//div[@class='popUp_buttonRow__+W8JD']/button[text()='Нет аккаунта']") # Кнопка "Нет аккаунта"
    enter_login_email = (By.NAME, "email") # Поле "Введите Email"
    enter_login_password = (By.NAME, "password") # Поле "Пароль"
    enter_login_button = (By.XPATH, "//div[@class='popUp_buttonRow__+W8JD']/button[text()='Войти']")

class RegistrationNoAccountModal: # Модальное окно "Зарегистрироваться"
    enter_email_field = (By.NAME, "email") # Поле "Введите Email"
    enter_password_field = (By.NAME, "password") # Поле "Пароль"
    enter_submit_password_field = (By.NAME, "submitPassword") # Поле "Повторите пароль"
    create_account_button = (By.XPATH, "//div[@class='popUp_buttonRow__+W8JD']//button[text()='Создать аккаунт']") # Кнопка "Создать аккаунт"
    error_email_message = (By.XPATH, "//div[@class='popUp_inputColumn__RgD8n']//span[text()='Ошибка']") # Ошибка под полем "Введите Email"
    error_marked_red_field = (By.CSS_SELECTOR, ".input_inputError__fLUP9") # Выделенные красным поля при ошибке

class CreatingModalUnauthorized:    # Модальное окно "Чтобы разместить объявление, авторизуйтесь"
    creating_modal_unauthorized_text = (By.XPATH, "//div[@class='popUp_titleRow__M7tGg']/h1[text()='Чтобы разместить объявление, авторизуйтесь']") # Заголовок модального окно

class CreatingNewAd: # Экран "Новое объявление"
    enter_name = (By.NAME, "name") # Поле "Название"
    enter_product_description = (By.XPATH, "//textarea[@placeholder='Описание товара']") # Поле "Описание товара"
    enter_price = (By.XPATH, "//input[@placeholder='Стоимость']") # Поле "Стоимость"
    open_list_categories = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]") # Выпадающий список категорий
    select_category_technology =  (By.XPATH, "//span[text()='Технологии']") # Категория "Технологии"
    open_list_cities = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]") # Выпадающий список городов
    select_city_novosibirsk = (By.XPATH, "//span[text()='Новосибирск']") # Город "Новосибирск"
    select_condition_goods = (By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular__FbVbr')]") # Выбираем радиокнопку "Б/У"
    to_publish_button = (By.XPATH, "//button[text()='Опубликовать']") # Кнопка "Опубликовать"

class MyProfile: # Экран профиля
    my_ads = (By.XPATH, f"//h2[@class='h2' and text()='{name_ad}']") # Объявление
