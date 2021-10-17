# We now save one genre per artist depending on the genre-count we created
# We save this information in a file called: artist-to-genre.json

import json


def main():

	file1 = open('genre-count.json')
	genre_count = json.load(file1)

	file2 = open('genre.json')
	artist_to_genres = json.load(file2)

	artist_to_genre = dict()

	for key, value in artist_to_genres.items():


		if value == None:
			continue

		temp_dict = dict()

		for genre in value:
			temp_dict[genre] = genre_count[genre]

		sorted_dict = {k: v for k, v in sorted(temp_dict.items(), key = lambda item: item[1], reverse = True)}

		artist_to_genre[key] = list(sorted_dict.keys())[0]


	with open('artist-to-genre.json', 'w') as outfile:
		json.dump(artist_to_genre, outfile)


main()