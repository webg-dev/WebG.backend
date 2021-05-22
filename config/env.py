from pydantic import BaseSettings

from .common import ROOT_DIR


class Env(BaseSettings):
    db_type: str

    # Mongo DB
    mongo_host: str
    mongo_port: int
    mongo_db_name: str

    class Config:
        env_file = str(ROOT_DIR / '.env')
        env_prefix = 'WEBG_'
        case_sensitive = False


env = Env()
