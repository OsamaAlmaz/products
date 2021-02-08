import requests
from lxml import html
from pymongo import MongoClient
from celery_app.app import Database
from celery_app.constants import URL
from celery_app.constants import content_array
from productsapp.data_access.website import get_base_url
from furl import furl


class Error(Exception):
    pass

class Urlnotfound(Error):
    def __init__(self, message):
        self.message = message


class Extractor():
    def _extractor (self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        root_url = furl(url).host
        website_object = get_base_url(root_url)
        store_id = website_object.id
        content = content_array.get(store_id)
        self._extractFields(url, content, tree)
        return

    def _extractFields(self, url, content_array):
        title = tree.xpath(content_array['title'][0])
        price = tree.xpath(content_array['price'][0])
        description = tree.xpath(content_array['description'][0])
        model_number = tree.xpath(content_array['model_number'][0])
        image = tree.xpath(content_array['image'][0])
        #serialize it and then send it off to productsapp database. 
        return
    

    def extractFields(self):
        self.__extract(URL)
        page = requests.get(URL)
        tree = html.fromstring(page.content)
        title = tree.xpath("//div[@id= 'product-overview']//h1//text()")
        price = tree.xpath("//span[@class = 'price-characteristic']//@content")
        # connect to mongodb or use a connection in order for you to post and get data.
        db = Database()
        collection = db.get_collections()
        post = {
            "title": title,
            "price": price
        }
        id = collection.insert_one(post).inserted_id
        print("The id "+ str(id) + " was successfully added")

    def __extract(self, url):
        try:
            r = requests.get(url)
        except:
            raise Urlnotfound('URL is not found')




if __name__ == "__main__":
    extractor = Extractor()
    extractor.extractFields()

