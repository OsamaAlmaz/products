from celery import Celery
from config import Config
from pymongo import MongoClient


celery_app = Celery("products", include=['products.celery_app.tasks'])
celery_app.config_from_object(Config)

class Database():
    def get_client(self):
        client = MongoClient('mongodb://localhost:27017/')
        return client
    def get_database(self):
        client = self.get_client()
        return client.products
    def get_collections(self):
        database = self.get_database()
        return database.extractedProducts


URL = 'https://www.walmart.com/ip/ASUS-VivoBook-Flip-14-Thin-Light-2-in-1-Laptop-14-FHD-Intel-Core-i5-8265U-8GBDDR4-RAM-512GB-SSD-Glossy-Touch-Fingerprint-Reader-Windows-10-Star-Grey-/501082588'

X  M