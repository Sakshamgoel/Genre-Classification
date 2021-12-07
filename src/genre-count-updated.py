# Code to create genre-count based on artist-count.json and artist-to-genre.json
# Output file is genre-count.json, and is sorted in reverse order based on count
# Everything is in the reverse order for better results and overlap prevention

import json


def main():

	file1 = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-to-unique-genre.json')
	artist_to_genre = json.load(file1)
	file2 = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-count.json')
	artist_count = json.load(file2)

	genre_count = dict()

	for artist, genre in artist_to_genre.items():
		if genre in genre_count:
			genre_count[genre] += artist_count[artist]
		else:
			genre_count[genre] = artist_count[artist]

	new_dict = {k: v for k, v in sorted(genre_count.items(), key = lambda item: item[1], reverse = True)}

	with open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\genre-count.json', 'w') as outfile:
		json.dump(new_dict, outfile)





main()