from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM, RegistrationNoAccountModal as RNAM

class TestUserRegistration:
    # Тест: Регистрация пользователя
    def test_user_registration_open_main_page(self, driver, website, random_email, password, find):
        driver.get(website)                      # Открываем сайт
        driver.maximize_window()                 # Браузер на полный экран

        # Явное ожидание загрузки кнопки «Вход и регистрация»
        wait(driver, 3).until(EC.visibility_of_element_located(MW.login_registration_button))

        find(*MW.login_registration_button).click() # Нажать кнопку «Вход и регистрация»
        find(*LRM.no_account_button).click()        # Нажать кнопку «Нет аккаунта»

        # Явное ожидание появления полей с email, password, submit password:
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.enter_email_field))
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.enter_password_field))
        wait(driver, 2).until(EC.visibility_of_element_located(RNAM.enter_submit_password_field))

        find(*RNAM.enter_email_field).send_keys(random_email)               # Вводим случайный сгенерированный email
        find(*RNAM.enter_password_field).send_keys(password)                # Вводим пароль
        find(*RNAM.enter_submit_password_field).send_keys(password)         # Повторно вводим пароль
        find(*RNAM.create_account_button).click()                           # Кликаем на кнопку «Создать аккаунт»

        # Явное ожидание появления блока с аватаром:
        wait(driver, 3).until(EC.visibility_of_element_located(MW.avatar_img))

        assert driver.current_url == website # Проверка: произошёл переход на главную страницу
        assert find(*MW.avatar_img).get_attribute("class") == "circleSmall" # Проверка: отображается аватар в правом верхнем углу меню
        assert find(*MW.user_name).text == "User." # Проверка: отображается имя User.
