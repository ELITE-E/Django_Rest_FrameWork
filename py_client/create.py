import requests

endpoint="http://127.0.0.1:8000/api/products/"

data={
    "title":"This whole thing is difficult and nasty I say.",
    "content" : "But I was mad and now ,not that as before like what changed hehehe"
}

get_response=requests.post(endpoint,json=data)

print(get_response.json())