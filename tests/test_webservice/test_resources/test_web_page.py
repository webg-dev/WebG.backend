from models import WebPage


def test_predict_endpoint(app, client, test_page_1_url, expected_web_page_dict_for_test_page_1):

    response = client.get(f'/webPage?url={test_page_1_url}')

    assert response.status_code == 200
    response_body = response.json()
    web_page = WebPage(**response_body)
    assert web_page.dict() == expected_web_page_dict_for_test_page_1
