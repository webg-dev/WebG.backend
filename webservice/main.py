from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from services.data_storage import database
from webservice.resources import api_router

app = FastAPI()

app.include_router(api_router)

app.state.db = database

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
