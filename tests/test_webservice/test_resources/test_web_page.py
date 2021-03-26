from models import WebPage


def test_predict_endpoint(app, client, url, expected_web_page_dict):

    response = client.get(f'/webPage?url={url}')

    assert response.status_code == 200
    response_body = response.json()
    web_page = WebPage(**response_body)
    assert web_page.dict() == expected_web_page_dict
