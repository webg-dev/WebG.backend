from models import WebPage, NodeLabel


def test_create_web_page(mongodb, mongo_database, web_page):
    mongo_database.create_web_page(web_page)

    document = mongodb['web_pages'].find_one({'id': web_page.id})
    assert WebPage(**document) == web_page


def test_get_web_page(mongodb, mongo_database):
    _id = 'cbca3e55-14c9-45e9-9ce2-2453019bbfbe'
    document = mongodb['web_pages'].find_one({'id': _id})
    expected_web_page = WebPage(**document)

    web_page = mongo_database.get_web_page(_id)

    assert web_page == expected_web_page


def test_update_web_page(mongodb, mongo_database):

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

    mongo_database.update_web_page(_id=web_page.id, web_page=web_page)

    web_page = _get_test_web_page()
    assert web_page.labels == new_labels
