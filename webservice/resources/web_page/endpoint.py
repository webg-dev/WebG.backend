import os
from urllib.parse import urlparse

from fastapi import APIRouter

from models import WebPage
from services.web_capture.web_driver import WebDriver

router = APIRouter()


@router.get('/webPage', response_model=WebPage)
def get_web_page(url: str) -> WebPage:
    if os.path.isfile(url):
        url = 'file://' + url
    else:
        url = urlparse(url, 'https').geturl()
    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(url)
    webdriver.quit()
    return web_page
