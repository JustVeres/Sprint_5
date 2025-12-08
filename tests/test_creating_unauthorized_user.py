from locators import MainWebsite as MW, CreatingModalUnauthorized as CMU

class TestCreatingUnauthorizedUser:
    # Тест: Создание объявления неавторизованным пользователем
    def test_modal_creating_unauthorized_user_not_creating(self, driver, website, find):
        driver.get(website)               # Открываем сайт
        driver.maximize_window()          # Браузер на полный экран
        find(*MW.place_ad).click()        # Кликаем на "Разместить объявление"

        # Проверка: открыто модальное окно "Чтобы разместить объявление, авторизуйтесь":
        assert find(*CMU.creating_modal_unauthorized_text).text == "Чтобы разместить объявление, авторизуйтесь"
