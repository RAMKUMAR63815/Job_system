# Asynchronous Job Processing System

## Project Overview

Job Queue System is a backend application developed using FastAPI, Celery, Redis, and PostgreSQL.

The main purpose of this project is to process long-running tasks asynchronously using background workers. The system allows users to submit jobs, manage job priorities, track execution status, monitor processing details, and manage jobs efficiently through filtering, sorting, pagination, and cancellation features.

---

# Technology Stack

* Python
* FastAPI
* PostgreSQL
* Redis
* Celery
* SQLAlchemy
* Pydantic

---

# System Architecture

```text
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

```text
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

* Create new jobs
* Store job details in PostgreSQL
* Track complete job lifecycle
* Retrieve individual jobs
* Retrieve all jobs

---

## Asynchronous Processing

* Background task execution using Celery
* Redis used as message broker
* Independent worker execution
* API remains responsive during processing

---

## Queue Management

Implemented priority-based queues:

* High Priority Queue
* Medium Priority Queue
* Low Priority Queue

Features:

* Priority-based routing
* FIFO queue processing
* Queue statistics monitoring

---

## Retry Mechanism

* Automatic retry for failed tasks
* Configurable retry limits
* Retry count tracking
* Error message storage
* Failure logging

---

## Worker System

* Independent Celery worker process
* Background job execution
* Multiple worker support
* Concurrent task processing

---

## Worker Reliability

Implemented:

* Task acknowledgement handling
* Worker crash recovery
* Failed task re-queuing
* Safe task execution

---

## Monitoring Dashboard

Implemented APIs for:

* Total jobs
* Pending jobs
* Running jobs
* Completed jobs
* Failed jobs
* Queue statistics
* Processing statistics

---

## Processing Time Tracking

Tracks:

* Job creation time
* Job start time
* Job completion time
* Total execution duration

---

## Pagination

Supports pagination for large datasets.

Examples:

```http
GET /jobs?page=1&limit=10
```

Benefits:

* Faster response time
* Reduced database load
* Efficient job browsing

---

## Filtering

Supports filtering by:

### Status

```http
GET /jobs?status=Completed
```

### Priority

```http
GET /jobs?priority=high
```

### Combined Filtering

```http
GET /jobs?status=Pending&priority=medium
```

---

## Sorting

Supports sorting by:

### Created Time

```http
GET /jobs?sort_by=created_at
```

### Processing Time

```http
GET /jobs?sort_by=processing_time
```

---

## Job Cancellation

Implemented job cancellation support.

Endpoint:

```http
POST /jobs/{id}/cancel
```

Features:

* Cancel pending jobs
* Cancel running jobs
* Prevent cancellation of completed jobs
* Prevent cancellation of failed jobs

---

## Logging

Implemented structured logging:

* Job processing logs
* Completion logs
* Retry logs
* Error logs

---

# Database Implementation

Database:

```text
PostgreSQL
```

Database Name:

```text
job_system
```

Table Name:

```text
jobs
```

## Job Table Fields

* id
* job_type
* payload
* priority
* status
* retry_count
* error_message
* created_at
* started_at
* completed_at
* processing_time

---

# Installation and Setup

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate to Project Folder

```bash
cd Job_System
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection
REDIS_URL=redis://localhost:6379/0
```

---

# Running the Application

## Start FastAPI Server

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Start Celery Worker

```bash
celery -A app.queue.celery_app worker --pool=solo
```

---

# API Endpoints

## Create Job

```http
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

```http
GET /jobs
```

---

## Pagination

```http
GET /jobs?page=1&limit=10
```

---

## Filter By Status

```http
GET /jobs?status=Completed
```

---

## Filter By Priority

```http
GET /jobs?priority=high
```

---

## Sort By Created Time

```http
GET /jobs?sort_by=created_at
```

---

## Sort By Processing Time

```http
GET /jobs?sort_by=processing_time
```

---

## Combined Example

```http
GET /jobs?page=1&limit=5&status=Completed&priority=high
```

---

## Get Job By ID

```http
GET /jobs/{id}
```

---

## Cancel Job

```http
POST /jobs/{id}/cancel
```

Example:

```http
POST /jobs/1/cancel
```

Response:

```json
{
  "id": 1,
  "status": "Cancelled",
  "message": "Job cancelled successfully"
}
```

---

## Dashboard Statistics

```http
GET /dashboard
```

Dashboard provides:

* Total jobs
* Pending jobs
* Running jobs
* Completed jobs
* Failed jobs
* Queue statistics
* Processing statistics

---

# Job Lifecycle

Normal Flow:

```text
Pending
   |
Running
   |
Completed
```

Failure Flow:

```text
Running
   |
Failed
```

Cancellation Flow:

```text
Pending
   |
Cancelled
```

---

# Verification Completed

The system was tested and verified for:

* FastAPI server execution
* PostgreSQL database connection
* Job creation API
* Redis queue integration
* Celery worker execution
* Asynchronous processing
* Priority queue handling
* FIFO queue behavior
* Retry mechanism
* Error handling
* Worker recovery
* Dashboard monitoring
* Processing time tracking
* Logging implementation
* Pagination functionality
* Status filtering
* Priority filtering
* Job sorting
* Job cancellation workflow

---

# Future Enhancements

* Docker deployment
* WebSocket live updates
* Scheduled jobs
* Dead Letter Queue
* Authentication and Authorization
* Rate limiting

---

# Project Status

## Completed Successfully

The Job Queue System provides a reliable backend solution for asynchronous job processing using:

* FastAPI
* PostgreSQL
* Redis
* Celery
* SQLAlchemy

Additional production-ready features implemented:

* Pagination
* Filtering
* Sorting
* Job Cancellation

---

# Developer

Ramkumar S
