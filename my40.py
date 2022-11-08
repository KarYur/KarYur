import os

# nshvac direktoriayic sax filerix vori mej ka _cleanup jnjuma texe dnuma menak ira anun j-n
os.chdir(r"C:\\Users\\karen\\Desktop\\New folder (2)")
for i in os.listdir(path="."):
    if i.count('(1)'):
        j = i.replace('(1)','')
        print(i)
        print(j)
        os.renames(str(i), str(j))