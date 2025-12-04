import requests

product_id=input("What is the product ID you want to use ?")
try:
    product_id=int(product_id)

except:
    product_id=None
    print(f"{product_id} not a valid id ")

if product_id:
    endpoint=f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response=requests.delete(endpoint)
    print(f"Response Status:{get_response.status_code}")
    print(f"Res text:{get_response.text}")
    #print(f"Response :{get_response.json()}")
    