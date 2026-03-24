import requests

API_KEY = "ISI_API_KEY_KAMU"
number = "+83877567966"

url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"

res = requests.get(url).json()
print(res)