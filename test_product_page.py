from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):

        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        add_product = page.go_to_product_page()
        add_product.solve_quiz_and_get_code()
