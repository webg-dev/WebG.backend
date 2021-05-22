from typing import Union
from uuid import UUID

from pymongo import MongoClient, ReturnDocument

from models import WebPage
from .base_database import BaseDatabase


class MongoDatabase(BaseDatabase):

    def __init__(self, host: str, port: int, db_name: str):
        self.client = MongoClient(
            host=host,
            port=port,
        )
        self.db = self.client[db_name]
        self.web_pages = self.db['web_pages']

    def get_web_page(self, _id: UUID) -> Union[WebPage, None]:
        document = self.web_pages.find_one({'id': _id})
        return WebPage(**document) if document else None

    def update_web_page(self, _id: UUID, web_page: WebPage) -> Union[WebPage, None]:
        document = self.web_pages.find_one_and_replace(
            filter={'id': _id},
            replacement=web_page.dict(by_alias=True),
            return_document=ReturnDocument.AFTER,
        )
        return WebPage(**document) if document else None


    def create_web_page(self, web_page: WebPage) -> None:
        self.web_pages.insert_one(document=web_page.dict(by_alias=True))
