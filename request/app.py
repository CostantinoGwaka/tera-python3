import requests

print(type(requests))
response = requests.get("https://google.com")
print(response.status_code)

print(response)
print(response.status_code)
print(response.headers)
# Print the first 100 characters of the response body
print(response.text[:100])
