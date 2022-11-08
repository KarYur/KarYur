import requests

with open(r"C:\\Users\\karen\\Downloads\\dataset_3378_2.txt") as file:
    for ssilka in file:
        ssilka = ssilka.strip()
r = requests.get(ssilka)
f = r.text.splitlines()
print(f)
print(len(f))
with open(r"C:\\Users\\karen\\Downloads\\dataset_3378_2.txt", 'w') as file:
    file.write(str(len(f)))
