


class Config(object):
    #celery app configuration
    result_backend = "redis://localhost:6379/0"
    broker_url = "amqp://guest:guest@localhost:5672//"
    timezone = ""
    enable_utc = True
