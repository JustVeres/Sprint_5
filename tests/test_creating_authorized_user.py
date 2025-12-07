from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM, CreatingNewAd as CNA, MyProfile as MP, RegistrationNoAccountModal as RNAM
from data.data_for_creating_authorized_user import name_ad, product_description, price

class TestCreatingAuthorizedUser:
    # Тест: Создание объявления авторизованным пользователем
    def test_creating_authorized_user_is_creating(self, driver, website, password, find, random_email):
        driver.get(website)               # Открываем сайт
        driver.maximize_window()          # Браузер на полный экран

        # Явное ожидание загрузки кнопки «Вход и регистрация»:
        wait(driver, 3).until(EC.visibility_of_element_located(MW.login_registration_button))

        find(*MW.login_registration_button).click()                         # Нажать кнопку «Вход и регистрация»
        find(*LRM.no_account_button).click()                                # Нажать кнопку «Нет аккаунта»

        # Явное ожидание кликабельности поля для ввода email
        wait(driver, 3).until(EC.element_to_be_clickable(RNAM.enter_email_field))

        # --- Генерируем и создаём аккаунт ---
        find(*RNAM.enter_email_field).send_keys(random_email)               # Вводим случайный сгенерированный email
        find(*RNAM.enter_password_field).send_keys(password)                # Вводим пароль
        find(*RNAM.enter_submit_password_field).send_keys(password)         # Повторно вводим пароль
        find(*RNAM.create_account_button).click()                           # Кликаем на кнопку «Создать аккаунт»

        # Явное ожидание, проверяем что мы залогинены по наличию кнопки "Выйти"
        wait(driver, 3).until(EC.presence_of_element_located(MW.logout_button))

        # --- Размещаем объявление ---
        find(*MW.place_ad).click()                                          # Кликаем на "Разместить объявление"
        find(*CNA.enter_name).send_keys(name_ad)                            # Вводим товар в поле "Название"
        find(*CNA.enter_product_description).send_keys(product_description )# Добавляем текст в поле «Описание товара»
        find(*CNA.enter_price).send_keys(price)                             # Вводим цену в поле "Стоимость"
        find(*CNA.open_list_categories).click()                             # Открываем выпадающий список категорий
        find(*CNA.select_category_technology).click()                       # Выберем категорию "Технология"
        find(*CNA.open_list_cities).click()                                 # Открываем выпадающий список городов
        find(*CNA.select_city_novosibirsk).click()                          # Выбираем город Новосибирск
        find(*CNA.select_condition_goods).click()                           # Выбираем радиокнопку "Б/У"
        find(*CNA.to_publish_button).click()                                # Кликаем на кнопку "Опубликовать"

        # Явное ожидание того, что закрыт экран с размещением объявления, по признаку отсутствия кнопки "Опубликовать"
        wait(driver, 3).until(EC.invisibility_of_element_located(CNA.to_publish_button))

        find(*MW.avatar_img).click()                                        # Переходим в профиль юзера

        # Явное ожидание появления названия созданной карточки товара
        wait(driver, 3).until(EC.visibility_of_element_located(MP.my_ads))

        assert find(*MP.my_ads).text == name_ad # Проверка: в блоке «Мои объявления» отображается созданное объявление
        driver.quit()
