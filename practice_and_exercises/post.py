import requests

payload = {"firstName" : "PEPE", "lastName" : "PECASPICAPAPAS"}

r = requests.post("https://httpbin.org/post", data = payload)

print(r.text)
print(r.content)
print("Status code: ", r.status_code)