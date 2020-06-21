from celery import Celery
from products.config import Config


celery_app = Celery("products", include=['products.celery.tasks'])
celery_app.config_from_object(Config)
