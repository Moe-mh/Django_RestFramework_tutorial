import requests

endpoint = "https://httpbin.org"

# Send your own data with get()
# We can send anything and recieve the same type of sent data.
response = requests.get(endpoint, json={"query":"Hello world!"}) 
print(response.json())
print(response.status_code())
