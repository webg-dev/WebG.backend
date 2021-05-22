from uuid import UUID

from services.web_capture.web_driver import WebDriver, WebPage


def test_returns_expected_web_page_object(test_page_1_url, expected_web_page_dict_for_test_page_1):
    """Tests that WebPage object can be captured correctly
    for a very small, fixed page both with and without the use
    of a virtual display."""
    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(test_page_1_url)
    webdriver.quit()

    assert isinstance(web_page, WebPage)
    assert isinstance(web_page.id, str)
    assert web_page.dict(exclude={'id'}) == expected_web_page_dict_for_test_page_1
