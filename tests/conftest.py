from pathlib import Path

import pytest

from utils.io_funcs import read_json_file


@pytest.fixture()
def url():
    test_html_path = Path(__file__).resolve().parent / 'mock_data/test_page_1.html'
    url = f'file://{test_html_path}'
    return url


@pytest.fixture()
def expected_web_page_dict(url: str) -> dict:
    expected_web_page_path = Path(__file__).resolve().parent / 'mock_data/expected_web_page_1.json'
    expected_web_page_dict = read_json_file(expected_web_page_path)
    expected_web_page_dict['url'] = str(url)  # must override this as path be different for each machine.
    return expected_web_page_dict
