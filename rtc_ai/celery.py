import os
from logging.config import dictConfig

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtc_ai.settings')
app = Celery('rtc_ai', broker_connection_retry_on_startup=True)

app.config_from_object('django.conf:settings', namespace='CELERY')


@setup_logging.connect
def config_loggers(*args, **kwargs):
    dictConfig(settings.LOGGING)


# ! periodic task registration
# app.conf.beat_schedule = {
#     'clear_action_log': {
#         'task': 'mps_core.tasks.clear_action_log',
#         'schedule': crontab(hour='3', minute='0'),
#     }
# }

app.autodiscover_tasks()
