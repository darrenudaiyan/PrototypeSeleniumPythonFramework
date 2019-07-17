from selenium import webdriver

class BasePage:
    def __init__(self, webdriver : webdriver):
        self.webdriver = webdriver
        self.title_text = webdriver.Remote.find_element_by_id("Title").Text
        
    
    