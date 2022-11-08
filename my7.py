import requests

r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(r.text)


r = requests.put('https://httpbin.org/put', data = {'key':'value'})
print(r.text)

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)
