import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

response = requests.get(url)
print("\nStatus Score: ", response.status_code)
print("\nReason: " , response.reason)
print("\nHeaders: " ,response.headers)
print("\nText: " ,response.text)
print("\nConnection: " ,response.connection)

