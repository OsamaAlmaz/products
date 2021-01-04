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

    def test_delete_website(self):
        # we have to find that test_case exists. 
        wm = WebsiteManager(session)
        website = wm.get_name('test_website')
        deleted_website = wm.delete(website.website_name)
        updated_website = wm.get(website.website_name)
        self.assertIsNone(updated_website)
    
    def test_update_name(self):
        wm = WebsiteManager(session)
        web_created = wm.create('test_website_v_1', 'www.test_url.com')
        updated_web = wm.update_name('test_website_v_1', 'updateed_test_website_v_1')
        self.assertEqual(updated_web.website_name, 'updateed_test_website_v_1')
    
    def test_create_website(self):
        wm = WebsiteManager(session)
        web_created = wm.create('test_website_v_2', 'www.test_url.com')
        web_obj = wm.get_name('test_website_v_2')
        self.assertEqual(web_obj.website_name, 'test_website_v_2')
    
    def test_list_website(self):
        wm = WebsiteManager(session)
        count_wm = wm.get_list_count()
        count, list_website = wm.list()
        self.assertEqual(count, count_wm)
    
    
    
