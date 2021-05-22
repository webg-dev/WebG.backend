import logging
from typing import Union

from pymongo import MongoClient, ReturnDocument

from models import WebPage
from .base_database import BaseDatabase

module_logger = logging.getLogger('main_app.services.data_storage.mongo_database')


class MongoDatabase(BaseDatabase):

    def __init__(self, host: str, port: int, db_name: str):
        self.client = MongoClient(
            host=host,
            port=port,
        )
        self.db = self.client[db_name]
        self.web_pages_collection = self.db['web_pages']

    def get_web_page(self, _id: str) -> Union[WebPage, None]:
        document = self.web_pages_collection.find_one({'id': _id})
        return WebPage(**document) if document else None

    def update_web_page(self, _id: str, web_page: WebPage) -> Union[WebPage, None]:
        module_logger.info(f'Updating web page in DB with ID: {web_page.id}')
        document = self.web_pages_collection.find_one_and_replace(
            filter={'id': _id},
            replacement=web_page.dict(by_alias=True),
            return_document=ReturnDocument.AFTER,
        )
        return WebPage(**document) if document else None

    def create_web_page(self, web_page: WebPage) -> None:
        module_logger.info(f'Creating web page in DB with ID: {web_page.id}')
        self.web_pages_collection.insert_one(document=web_page.dict(by_alias=True))
