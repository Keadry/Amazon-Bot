from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class productDetailPage():
    def __init__(self, driver):
        self.driver = driver
    
    def addToCart(self):
        add_to_cart_button = self.driver.find_element(By.ID, 'add-to-cart-button')
        add_to_cart_button.click()