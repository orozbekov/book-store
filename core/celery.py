import os 

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(name="core.heartbeat")
def heartbeat():
    logger.info("Celery heartbeat: Я работаю")


app.conf.beat_schedule = {
    "heartbeat-everyminute": {
        "task": "core.heartbeat",
        "schedule": 60.0,
    },
}

