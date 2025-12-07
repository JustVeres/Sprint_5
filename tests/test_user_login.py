from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainWebsite as MW, LoginRegistrationModal as LRM

class TestUserLogin:
    # Тест: Login пользователя
    def test_user_login_open_main_page(self, driver, website, password, test_mail, find):
        driver.get(website)               # Открываем сайт
        driver.maximize_window()          # Браузер на полный экран

        # Нужно явное ожидание загрузки кнопки «Вход и регистрация», без этого иногда может возникать ошибка:
        wait(driver, 3).until(EC.visibility_of_element_located(MW.login_registration_button))

        find(*MW.login_registration_button).click()           # Нажать кнопку «Вход и регистрация»
        find(*LRM.enter_login_email).send_keys(test_mail)     # Вводим уже зарегистрированный email
        find(*LRM.enter_login_password).send_keys(password)   # Вводим пароль

        # Явное ожидание для кнопки "Войти"
        wait(driver, 3).until(EC.visibility_of_element_located(LRM.enter_login_button))

        find(*LRM.enter_login_button).click()                 # Кликаем на кнопку "Войти"

        # Явное ожидание появления блока с аватаром:
        wait(driver, 3).until(EC.visibility_of_element_located(MW.avatar_img))

        assert driver.current_url == website # Проверка: произошёл переход на главную страницу
        assert find(*MW.avatar_img).get_attribute("class") == "circleSmall" # Проверка: отображается аватар в правом верхнем углу меню
        assert find(*MW.user_name).text == "User." # Проверка: отображается имя User.
        driver.quit()
