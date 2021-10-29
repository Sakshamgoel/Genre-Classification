# File to convert artist names to lowercase in artist-count.json
# File override (saved as artist-count.json)

import json

def main():
	file = open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-count.json')
	artist_count = json.load(file)


	new_dict = dict()

	for artist, number in artist_count.items():
		new_dict[artist.lower()] = number

	with open(r'C:\Users\goels\Desktop\fall 2021\COMP 5970\final project\github\datasets\artist-count.json', 'w') as outfile:
		json.dump(new_dict, outfile)




main()