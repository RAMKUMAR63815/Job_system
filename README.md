# Backend Job Queue System

## Project Overview

Job Queue System is a backend application developed using FastAPI, Celery, Redis, and PostgreSQL.

The main purpose of this project is to process long-running tasks asynchronously using background workers. The system allows users to submit jobs, manage job priorities, track execution status, and monitor job processing details.

---

# Technology Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- Celery
- SQLAlchemy
- Pydantic

---

# System Architecture

```
User
 |
FastAPI API
 |
PostgreSQL Database
 |
Redis Queue
 |
Celery Worker
 |
Job Processing
 |
Database Status Update
```

---

# Project Structure

```
app
│
├── core
│   ├── database.py
│   └── logger.py
│
├── models
│   └── job.py
│
├── routes
│   └── jobs.py
│
├── schemas
│   └── job_schema.py
│
├── services
│   └── job_service.py
│
├── workers
│   └── tasks.py
│
├── queue
│   └── celery_app.py
│
└── main.py
```

---

# Features Implemented

## Job Management
- Create new jobs
- Store job details in PostgreSQL
- Track job lifecycle

## Asynchronous Processing
- Background task execution using Celery
- Redis used as message broker
- API does not wait for long-running tasks

## Queue Management
Implemented priority-based queues:

- High Priority Queue
- Medium Priority Queue
- Low Priority Queue

Features:
- Priority-based routing
- FIFO queue processing

## Retry Mechanism
- Automatic retry for failed tasks
- Maximum retry attempts configured
- Retry count tracking
- Error message storage

## Worker System
- Independent Celery worker process
- Background job execution
- Multiple worker support

## Worker Reliability
Implemented:

- Task acknowledgement handling
- Worker crash recovery
- Failed task re-queuing

## Monitoring Dashboard

Implemented APIs for:

- Total jobs
- Pending jobs
- Running jobs
- Completed jobs
- Failed jobs

## Processing Time Tracking

Tracks:

- Job start time
- Job completion time
- Total execution duration

## Logging

Implemented structured logging:

- Job processing logs
- Completion logs
- Error logs

---

# Database Implementation

Database:

```
PostgreSQL
```

Database Name:

```
job_system
```

Table Name:

```
jobs
```

## Job Table Fields

- id
- job_type
- payload
- priority
- status
- retry_count
- error_message
- created_at
- started_at
- completed_at
- processing_time

---

# Installation and Setup

## Clone Repository

```
git clone <repository-url>
```

## Navigate to Project Folder

```
cd Job_System
```

## Create Virtual Environment

```
python -m venv venv
```

## Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file:

```
DATABASE_URL=your_postgresql_connection
REDIS_URL=redis://localhost:6379/0
```

---

# Running the Application

## Start FastAPI Server

```
uvicorn main:app --reload
```

Application URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start Celery Worker

Run:

```
celery -A app.queue.celery_app worker --pool=solo
```

---

# API Endpoints

## Create Job

Method:

```
POST /jobs
```

Example Request:

```json
{
  "job_type": "file_processing",
  "payload": {
    "file_name": "test.txt",
    "size": "10MB"
  },
  "priority": "high"
}
```

---

## Get All Jobs

```
GET /jobs
```

---

## Get Job By ID

```
GET /jobs/{id}
```

---

## Dashboard Statistics

```
GET /dashboard
```

Dashboard provides:

- Total jobs
- Pending jobs
- Running jobs
- Completed jobs
- Failed jobs

---

# Job Lifecycle

Normal Flow:

```
Pending
   |
Running
   |
Completed
```

Failure Flow:

```
Running
   |
Failed
```

---

# Verification Completed

The system was tested and verified for:

- FastAPI server execution
- PostgreSQL database connection
- Job creation API
- Redis queue integration
- Celery worker execution
- Asynchronous processing
- Priority queue handling
- FIFO queue behavior
- Retry mechanism
- Error handling
- Worker recovery
- Dashboard monitoring
- Processing time tracking
- Logging implementation

---

# Future Enhancements

- Docker deployment
- WebSocket live updates
- Scheduled jobs
- Dead Letter Queue
- Job cancellation
- Rate limiting

---

# Project Status

## Completed Successfully

The Job Queue System provides a reliable backend solution for asynchronous job processing using:

- FastAPI
- PostgreSQL
- Redis
- Celery
- SQLAlchemy

---

# Developer