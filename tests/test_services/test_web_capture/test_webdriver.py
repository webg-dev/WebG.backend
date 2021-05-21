from pathlib import Path
from uuid import UUID

import pytest

from services.web_capture.web_driver import WebDriver, WebPage
from utils.io_funcs import read_json_file


@pytest.fixture()
def expected_web_page_dict_for_test_page_1(test_page_1_url) -> dict:
    expected_web_page_path = Path(__file__).resolve().parent / 'expected_web_page_1.json'
    expected_web_page_dict = read_json_file(expected_web_page_path)
    expected_web_page_dict['url'] = str(test_page_1_url)  # must override this as path be different for each machine.
    return expected_web_page_dict



def test_returns_expected_web_page_object(test_page_1_url, expected_web_page_dict_for_test_page_1):
    """Tests that WebPage object can be captured correctly
    for a very small, fixed page both with and without the use
    of a virtual display."""
    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(test_page_1_url)
    webdriver.quit()

    assert isinstance(web_page, WebPage)
    assert isinstance(web_page.id, UUID)
    assert web_page.dict(exclude={'id'}) == expected_web_page_dict_for_test_page_1
