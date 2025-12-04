import requests

endpoint="http://127.0.0.1:8000/api/products/1/update/"

data={"title":"Hello world My guys ",
      "price":499.00}


response=requests.put(url=endpoint,json=data)
print(f"Response status:{response.status_code}")
print(f"Response :{response.json()}")