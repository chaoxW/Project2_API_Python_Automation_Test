import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"
# read input json file
file = open("C:/Users/shuai.wang/PycharmProjects/API Tets/Lib/opponent.json","r")
json_input = file.read()
request_json = json.loads(json_input)
#print(request_json)

# post request with json input body
response = requests.post(url,request_json)

print(response.status_code)
#print(response.content)

assert response.status_code == 201

# fetch header from response
#print(response.headers)
print(response.headers.get("Content-Type"))

# parse response to json format
response_json = json.loads(response.text)
#print(response_json)

#get id with json path
id = jsonpath.jsonpath(response_json,"id")
print(id[0])