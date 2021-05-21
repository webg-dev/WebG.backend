from pathlib import Path

import pytest


@pytest.fixture()
def test_page_1_file_path() -> Path:
    return Path(__file__).resolve().parent / 'mock_data/html/test_page_1.html'


@pytest.fixture()
def test_page_1_url(test_page_1_file_path):
    url = f'file://{test_page_1_file_path}'
    return url
