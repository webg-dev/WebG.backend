import os
from urllib.parse import urlparse
from uuid import UUID

from fastapi import APIRouter, Request
from pydantic import BaseModel

from models import WebPage
from services.web_capture.web_driver import WebDriver
from services.data_storage import BaseDatabase
from webservice.exceptions import WebPageDoesNotExist

router = APIRouter()


class PostWebPageRequest(BaseModel):
    url: str


@router.post(
    path='/pages/',
    response_model=WebPage,
    status_code=201
)
def create_web_page(request: Request, body: PostWebPageRequest) -> WebPage:
    url = normalize_url(body.url)

    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(url)
    webdriver.quit()

    db: BaseDatabase = request.app.state.db
    db.create_web_page(web_page)

    return web_page


@router.get(
    path='/pages/{_id}',
    response_model=WebPage,
    status_code=200
)
def get_web_page(request: Request, _id: str) -> WebPage:
    db: BaseDatabase = request.app.state.db

    web_page = db.get_web_page(_id)

    if web_page is None:
        raise WebPageDoesNotExist(_id=_id)

    return web_page


@router.put(
    path='/pages/{_id}',
    response_model=WebPage,
    status_code=200
)
def update_web_page(request: Request, _id: str, web_page: WebPage) -> WebPage:
    db: BaseDatabase = request.app.state.db

    web_page = db.update_web_page(_id, web_page)

    if web_page is None:
        raise WebPageDoesNotExist(_id=_id)

    return web_page


def normalize_url(url: str) -> str:
    if os.path.isfile(url):
        return 'file://' + url
    else:
        return urlparse(url, 'https').geturl()
