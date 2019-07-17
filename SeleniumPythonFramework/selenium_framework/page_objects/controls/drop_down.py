from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class DropDown:
    def __init__(self, options_element : WebElement, webdriver : webdriver ):
        self.__options_element = options_element
        self.__webdriver = webdriver

    def change_drop_down_value(self, byText):
        select_element = Select(self.__options_element)
        select_element.select_by_value(byText)


