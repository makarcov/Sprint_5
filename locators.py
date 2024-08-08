from selenium.webdriver.common.by import By

class Locators:

    # главная страница
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/account']") # кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/']") # кнопка "Конструктор"
    ENTER_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # кнопка "Войти в аккаунт"
    LOGO_BUTTON = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/a[@href = '/']") # Логотип
    CONSTRUCTOR_TITLE = (By.XPATH, "//section/h1") # надпись "Соберите бургер"
    BUNS_BUTTON = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']/parent::div")  # кнопка "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//span[text() = 'Начинки']/parent::div")  # кнопка "Начинки"

    # страница входа
    ENTER_EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name = 'name']") # поле ввода "Email"
    ENTER_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name = 'Пароль']") # поле ввода "Пароль"
    ENTER_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # кнопка "Войти"
    ENTER_REGISTRATION_BUTTON = (By.XPATH, "//a[@class = 'Auth_link__1fOlj' and @href = '/register']")  # кнопка "Зарегистрироваться"
    ENTER_FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@class = 'Auth_link__1fOlj' and @href = '/forgot-password']")  # кнопка "Восстановить пароль"

    # страница восстановления пароля
    FORGOT_PASSWORD_ENTER_BUTTON = (By.XPATH, "//a[text() = 'Войти']")  # кнопка "Войти"

    # страница регистрации
    REG_LOGIN_INPUT_FIELD = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  # поле ввода "Имя"
    REG_EMAIL_INPUT_FIELD = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле ввода "Email"
    REG_PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name = 'Пароль']")  # поле ввода "Пароль"
    REG_REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    REG_ENTER_BUTTON = (By.XPATH, "//a[text() = 'Войти']")  # кнопка "Войти"
    REG_ERROR = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # надпись "Некорректный пароль"

    # главная страница при успешном входе
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка "Оформить заказ"

    # страница профиля
    PROFILE_TITLE = (By.XPATH, "//input[@name = 'Name']")
    SAVE_BUTTON = (By.XPATH, "//button[text() = 'Сохранить']")  # кнопка "Сохранить"
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # кнопка "Выход"


