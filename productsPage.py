from selenium import webdriver
import random
from selenium.webdriver.common.by import By

class productsPage():
    def __init__(self, driver):
        self.driver = driver

    def isOnProductPage(self):
        return self.driver.find_element(By.ID,'p_n_free_shipping_eligible-title').is_displayed()

    def selectProduct(self):
        items = self.getAllProducts()
#        i = 0
#        for item in items:
#            i+=1
#            print('-'*25)
#            print(f'{i} | {item.text}')
#            print('-'*25)
        x = random.randint(0,len(items))
        items[x].click()

    def getAllProducts(self):
        return self.driver.find_elements(By.CSS_SELECTOR , 'span.a-size-base-plus')
    