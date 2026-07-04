import requests



r = requests.get("https://coreyms.com", timeout=10)
print(r.status_code)
print(r.ok)