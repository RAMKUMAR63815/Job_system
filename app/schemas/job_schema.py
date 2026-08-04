from pydantic import BaseModel

class JobCreate(BaseModel):

    job_type: str

    payload: dict

    priority: str