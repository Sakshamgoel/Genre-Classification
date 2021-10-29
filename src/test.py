import json, os, string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('datasets/genre-count-20.json') as f:
    data = json.load(f)

words = {}

main_genres = set(['rock', 'pop', 'metal', 'hip hop', 'folk', 'contemporary christian music'])

for k, v in data.items():
    k = k.lower()
    check = False
    k = k.replace('-', ' ')
    split = k.split()
    for i in range(len(split)):
        w = split[i]
        if (w == 'hip' or w == 'rap'):
            w = 'hip hop'

        if (w == 'contemporary' or w == 'ccm'):
            w = 'contemporary christian music'

        if (w in main_genres):
            if (w not in words):
                words[w] = v
            else:
                words[w] += v
            check = True 
            break
        
    if (not check):
        if (k not in words):
            words[k] = v
        else:
            words[k] += v

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
data_20 = set()
words_20 = set()

for i, (k, v) in enumerate(words.items()):
    if (i == 20):
        break 
    words_20.add(k) 



with open('datasets/genre.json') as f:
    genres = json.load(f)

genres_new = {}

for k, value in genres.items():
    if value is not None:
        for v in value:
            check = False
            v = v.replace('-', ' ').lower()
            split = v.split()
            for i in range(len(split)):
                w = split[i]
                if (w == 'hip' or w == 'rap'):
                    w = 'hip hop'

                if (w == 'contemporary' or w == 'ccm'):
                    w = 'contemporary christian music'
                    
                if (w in words_20):
                    genres_new[k] = w
                    check = True
                    break 
            
            if (not check):
                if (v in words_20):
                    genres_new[k] = w
                    break

with open('datasets/genre_revised.json', 'w') as f:
    json.dump(genres_new, f)

# drop = list(set(genres.keys()).difference(set(genres_new.keys())))

# csvs = ['new_data_2.csv', 'new_data_3.csv']
# df = pd.read_csv('datasets/new_data_1.csv')

# for csv in csvs:
#     df = df.append(pd.read_csv('datasets/' + csv))

# print(len(df))

# for k in drop:
#     df = df[df.artist != k]

# replace = {}

# for i, row in df.iterrows():
#     r = row['lyrics']

#     words = word_tokenize(r)
#     new_words= [word for word in words if word.isalnum()]
#     stop_words = set(stopwords.words('english'))

#     filtered_sentence = [w for w in new_words if not w in stop_words]
#     replace[i] = filtered_sentence

# with open('datasets/lyrics.json', 'w') as f:
#     json.dump(replace, f)