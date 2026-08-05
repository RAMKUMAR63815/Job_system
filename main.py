from fastapi import FastAPI

from app.routes.jobs import router

app = FastAPI()

app.include_router(router)