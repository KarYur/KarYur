import requests


file = open(r"C:\Users\karen\Downloads\qwerty.txt")
f = file.read().strip()
print(f)
r = requests.get(f)
r = r.text.splitlines()
print(len(r))
file = open(r"C:\Users\karen\Downloads\reply_3378_2.txt", 'w')
file.write(str(len(r)))
