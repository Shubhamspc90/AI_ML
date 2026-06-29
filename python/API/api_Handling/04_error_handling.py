import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    print("Success")
    print(data["data"]["name"]["first"])

except requests.exceptions.HTTPError:
    print("HTTP Error")

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.Timeout:
    print("Timeout")

except requests.exceptions.RequestException as e:
    print("Error:", e)