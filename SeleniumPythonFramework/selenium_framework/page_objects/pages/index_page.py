
from selenium import webdriver
from page_objects.pages.base_page import BasePage
from page_objects.pages.step2 import Step2
from page_objects.controls.drop_down import DropDown
from page_objects.generic_helpers.page_object_driver import PODriver

class IndexPage(BasePage):
    def __init__(self):
        super.__init__(self)
        self.__webdriver = self.webdriver
        self.page_name = "/index.html"
        self.link_step2 = self.webdriver.Remote.find_element_by_id("LinkStep2")
        self.link_step2_text = self.link_step2.Text
        self.protein_options = self.webdriver.Remote.find_element_by_id("ProteinOptions")
        self.selected_protein_text = self.webdriver.Remote.find_element_by_id("SelectedProtein").Text
        PODriver.goto_url(self.webdriver, self.page_name)
        self.dropdown = DropDown(self.protein_options, self.__webdriver)
    
    def click_link_step2(self):
        self.link_step2.Click()
        return Step2()
    
    def select_dropdown_by_text(self, byText):
        self.dropdown.change_drop_down_value(byText)
        return self