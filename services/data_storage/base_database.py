from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

from models import WebPage


class BaseDatabase(ABC):

    @abstractmethod
    def create_web_page(self, web_page: WebPage) -> None:
        """Saves web page to database."""
        pass

    @abstractmethod
    def get_web_page(self, _id: UUID) -> Union[WebPage, None]:
        """Fetches and returns web page from database with
        given id or None if it does not exist."""
        pass

    @abstractmethod
    def update_web_page(self, _id: UUID, web_page: WebPage) -> Union[WebPage, None]:
        """Updates web page in database with given ID and
        returns the web page after update. Returns None if
        web page does not exist with this ID."""
        pass
