import unittest
from productsapp.integration_test.factory.website_factory import WebsiteFactory
from productsapp.manager.website import WebsiteManager
from productsapp.main import Engine
engine = Engine()
session = engine.session_maker()


class TestWebsiteManager(unittest.TestCase):
    def test_create_website(self):
        wm = WebsiteManager(session)
        web_created = wm.create('test_website', 'www.test_url.com')
        self.assertEqual(web_created.website_name, "test_website")
    
    def test_update_name(self):
        wm = WebsiteManager(session)
        updated_web = wm.update_name('test_website', 'updated_test_website')

        self.assertEqual(updated_web.)
    # we are deleting thet test_case
    def test_delete_website(self):
        # we have to find that test_case exists. 


        
    
