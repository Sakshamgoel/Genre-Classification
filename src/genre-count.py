# Python code to get count of songs with a particular genre
# We then save it into a json file - 'genre-count.json'

import json
import pandas as pd


def main():
	
	genre_count = dict()

	file1 = open('artist-count.json')
	file2 = open('genre.json')

	artist_count = json.load(file1)
	artist_to_genre = json.load(file2)

	for key, value in artist_to_genre.items():
		if value == None:
			continue

		for item in value:
			if item in genre_count:
				genre_count[item] += artist_count[key]
			else:
				genre_count[item] = artist_count[key]


	with open('genre-count.json', 'w') as outfile:
		json.dump(genre_count, outfile)


main()
