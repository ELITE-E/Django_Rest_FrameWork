import requests

#endpoint="https://httpbin.org/status/200"
#Is this for the app we created ,maybe 
endpoint="http://127.0.0.1:8000/api/"

#get_response=requests.get(endpoint,json={"query":"Hello world"})#A http request
# 01.1 The post req
get_res=requests.post(endpoint,json={"title":"OH my 1123"})

#print(get_response.text) #print source code
#print(get_response.json())
#print(get_response.status_code)

#01.02. Lets see what happens 

print(get_res.json())
print(get_res.status_code)

