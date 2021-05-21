from pymongo import MongoClient

from config import env
from models import WebPage
from .base_database import BaseDatabase


class MongoDatabase(BaseDatabase):

    def __init__(self):
        self.client = MongoClient(
            host=env.mongo_host,
            port=env.mongo_port,
        )
        self.db = self.client[env.mongo_db_name]
        self.web_pages = self.db['web_pages']

    def get_web_page(self, _id: str) -> WebPage:
        document = self.web_pages.find_one({'id': _id})
        return WebPage(**document)

    def save_web_page(self, web_page: WebPage) -> WebPage:
        document = self.web_pages.insert_one(web_page.dict())
        return WebPage(**document)
