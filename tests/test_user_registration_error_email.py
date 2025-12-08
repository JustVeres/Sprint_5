from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM, RegistrationNoAccountModal as RNAM

class TestUserRegistrationErrorEmail:
    # Тест: регистрация пользователя c email не по маске *******@*******.***
    def test_user_registration_error_field(self, driver, website, find):
        driver.get(website)               # Открываем сайт
        driver.maximize_window()          # Браузер на полный экран

        # Нужно явное ожидание загрузки кнопки «Вход и регистрация», без этого иногда может возникать ошибка:
        wait(driver, 3).until(EC.visibility_of_element_located(MW.login_registration_button))

        find(*MW.login_registration_button).click()    # Нажать кнопку «Вход и регистрация»
        find(*LRM.no_account_button).click() # Нажать кнопку «Нет аккаунта»

        # Явное ожидание появления поля с email:
        wait(driver, 3).until(EC.visibility_of_element_located(RNAM.enter_email_field))

        find(*RNAM.enter_email_field).send_keys("error@mail")  # Вводим некорректный email

        # Явное ожидание появления кнопки «Создать аккаунт»:
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.create_account_button))

        find(*RNAM.create_account_button).click()              # Кликаем на кнопку «Создать аккаунт»

        # Явное ожидание появления красного выделения полей:
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.error_marked_red_field))

        assert find(*RNAM.error_email_message).text == "Ошибка" # Проверка: отображение "Ошибка" под полем email
        assert len(driver.find_elements(*RNAM.error_marked_red_field)) == 3 # Проверка: отображается 3 красных выделения поля
