import requests

r = requests.get("http://example.com")
print(r.text)

url = "http://example.com"
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params = par)
print(r.url)

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies = cookies)
print(r.text)
print(r.cookies['example_cookie_name'])
