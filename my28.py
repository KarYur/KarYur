import csv
from pymystem3 import Mystem
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import gensim
#import word2vec
import pandas as pd
import re

manager_text = []
with open('C:\\Users\\karen\\Downloads\\test_data.csv','r', encoding='utf-8') as df:
    reader = csv.reader(df)
    for row in reader:
        if 'manager' in row:
            manager_text += row

file = open('C:\\Users\\karen\\Downloads\\test_data_manager.txt','w', encoding='utf-8')

for text in manager_text:
    text = text.lower()

    res = re.findall('[а-яё]+', text)
    for i in res:
        file.write(i)
        file.write(' ')
    file.write('.')
file.close()

file = open('C:\\Users\\karen\\Downloads\\test_data_manager.txt', 'r', encoding='utf-8')
text = file.read()
posts = text.split('....')


m = Mystem()

with open('C:\\Users\\karen\\Downloads\\test_data_manager_lemma.txt', 'w', encoding='utf-8') as output_file:
    for post in posts:
        output_file.write("".join(m.lemmatize(post)))