import requests

endpoint="https://httpbin.org/ip"

get_response=requests.get(endpoint)#A http request

print(get_response.text) #print source code
