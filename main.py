from domain.selenium_config import SeleniumConfig
from use_case.login_site import LoginSelenium
from use_case.extractor import Extractor

def main():
    #Construtor
    selenium_config = SeleniumConfig(False,"")
    #Metodo do selenium_config
    driver = selenium_config.start()  
    #Construtor
    login = LoginSelenium(driver = driver, login = 'test_user', password='secure_password')
    extrator = Extractor(driver = driver)

    driver.get("http://quotes.toscrape.com/login")
    login.login_site()
    #extrator.extractor_site()

    #driver.quit()

    return extrator.extractor_site()

if __name__ == "__main__":
    main()
