import os

r = os.path.join(r"C:\\Users\\karen\\Downloads\\dataset_3378_2.txt")

print(r)

with open(r"C:\\Users\\karen\\Downloads\\dataset_3378_2.txt", 'w') as inf:
    inf.write("FOOBAR3")