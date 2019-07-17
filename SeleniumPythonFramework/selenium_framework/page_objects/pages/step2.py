from selenium import webdriver
from selenium_framework.page_objects.pages.base_page import BasePage
from selenium_framework.page_objects.pages.step3 import Step3
from selenium_framework.page_objects.controls.drop_down import DropDown
from selenium_framework.page_objects.generic_helpers.page_object_driver import PODriver

class Step2(BasePage):
    def __init__(self):
        super.__init__(self)
        self.__webdriver = self.webdriver
        self.page_name = "/step2.html"
        self.link_step3 = self.webdriver.Remote.find_element_by_id("LinkStep3")
        self.link_step3_text = self.link_step3.Text
        self.ml_options = self.webdriver.Remote.find_element_by_id("MLOptions")
        self.selected_protein_text = self.webdriver.Remote.find_element_by_id("SelectedProtein").Text
        PODriver.goto_url(self.webdriver, self.page_name)
        self.dropdown = DropDown(self.ml_options, self.__webdriver)
    
    def click_link_step2(self):
        self.link_step3.Click()
        return Step3()
    
    def select_dropdown_by_text(self, byText):
        self.dropdown.change_drop_down_value(byText)
        return self