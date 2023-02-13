from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
from .locators import ProductPageLocators
class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket.click()

    def should_be_notification_about_no_products(self):
        notification_no_products = self.browser.find_element(*BasketPageLocators.NOTIFICATION_ABOUT_NO_PRODUCTS)
        assert notification_no_products, "No notification"
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Success message is presented, but should not be"

    def user_go_to_product_page(self):
        product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        product_page.click()