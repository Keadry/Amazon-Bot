from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self,driver):
        self.driver = driver

    def search(self,text):
        searchBox = self.driver.find_element(By.ID , 'twotabsearchtextbox')
        searchBox.send_keys(text)
        submitBtn = self.driver.find_element(By.ID , 'nav-search-submit-button')
        submitBtn.click()
        
    def acceptCookie(self):
        try:
            cookieSubmit = self.driver.find_element(By.ID , 'sp-cc-accept')
            cookieSubmit.click()
        except:
            pass

    def isProductCountUp(self):
        return int(self.getCartCount()) > 0

    def goToCart(self):
        self.driver.find_element(By.ID,'nav-cart-count-container').click()

    def getCartCount(self):
        count = self.driver.find_element(By.ID,'nav-cart-count').text
        return int(count)