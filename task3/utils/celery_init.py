from celery import Celery
from utils.env_variables import BACKEND_URL,BROKER_URL

def celery_init_app(title="Scraping") -> Celery:
    celery_app = Celery(title)
    celery_app.conf.update(result_backend=BACKEND_URL)
    celery_app.conf.update(broker_url=BROKER_URL)
    celery_app.conf.update(autodiscover_tasks=True)
    celery_app.conf.update(task_acks_late=True)
    celery_app.conf.update(worker_prefetch_multiplier=1)
    celery_app.conf.update(broker_connection_retry_on_startup=True)

    return celery_app