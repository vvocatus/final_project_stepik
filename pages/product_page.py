from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def go_to_product_page(self):
		add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_to_basket.click()
		self.solve_quiz_and_get_code()
	def should_be_notification_and_price(self):
		notification_message = self.is_element_present(*ProductPageLocators.NOTFICATION_MESSAGE)
		assert notification_message, "No notification message"
		assert ProductPageLocators.PRODUCT_NAME == notification_message, "Wrong product name"
		assert ProductPageLocators.PRODUCT_PRICE == ProductPageLocators.BASKET_PRICE, "Wrong amount"