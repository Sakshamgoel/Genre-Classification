# Creates a new json file with unique-genre-count based on 'artist-to-genre.json'


import json
import pandas as pd

def main():
	file1 = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-to-genre.json')
	file2 = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-count.json')

	artist_to_genre = json.load(file1)
	artist_count = json.load(file2)

	unique_count = dict()

	for artist, genre in artist_to_genre.items():
		if genre in unique_count:
			unique_count[genre] += artist_count[artist]
		else:
			unique_count[genre] = artist_count[artist]


	with open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\unique-genre-count.json', 'w') as outfile:
		json.dump(unique_count, outfile)


main()