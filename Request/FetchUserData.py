import requests
import json
import  jsonpath
# API URL
url = "https://reqres.in/api/users?page=2"
# send get request
response = requests.get(url)

#display response content
print(response)
#print(response.content)
#print(response.headers)

#parse response to Json format
#json_response = json.loads(response.text)
json_response = response.json()
print(json_response)

#Fetch value using json path
first_name = jsonpath.jsonpath(json_response,"data[0].first_name")
print(first_name[0])
assert first_name[0] == "Michael"