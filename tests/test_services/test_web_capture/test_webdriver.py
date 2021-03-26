import pytest

from services.web_capture.web_driver import WebDriver, WebPage


@pytest.mark.parametrize('use_virtual_display', [True, False])
def test_web_driver(use_virtual_display, url, expected_web_page_dict):
    """Tests that WebPage object can be captured correctly
    for a very small, fixed page both with and without the use
    of a virtual display."""
    webdriver = WebDriver(use_virtual_display=use_virtual_display)
    web_page = webdriver.get_web_page(url)
    webdriver.close()

    assert isinstance(web_page, WebPage)
    assert web_page.dict() == expected_web_page_dict
