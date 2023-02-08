from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def go_to_product_page(self):
		add_to_basket = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET)
		add_to_basket.click() 
