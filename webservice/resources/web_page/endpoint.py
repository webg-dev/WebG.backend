import os
from urllib.parse import urlparse

from fastapi import APIRouter, Request

from models import WebPage
from services.web_capture.web_driver import WebDriver
from services.data_storage import BaseDatabase

router = APIRouter()


@router.get('/webPage', response_model=WebPage)
def get_web_page(request: Request, url: str) -> WebPage:
    url = normalize_url(url)

    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(url)
    webdriver.quit()

    db: BaseDatabase = request.app.state.db
    db.save_web_page(web_page)

    return web_page


def normalize_url(url: str) -> str:
    if os.path.isfile(url):
        return 'file://' + url
    else:
        return urlparse(url, 'https').geturl()
