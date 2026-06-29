import requests
url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
response = requests.get(url)
data = response.json()
user= data["data"]

print("\nUser Gender: ",user["gender"])
print("\nuser name: ", user["name"]["title"],user["name"]["first"],user["name"]["last"])
print("\nlocation: ",user["location"]["city"])
print("\nstreet number: ",user["location"]["street"]["number"])
print("\nuser_name: ",user["login"]["username"])

 