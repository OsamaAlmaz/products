import requests
from lxml import html
from pymongo import MongoClient
from celery_app.app import Database
from celery_app.constants import URL



class Error(Exception):
    pass

class Urlnotfound(Error):
    def __init__(self, message):
        self.message = message


class Extractor():

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

