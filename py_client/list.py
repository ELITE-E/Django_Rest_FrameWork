import requests
from getpass import getpass

auth_endpoint='http://127.0.0.1:8000/api/auth/'
password=getpass()

#2.50---->Token Auth(Post the endpoint + credentials to get an accesstoken )
auth_response=requests.post(auth_endpoint,json={"username":'kskroyal','password':password})
print(auth_response.json())
print(auth_response.status_code)

if auth_response.status_code==200:
    token=auth_response.json()['token']
    print(token)
    headers={
        'Authorization':f"Bearer {token}"#The space between Bearer and {} a must else its misred by DRF as single line of token
    }

    endpoint="http://127.0.0.1:8000/api/products/"

    get_response=requests.get(endpoint,headers=headers)

    print(get_response.json())