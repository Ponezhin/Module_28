from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "/Chrome/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "/Firefox/geckodriver.exe"

    BASE_URL = "https://www.labirint.ru/"

    # HOME PAGE data for main menu testing - testing "Книги" button
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_BOOK_PAGE = "Книги"
    TITLE_OF_MAIN_YEAR_BOOK_PAGE = "Главные книги 2021"
    ALL_BOOKS_TITLE = "Книги"
    TEENS_BOOKS_TITLE = "Молодежная литература"
    PERIODICALS_TITLE = "Периодические издания"
    BILINGUAL_TITLE = "Билингвы"
    CHILD_BOOK_TITLE = "Детский досуг"
    MANGA_BOOK_TITLE = "Манга для детей"
    RELIGION_BOOK_TITLE = "Религии мира"

    # CURRENT Region setting
    CITY_TO_SET = "Санкт-Петербург"
    CURRENT_CITY = "Санкт-Петербург"

    # equal to "москва" in cyrillic
    CITY_TO_SET_IN_CYRILLIC = "Владивосток"
    FIRST_CITY_IN_AUTO_ADVICE = "Владивосток"

    CITY_TO_SET_WRONG_LANGUAGE = "Rfkbybyuhfl"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Калининград"

    # Data for PostponePage tests
    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Successful deletion of postponed books message
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Successful deletion of books from Basket
    YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"

    # Names of attributes
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Data for Search page
    AUTHOR_SEARCH = "Иван Тургенев"
    SEARCHED_BOOK_NAME = "Муму"
    SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN = "Uhfa Vjynt-Rhbcnj"  # "Граф Монте-Кристо"
    EXPECTED_RESULT_BOOK_NAME = "Граф Монте-Кристо"

    # Data for Search page filter
    MIN_PRICE = "500"
    MAX_PRICE = "600"

    """CROSS PAGE LOCATORS"""

    # locator for button to close popup which appear after any action ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """for BASKET"""
    # locator for Basket "Корзина" button at header
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main '
                                         'analytics-click-js cart-icon-js"]')
    # locator for Basket "Корзина" counter
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    """for Search"""
