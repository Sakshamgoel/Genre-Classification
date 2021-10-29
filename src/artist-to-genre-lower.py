# Python file to convert artist-to-genre to lower case
# Saves it as artist-to-unique-genre.json only (file override)

import json

def main():
	file1 = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-to-genre.json')
	artist_to_genre = json.load(file1)

	new_dict = dict()

	for artist, genre in artist_to_genre.items():

		new_dict[artist.lower()] = genre.lower()

	with open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-to-unique-genre.json', 'w') as outfile:
		json.dump(new_dict, outfile)

main()