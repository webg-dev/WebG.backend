from models import WebPage

import pytest

from webservice.resources.web_page.endpoint import PostWebPageRequest


@pytest.fixture()
def send_request(app, client, test_page_1_url):
    def _send_request():
        endpoint_url = app.url_path_for(name='create_web_page')
        payload = PostWebPageRequest(url=test_page_1_url).dict()
        return client.post(endpoint_url, json=payload)
    return _send_request


def test_returns_web_page(app, client, expected_web_page_dict_for_test_page_1, send_request):
    response = send_request()

    assert response.status_code == 201
    response_body = response.json()
    web_page = WebPage(**response_body)
    assert web_page.dict(exclude={'id'}) == expected_web_page_dict_for_test_page_1


def test_saves_web_page_in_db(app, client, mongodb, test_page_1_url, send_request):
    send_request()

    document = mongodb['web_pages'].find_one({'url': test_page_1_url})

    assert document is not None
