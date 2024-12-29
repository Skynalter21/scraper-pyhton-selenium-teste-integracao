from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumConfig:
    def __init__(self, debug, path, **kwargs):
        self.debug = debug
        self.path = path

    def start(self):
        options = Options()
        options.add_experimental_option("detach", self.debug)
        options.add_experimental_option("prefs", {"download.default_directory": self.path})
        self.driver = webdriver.Chrome(options=options)

        return self.driver
