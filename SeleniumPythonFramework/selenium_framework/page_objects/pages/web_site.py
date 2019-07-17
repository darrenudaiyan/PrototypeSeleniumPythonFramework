from page_objects.generic_helpers.page_object_driver_options import PODriverOptions
from page_objects.generic_helpers.page_object_driver import PODriver
import page_objects.generic_helpers.error_strings as error_strings
from page_objects.pages.index_page import IndexPage
from page_objects.pages.step2 import Step2
from page_objects.pages.step3 import Step3

class WebSite:
    def __init__(self, driverOptions : PODriverOptions ):
        self.__webDriver = PODriver.initialise_web_driver(driverOptions)
    
    @classmethod
    def index(self):
        return IndexPage()

    def step2(self):
        return Step2()
    
    def step3(self):
        return Step3()
    
    def goto_page(self, page_name):
        PODriver.goto_url(self.__webDriver, page_name)
    
    def quit(self):
        self.__webDriver.quit()

    def check_params(self, url):
        if not url.strip():
            raise ValueError(error_strings.URL_is_Null)
