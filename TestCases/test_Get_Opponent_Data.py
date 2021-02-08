import json
import requests
import jsonpath

def test_get_opponent_status_code():
    # API URL
    url = "https://reqres.in/api/users?page=2"
    # get request
    response = requests.get(url)

    # validate response code
    response_code = response.status_code
    assert response_code == 200




def test_get_opponent_data():
    # API URL
    url = "https://reqres.in/api/users?page=2"
    # get request
    response = requests.get(url)
    # parse response to Json format
    #json_response = json.loads(response.text)
    json_response = response.json()
    #print(json_response)

    # Fetch value using json path
    first_name = jsonpath.jsonpath(json_response, "data[0].first_name")
    print(first_name[0])
    assert first_name[0] == "Michael"