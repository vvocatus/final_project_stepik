from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def go_to_product_page(self):
		add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_to_basket.click()
		self.solve_quiz_and_get_code()
	def should_be_notification_and_price(self):
		notification_message = self.browser.find_element(*ProductPageLocators.NOTIFICATION_MESSAGE)
		assert notification_message, "No notification message"
		return notification_message.text

	def return_book_name(self):
		book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		return book_name.text

	def return_book_price(self):
		book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		return book_price.text

	def should_be_thing_in_basket(self, book_name):
		alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
		assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(book_name,
																										  alert_book_name.text)

	def should_be_same_price(self, book_price):
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
		assert basket_price.text == book_price, "basket prise is {}, but book price is {}".format(basket_price.text,
																									  book_price)

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"

	def should_be_dissapeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"
