from config.env import env
from .base_database import BaseDatabase
from .mongo_database import MongoDatabase

if env.db_type == 'mongo':
    database = MongoDatabase()
else:
    pass
