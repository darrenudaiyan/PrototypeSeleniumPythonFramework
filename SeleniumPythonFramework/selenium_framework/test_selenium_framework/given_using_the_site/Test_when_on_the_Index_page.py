
import pytest
from selenium_framework.page_objects.pages.web_site import WebSite
from connection import Connection
from selenium_framework.test_selenium_framework.connect_helpers.connection import Connection

class Test_when_on_the_index_page:
    def __init__(self):
        self.website = ""
    @pytest.fixture(scope="session")
    def setup(self,request):
        self.website =  WebSite(Connection.driver_options)

        def teardown():
            self.website().quit

        request.addfinalizer(teardown)
    
    def test_title_should_be_correct(self):
        assert self.website().index().title_text == "Udaiyan Protein Predictor - Wizard 1"