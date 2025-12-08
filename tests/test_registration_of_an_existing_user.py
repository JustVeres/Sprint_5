from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM, RegistrationNoAccountModal as RNAM

class TestRegistrationOfAnExistingUser:
    # Тест: Регистрация уже существующего пользователя
    def test_user_registration_already_existing_user_error_field(self, driver, website, password, test_mail, find):
        driver.get(website)               # Открываем сайт
        driver.maximize_window()          # Браузер на полный экран

        # Явное ожидание загрузки кнопки «Вход и регистрация»
        wait(driver, 3).until(EC.visibility_of_element_located(MW.login_registration_button))

        find(*MW.login_registration_button).click()                         # Нажать кнопку «Вход и регистрация»
        find(*LRM.no_account_button).click()                                # Нажать кнопку «Нет аккаунта»

        # Явное ожидание появления поля с email:
        wait(driver, 3).until(EC.visibility_of_element_located(RNAM.enter_email_field))

        find(*RNAM.enter_email_field).send_keys(test_mail)                  # Вводим уже зарегистрированный email
        find(*RNAM.enter_password_field).send_keys(password)                # Вводим пароль
        find(*RNAM.enter_submit_password_field).send_keys(password)         # Повторно вводим пароль
        find(*RNAM.create_account_button).click()                           # Кликаем на кнопку «Создать аккаунт»

        # Явное ожидание появления красного выделения полей:
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.error_marked_red_field))

        assert find(*RNAM.error_email_message).text == "Ошибка" # Проверка: отображение "Ошибка" под полем email
        assert len(driver.find_elements(*RNAM.error_marked_red_field)) == 3 # Проверка: отображается 3 красных выделения поля
