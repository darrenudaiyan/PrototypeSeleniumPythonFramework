
from selenium import webdriver
from page_objects.pages.base_page import BasePage
from page_objects.pages.index_page import IndexPage
from page_objects.controls.drop_down import DropDown
from page_objects.generic_helpers.page_object_driver import PODriver
from page_objects.controls.protein_data_table import ProteinDataTable

class Step3(BasePage):
    def __init__(self):
        super.__init__(self)
        self.__webdriver = self.webdriver
        self.page_name = "/step3.html"
        self.link_step1 = self.webdriver.Remote.find_element_by_id("LinkStep1")
        self.link_step1_text = self.link_step1.Text
        self.ml_options = self.webdriver.Remote.find_element_by_id("MLOptions")
        self.selected_ml = self.webdriver.Remote.find_element_by_id("SelectedML").Text
        self.regenerate = self.webdriver.Remote.find_element_by_id("Regenerate")
        self.protein_sizer_data = self.webdriver.Remote.find_element_by_id("ProteinSizerData")
        PODriver.goto_url(self.webdriver, self.page_name)
        self.dropdown = DropDown(self.ml_options, self.__webdriver)
        self.protein_data_table = ProteinDataTable(self.protein_sizer_data)
    
    def click_link_step1(self):
        self.link_step1.Click()
        return IndexPage()
    
    def click_regenerate(self):
        self.regenerate.Click
        return  self
    
    def get_protein_data(self):
        return self.protein_data_table.get_table_contents
    
    def select_dropdown_by_text(self, byText):
        self.dropdown.change_drop_down_value(byText)
        return self