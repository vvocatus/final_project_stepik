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

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
