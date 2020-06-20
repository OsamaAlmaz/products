from celery import Celery



celery_app = Celery("products", include=['products.celery.tasks'])




