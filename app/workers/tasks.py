from app.queue.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.job import Job
from app.core.logger import logger

import time
from datetime import datetime


@celery_app.task(bind=True, max_retries=3)
def process_job(self, job_id):

    db = SessionLocal()

    job = None

    try:

        # Get job from database
        job = db.query(Job).filter(
            Job.id == job_id
        ).first()


        if job:

            # Pending -> Running
            job.status = "Running"
            job.started_at = datetime.now()

            db.commit()


        logger.info(f"Processing Job ID: {job_id}")


        # Simulate long running task
        time.sleep(10)



        if job:

            # Running -> Completed
            job.status = "Completed"
            job.completed_at = datetime.now()


            # Calculate processing time
            job.processing_time = (
                job.completed_at - job.started_at
            ).total_seconds()


            db.commit()


        logger.info(
            f"Job {job_id} Completed in {job.processing_time} seconds"
        )


    except Exception as e:


        if job:

            # Failed status
            job.status = "Failed"

            job.error_message = str(e)

            job.retry_count += 1

            db.commit()


        logger.error(
            f"Job {job_id} Failed: {e}"
        )


        # Retry failed jobs
        raise self.retry(
            exc=e,
            countdown=5
        )


    finally:

        db.close()