def test_returns_web_page(app, client, mongodb):
    document = mongodb['web_pages'].find_one({'_id': '0'})
    endpoint_url = app.url_path_for(name='get_web_page', _id=document['id'])

    response = client.get(endpoint_url)

    document.pop('_id')  # remove mongo ID before asserting equality
    assert response.json() == document
