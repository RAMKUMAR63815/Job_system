from app.core.database import Base
from app.core.database import engine

from app.models.job import Job

Base.metadata.create_all(bind=engine)

print("Tables Created")