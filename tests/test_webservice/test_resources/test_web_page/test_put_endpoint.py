def test_updates_web_page_in_db(app, client, mongodb):
    document = mongodb['web_pages'].find_one({'_id': '0'})
    endpoint_url = app.url_path_for(name='update_web_page', _id=document['id'])
    updated_html = 'updated html'
    document['html'] = updated_html
    document.pop('_id')

    response = client.put(endpoint_url, json=document)

    assert response.status_code == 200
    document = mongodb['web_pages'].find_one({'_id': '0'})
    assert document['html'] == updated_html
