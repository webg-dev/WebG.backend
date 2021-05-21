from abc import ABC, abstractmethod

from models import WebPage


class BaseDatabase(ABC):

    @abstractmethod
    def get_web_page(self, _id: str) -> WebPage:
        pass

    @abstractmethod
    def save_web_page(self, web_page: WebPage) -> WebPage:
        pass
