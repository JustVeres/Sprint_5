from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM

class TestUserLogout:
    # Тест: Logout пользователя
    def test_user_logout_open_main_page(self, driver, website, password, test_mail, find):
        driver.get(website)                                  # Открываем сайт
        driver.maximize_window()                             # Браузер на полный экран

        # Явное ожидание загрузки кнопки «Вход и регистрация»:
        wait(driver, 3).until(EC.element_to_be_clickable(MW.login_registration_button))

        find(*MW.login_registration_button).click()           # Нажать кнопку «Вход и регистрация»
        find(*LRM.enter_login_email).send_keys(test_mail)     # Вводим уже зарегистрированный email
        find(*LRM.enter_login_password).send_keys(password)   # Вводим пароль
        find(*LRM.enter_login_button).click()                 # Кликаем на кнопку "Войти"

        # Явное ожидание кнопки "Выйти"
        wait(driver, 3).until(EC.element_to_be_clickable(MW.logout_button))

        find(*MW.logout_button).click()                       # Кликаем на кнопку "Выйти"

        # Явное ожидание, что аватарки больше не видно
        wait(driver, 3).until(EC.invisibility_of_element_located(MW.avatar_img))

        avatar_not_found = driver.find_elements(*MW.avatar_img)
        assert len(avatar_not_found) == 0 # Проверка: аватар не отображается

        user_name_not_found = driver.find_elements(*MW.user_name)
        assert len(user_name_not_found) == 0 # Проверка: Имя "User." не отображается

        assert find(*MW.login_registration_button).text == 'Вход и регистрация' # Проверка: отображается кнопка «Вход и регистрация»
