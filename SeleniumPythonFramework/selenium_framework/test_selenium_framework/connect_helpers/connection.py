from selenium_framework.page_objects.generic_helpers.page_object_driver_options import PODriverOptions

class Connection(object):
    @classmethod
    def driver_options(cls):
        url = r"http:\\localhost\ProteinPredictorWebSite"
        Browser = "Chrome"
        Headless = "False"
        driver_options = PODriverOptions(url, Browser, Headless)
        return driver_options