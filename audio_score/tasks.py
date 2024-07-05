import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def t_ping():
    logger.info('t_ping')
