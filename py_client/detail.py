import requests

endpoint ="http://127.0.0.1:8000/api/products/1/"
get_res=requests.get(endpoint)

print(f"Response Status:{get_res.status_code}")
#print(f"Res text:{get_res.text}")

#print(f"{get_res.__format__}")
#print(get_res.json())