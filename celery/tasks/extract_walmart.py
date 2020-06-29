
import requests
from constands.constant import URL
from lxml import html

class Error(Exception):
    pass

class Urlnotfound(Error):
    def __init__(self, message):
        self.message = message



class Extractor():

    def extractFields(self):
        self.__extract(URL)
        page = requests.get(URL)
        tree = html.fromString(page.content)
        title = tree.xpath("//div[@id= 'product-overview']//h1//text()")
        price = tree.xpath("//span[@class = 'price-characteristic']//@content")
        model_number= tree.xpath()
        

        

    def __extract(self, url, timeouts):
        try:
            r = requests.get(url)
        except:
            raise Urlnotfound('URL is not found')
