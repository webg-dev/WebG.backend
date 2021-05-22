import pytest

from models import WebPage, NodeLabel

from services.data_storage import MongoDatabase


@pytest.fixture()
def db(mongodb) -> MongoDatabase:
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


def test_create_web_page(mongodb, db, web_page):
    db.create_web_page(web_page)

    document = mongodb['web_pages'].find_one({'id': web_page.id})
    assert WebPage(**document) == web_page


def test_get_web_page(mongodb, db):
    _id = 'cbca3e55-14c9-45e9-9ce2-2453019bbfbe'
    document = mongodb['web_pages'].find_one({'id': _id})
    expected_web_page = WebPage(**document)

    web_page = db.get_web_page(_id)

    assert web_page == expected_web_page


def test_update_web_page(mongodb, db):

    def _get_test_web_page():
        document = mongodb['web_pages'].find_one({'id': 'cbca3e55-14c9-45e9-9ce2-2453019bbfbe'})
        return WebPage(**document)

    web_page = _get_test_web_page()
    new_labels = [
        NodeLabel(
            className='price',
            nodeId=0
        )
    ]
    web_page.labels = new_labels

    db.update_web_page(_id=web_page.id, web_page=web_page)

    web_page = _get_test_web_page()
    assert web_page.labels == new_labels
