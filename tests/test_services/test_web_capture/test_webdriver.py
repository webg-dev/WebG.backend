from pathlib import Path
import pytest

from services.web_capture.web_driver import WebDriver, WebPage
from utils.io_funcs import read_json_file


@pytest.mark.parametrize('use_virtual_display', [True, False])
def test_web_driver(use_virtual_display):
    """Tests that WebPage object can be captured correctly
    for a very small, fixed page both with and without the use
    of a virtual display."""
    test_html_path = Path(__file__).resolve().parent.parent.parent / 'test_data/test_page_1.html'
    expected_web_page_path = Path(__file__).resolve().parent.parent.parent / 'test_data/expected_web_page_1.json'
    url = f'file://{test_html_path}'
    expected_web_page_dict = read_json_file(expected_web_page_path)
    expected_web_page_dict['url'] = str(url)  # must override this as path be different for each machine.

    webdriver = WebDriver(use_virtual_display=use_virtual_display)
    web_page = webdriver.get_web_page(url)
    webdriver.close()

    assert isinstance(web_page, WebPage)
    assert web_page.dict() == expected_web_page_dict
