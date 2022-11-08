import os

# nshvac direktoriayic sax filerix vori mej ka _cleanup jnjuma texe dnuma menak ira anun j-n
os.chdir(r"C:\\Users\\karen\\Downloads\\")
for i in os.listdir(path="."):
    if i.count('_cleanup'):
        j = i.replace('_cleanup','')
        print(i)
        k = r"C:\\Users\\karen\\Downloads\\" + str(i)
        os.renames(str(k), str(j))