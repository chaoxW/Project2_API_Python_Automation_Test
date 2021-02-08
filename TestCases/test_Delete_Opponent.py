import json
import requests
import jsonpath

def test_delete_opponent():
    # API URL
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)
    # fetch response code
    print(response.status_code)
    assert response.status_code == 204

    # should use get to verify the user got deleted
    # but it is open api we can not verify that

    # get_repsonse = requests.get(url)
    # print(get_repsonse.status_code)
    # assert get_repsonse.status_code == 404

    # url with 404
    url_404 = "https://reqres.in/api/unknown/23"

    repsonse_404 = requests.get(url_404)
    print(repsonse_404.status_code)
    assert repsonse_404.status_code == 404