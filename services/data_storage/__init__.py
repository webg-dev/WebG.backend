from config.env import env
from .mongo_database import MongoDatabase

if env.db_type == 'mongo':
    database = MongoDatabase()
else:
    database = None
