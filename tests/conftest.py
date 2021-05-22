from pathlib import Path

import pytest

from models.web_page import WebPage


@pytest.fixture()
def test_page_1_file_path() -> Path:
    return Path(__file__).resolve().parent / 'mock_data/html/test_page_1.html'


@pytest.fixture()
def test_page_1_url(test_page_1_file_path):
    url = f'file://{test_page_1_file_path}'
    return url


@pytest.fixture()
def web_page() -> WebPage:
    web_page_dict = {
        "id": "56cd47c1-8597-4835-9958-2610eea4db6a",
        "url": "https://test.com",
        "viewportWidth": 1,
        "viewportHeight": 1,
        "html": "html",
        "screenshot": "base64 screenshot",
        "graph": {
            "nodes": [
                {
                    "id": 0,
                    "label": "html",
                    "attributes": {
                        "class": "css class name"
                    },
                    "coordinates": {
                        "width": 1.0,
                        "height": 1.0,
                        "left": 1.0,
                        "right": 1.0,
                        "top": 1.0,
                        "bottom": 1.0
                    },
                    "isVisible": True
                }
            ],
            "edges": [
                {
                    "from": 0,
                    "to": 1
                }
            ],
            "labels": [
                {
                    "nodId": 1,
                    "className": "className"
                }
            ]
        }
    }

    return WebPage(**web_page_dict)
