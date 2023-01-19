from celery import shared_task
from celery.utils.log import get_task_logger
from tips.utils import get_data


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    get_data()
    logger.info("The sample task just ran.")
    

    