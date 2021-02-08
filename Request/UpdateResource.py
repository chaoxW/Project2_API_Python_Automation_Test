import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users/2"

# read input json file
file = open("C:/Users/shuai.wang/PycharmProjects/API Tets/Lib/opponentUpdated.json")
request_json = json.loads(file.read())
print(request_json)

# put request
response = requests.put(url,request_json)
print(response)
assert response.status_code == 200

# parse response content
response_json = json.loads(response.text)

# fetch opponent updated
opponent_update = jsonpath.jsonpath(response_json,"opponent")
print(opponent_update[0])

assert opponent_update[0] == "TestOpponent updated"