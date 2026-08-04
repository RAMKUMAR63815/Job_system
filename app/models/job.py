from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import DateTime

from app.core.database import Base

class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    job_type = Column(String)

    payload = Column(JSON)

    priority = Column(String)

    status = Column(String)

    retry_count = Column(Integer, default=0)

    error_message = Column(String)

    created_at = Column(DateTime)

    started_at = Column(DateTime)

    completed_at = Column(DateTime)