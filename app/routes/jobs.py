from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.core.database import get_db
from app.models.job import Job
from app.schemas.job_schema import JobCreate

from app.workers.tasks import process_job


router = APIRouter()


# Home API
@router.get("/")
def home():

    return {
        "message": "Job Queue System"
    }



# Create Job
@router.post("/jobs")
def create_job(
    job_data: JobCreate,
    db: Session = Depends(get_db)
):

    new_job = Job(

        job_type=job_data.job_type,

        payload=job_data.payload,

        priority=job_data.priority,

        status="Pending",

        retry_count=0,

        created_at=datetime.now()

    )


    db.add(new_job)

    db.commit()

    db.refresh(new_job)



    # Priority based queue routing

    if new_job.priority == "high":

        process_job.apply_async(
            args=[new_job.id],
            queue="high"
        )


    elif new_job.priority == "medium":

        process_job.apply_async(
            args=[new_job.id],
            queue="medium"
        )


    else:

        process_job.apply_async(
            args=[new_job.id],
            queue="low"
        )



    return {

        "id": new_job.id,

        "priority": new_job.priority,

        "status": new_job.status,

        "message": "Job added to queue"

    }



# Get All Jobs
@router.get("/jobs")
def get_jobs(

    db: Session = Depends(get_db)

):

    jobs = db.query(Job).all()

    return jobs



# Get Single Job
@router.get("/jobs/{id}")
def get_job(

    id: int,

    db: Session = Depends(get_db)

):

    job = db.query(Job).filter(
        Job.id == id
    ).first()


    return job



# Dashboard
@router.get("/dashboard")
def dashboard(

    db: Session = Depends(get_db)

):

    jobs = db.query(Job).all()


    # Total processing time
    total_processing_time = sum(
        [
            job.processing_time or 0
            for job in jobs
        ]
    )


    return {


        "total_jobs":
        len(jobs),



        "pending_jobs":
        db.query(Job)
        .filter(Job.status == "Pending")
        .count(),



        "running_jobs":
        db.query(Job)
        .filter(Job.status == "Running")
        .count(),



        "completed_jobs":
        db.query(Job)
        .filter(Job.status == "Completed")
        .count(),



        "failed_jobs":
        db.query(Job)
        .filter(Job.status == "Failed")
        .count(),



        "processing_statistics": {

            "total_processing_seconds":
            total_processing_time

        },



        "queue_statistics": {

            "high_priority_jobs":
            db.query(Job)
            .filter(Job.priority == "high")
            .count(),


            "medium_priority_jobs":
            db.query(Job)
            .filter(Job.priority == "medium")
            .count(),


            "low_priority_jobs":
            db.query(Job)
            .filter(Job.priority == "low")
            .count()

        }

    }