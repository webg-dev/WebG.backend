from pathlib import Path

import pytest

from models.web_page import WebPage
from services.data_storage import MongoDatabase
from utils.io_funcs import read_json_file


@pytest.fixture()
def mongo_database(mongodb) -> MongoDatabase:
    """Returns instance of MongoDatabase in which the
    'web_pages_collection' attribute is patched using
    the mongodb fixture from pytest-mongodb."""
    db = MongoDatabase(
        host='localhost',
        port=27017,
        db_name='webg_db'
    )

    db.web_pages_collection = mongodb['web_pages']
    return db



@pytest.fixture()
def test_page_1_file_path() -> Path:
    return Path(__file__).resolve().parent / 'mock_data/html/test_page_1.html'


@pytest.fixture()
def test_page_1_url(test_page_1_file_path):
    url = f'file://{test_page_1_file_path}'
    return url


@pytest.fixture()
def expected_web_page_dict_for_test_page_1(test_page_1_url) -> dict:
    expected_web_page_path = Path(__file__).resolve().parent / 'mock_data/web_pages/expected_web_page_for_test_page_1.json'
    expected_web_page_dict = read_json_file(expected_web_page_path)
    expected_web_page_dict['url'] = str(test_page_1_url)  # must override this as path be different for each machine.
    return expected_web_page_dict



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
