import unittest
import json
from homePage import HomePage
from cartPage import cartPage
from productsPage import productsPage  
from productDetailPage import productDetailPage  
import time
from selenium import webdriver

class TestAddProductToCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.amazon.com/')
        cls.driver.maximize_window()
        cls.home = HomePage(cls.driver)
        cls.product = productsPage(cls.driver)
        cls.productDetail = productDetailPage(cls.driver)
        cls.cart = cartPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def go_to_cart(self):
        self.home.goToCart()
        self.assertTrue(self.cart.checkProductAdded(),'Product did not added!')

    def add_product_to_cart(self):
        self.productDetail.addToCart()
        self.assertTrue(self.home.isProductCountUp(),'Product count did not increase!')

    def select_product(self):
        self.product.selectProduct()

    def search_product(self, product):
        self.home.search(product)
        self.home.acceptCookie()
        self.assertTrue(self.product.isOnProductPage(),'Not on products page!')

    @staticmethod
    def create_test_for_product(product):
        def test_product(self):
            self.search_product(product)
            self.select_product()
            self.add_product_to_cart()
            self.go_to_cart()
        return test_product

if __name__ == '__main__':
    with open('products.json', 'r', encoding='utf-8') as file:
        product_list = json.load(file)
    
    for product in product_list:
        test_name = 'test_' + product.replace(' ', '_').lower()
        test_func = TestAddProductToCart.create_test_for_product(product)
        setattr(TestAddProductToCart, test_name, test_func)
    
    unittest.main()
