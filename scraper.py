from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import json
from os import listdir
from os.path import isfile, join
import functools
from googlesearch import search
import csv

# get the first wikipedia link from google for the artist/band 
def getWikipediaLink(query: str) -> str:
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if ('wikipedia' in j):
            return j

# get the genres from the wikipedia page 
def getGenre(soup) -> list:
    table = soup.find('table', {"class": "infobox vcard plainlist"})
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    genres = []
    for tr in trs:
        if tr.find('th', text="Genres"):
            for a in tr.findChildren('a'):
                if ('[' not in a.text):
                    genres.append(a.text)
            
            break
    return genres

# get the wikipedia article's html 
def getSoup(name: str):
    url = getWikipediaLink(name + " artist")
    if url:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        return soup
    return None

# get the genres for all the artists in the list
def getGenres(artists: list) -> dict:
    genres = {}
    for i in range(len(artists)):
        artist = artists[i]
        exc = 0
        try:
            genre = getGenre(getSoup(artist))
        except:
            genre = []

        genres[artists[i]] = genre if len(genre) > 0 else None
    return genres

def rreplace(s: str, old: str, new: str) -> str:
    return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]

# print(getGenres(["Nirvana", "Grandson", "Bring Me the Horizon"]))
def main():
    files = [f for f in listdir("datasets/csv") if isfile(join("datasets/csv", f)) and f.endswith('.csv')]
    files.sort()
    data_frames = []

    for f in files:
        rows = []
        with open("datasets/csv/" + f, 'r') as file:
            csvreader = csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row[:5])

        df = pd.DataFrame(rows, columns = ["ARTIST_NAME","ARTIST_URL","SONG_NAME","SONG_URL","LYRICS"])
        df = df.drop(["ARTIST_URL", "SONG_URL"], axis=1)
        data_frames.append(df)

    for i in range(len(data_frames)):
        if i != 0:
            artists = list(set(data_frames[i]['ARTIST_NAME'].tolist()))
            artists_str = [str(a) for a in artists]
            artists_str.sort()
            genres = getGenres(artists_str)
            
            file = files[i].replace("csv", "json")

            file = rreplace(file, 'lyrics', 'genres')

            print(file)

            with open("datasets/json/" + file, 'w') as fp:
                json.dump(genres, fp)

if __name__ == '__main__':
    main()