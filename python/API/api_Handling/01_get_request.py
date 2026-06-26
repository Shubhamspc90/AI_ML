import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

response=requests.get(url)

print(response)

print("Status Code: ",response.status_code)

