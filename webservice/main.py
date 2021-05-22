from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import env
from services.data_storage import BaseDatabase, MongoDatabase
from webservice.resources import api_router
from utils.logging import initialise_logger

def initialise_database() -> BaseDatabase:
    if env.db_type == 'mongo':
        return MongoDatabase(
            host=env.mongo_host,
            port=env.mongo_port,
            db_name=env.mongo_db_name
        )
    else:
        raise RuntimeError(f'Unhandled database type: "{env.db_type}"')


def initialise_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(api_router)
    _app.state.db = initialise_database()
    _app.state.logger = initialise_logger()
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = initialise_app()
