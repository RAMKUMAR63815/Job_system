from celery import Celery


celery_app = Celery(
    "job_system",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


# Load tasks from workers folder
celery_app.autodiscover_tasks(
    ["app.workers"]
)


# Do not lose jobs if worker crashes
celery_app.conf.task_acks_late = True