from pymystem3 import Mystem
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import gensim
#import word2vec
import pandas as pd
import re



df = pd.read_csv('C:\\Users\\karen\\Downloads\\test_data.csv', sep=';', encoding='utf-8')
df = df.dropna()
print(df)

file = open('C:\\Users\\karen\\Downloads\\test_data1.txt','w', encoding='utf-8')

for text in df['dlg_id,line_n,role,text']:
    text = text.lower()

    res = re.findall('[а-яё]+', text)
    for i in res:
        file.write(i)
        file.write(' ')
    file.write('.')
file.close()

file = open('C:\\Users\\karen\\Downloads\\test_data1.txt', 'r', encoding='utf-8')
text = file.read()
posts = text.split('.')

m = Mystem()

with open('C:\\Users\\karen\\Downloads\\test_data1_lemma.txt', 'w', encoding='utf-8') as output_file:
    for post in posts:
        output_file.write("".join(m.lemmatize(post)))

