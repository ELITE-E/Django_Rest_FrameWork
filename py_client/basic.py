import requests

#endpoint="https://httpbin.org/status/200"
#Is this for the app we created ,maybe 
endpoint="http://127.0.0.1:8000/api"

get_response=requests.get(endpoint,json={"query":"Hello world"})#A http request

#print(get_response.text) #print source code
print(get_response.json())
print(get_response.status_code)
