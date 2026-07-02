import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

headers = {
    "User-Agent": "Python Requests",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

print("\nResponse Headers\n")

for key, value in response.headers.items():
    print(key, ":", value)