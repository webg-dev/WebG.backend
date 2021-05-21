from abc import ABC, abstractmethod
from uuid import UUID

from models import WebPage


class BaseDatabase(ABC):

    @abstractmethod
    def get_web_page(self, _id: UUID) -> WebPage:
        pass

    @abstractmethod
    def save_web_page(self, web_page: WebPage) -> None:
        pass
