from uuid import UUID

import pytest

from services.web_capture.web_driver import WebDriver, WebPage


def test_returns_expected_web_page_object(url, expected_web_page_dict):
    """Tests that WebPage object can be captured correctly
    for a very small, fixed page both with and without the use
    of a virtual display."""
    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(url)
    webdriver.quit()

    assert isinstance(web_page, WebPage)
    assert isinstance(web_page.id, UUID)
    assert web_page.dict(exclude={'id'}) == expected_web_page_dict
