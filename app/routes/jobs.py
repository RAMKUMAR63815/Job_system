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

        created_at=datetime.now()

    )


    db.add(new_job)

    db.commit()

    db.refresh(new_job)


    # Send job to Redis Queue
    process_job.delay(new_job.id)


    return {

        "id": new_job.id,

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

    id:int,

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

    return {


        "total_jobs":
        db.query(Job).count(),


        "pending_jobs":
        db.query(Job)
        .filter(Job.status=="Pending")
        .count(),


        "running_jobs":
        db.query(Job)
        .filter(Job.status=="Running")
        .count(),


        "completed_jobs":
        db.query(Job)
        .filter(Job.status=="Completed")
        .count(),


        "failed_jobs":
        db.query(Job)
        .filter(Job.status=="Failed")
        .count()

    }