from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	SIGN_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
	NOTIFICATION_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
	BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
	ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")
	PRODUCT_PAGE = (By.CSS_SELECTOR, "li:nth-child(1) article h3 a")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class BasketPageLocators():
	NOTIFICATION_ABOUT_NO_PRODUCTS = (By.CSS_SELECTOR, "#content_inner")
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs span a")



