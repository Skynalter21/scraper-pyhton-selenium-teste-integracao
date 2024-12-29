from selenium.webdriver.common.by import By
import time

class LoginSelenium:
    def __init__(self, driver, login, password):
        self.driver = driver
        self.login = login
        self.password = password
    
    def login_site(self):
        self.driver.find_element(By.ID, "username").send_keys(self.login)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Login"]').click()
        
        time.sleep(3)

        if self.driver.find_elements(By.CSS_SELECTOR, "p.error"):
            print("login error")
            exit()
        else:
            print("login success")
