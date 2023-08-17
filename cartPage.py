import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class cartPage():
    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal span.a-truncate-cut")
    
    def checkProductAdded(self):
        return len(self.getProducts()) > 0