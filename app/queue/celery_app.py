from celery import Celery
from kombu import Queue


celery_app = Celery(
    "job_system",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


# Load tasks automatically
celery_app.autodiscover_tasks(
    ["app.workers"]
)


# Reliability settings
celery_app.conf.update(

    # Do not remove job from queue until completed
    task_acks_late=True,

    # Re-queue job if worker crashes
    task_reject_on_worker_lost=True,

    # Do not acknowledge failed/timeout jobs
    task_acks_on_failure_or_timeout=False,

    # Worker takes one task at a time
    worker_prefetch_multiplier=1,

    # Track task state
    task_track_started=True,

    # Keep completed task results
    result_expires=3600
)


# Priority queues
celery_app.conf.task_queues = (
    Queue("high"),
    Queue("medium"),
    Queue("low"),
)


# Default queue
celery_app.conf.task_default_queue = "medium"


# Optional: route tasks based on priority
celery_app.conf.task_routes = {
    "app.workers.tasks.process_job": {
        "queue": "medium"
    }
}