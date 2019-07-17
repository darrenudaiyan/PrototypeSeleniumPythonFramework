from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium_framework.page_objects.generic_helpers.page_object_driver_options import PODriverOptions
from pathlib import Path

class PODriver (object):
    base_url = ""

    @classmethod
    def goto_url(cls, webdriver : webdriver, page_name):
        webdriver.get(cls.base_url + page_name)
        webdriver.Remote.find_elements_by_id("Title")
        
    @classmethod
    def initialise_web_driver(cls, driverOptions : PODriverOptions):
        cls.base_url = driverOptions.url
        driver_path = Path(__file__).parent.parent + "\drivers"
        
        browser_type = driverOptions.browser
        web_driver = cls.get_browser_type(browser_type, driver_path)
        return web_driver
    
    @classmethod
    def get_browser_type(cls, browser_type, driver_path):
        switcher={
            'Chrome': webdriver.Chrome(driver_path),
            'Edge':webdriver.Edge(driver_path),
            'Firefox':webdriver.Firefox(driver_path),
        }
        return switcher.get(browser_type,webdriver.Chrome(driver_path))
    