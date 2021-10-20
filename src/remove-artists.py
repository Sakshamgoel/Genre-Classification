# Code to remove artists and their songs that are without a genre
# Returns new data that has none of those artists


import json
import pandas as pd

def main():

	file1 = open('artist-to-genre.json')

	artist_genre = json.load(file1)

	artist_list = list(artist_genre.keys())

	x = 0
	for artist in artist_list:
		#print(artist)

		x += 1

	print(x)

	data_1 = pd.read_csv('data1.csv')
	data_1.drop(data_1.columns[[0]], axis = 1, inplace = True)

	data_2 = pd.read_csv('data2.csv')
	data_2.drop(data_2.columns[[0]], axis = 1, inplace = True)

	data_3 = pd.read_csv('data3.csv')
	data_3.drop(data_3.columns[[0]], axis = 1, inplace = True)

	drop_list_1 = []
	drop_list_2 = []
	drop_list_3 = []

	for ind in data_1.index:
		if data_1['artist'][ind] not in artist_list:
			drop_list_1.append(ind)

	for ind in data_2.index:
		if data_2['artist'][ind] not in artist_list:
			drop_list_2.append(ind)

	for ind in data_3.index:
		if data_3['artist'][ind] not in artist_list:
			drop_list_3.append(ind)


	data_1.drop(drop_list_1, axis = 0, inplace = True)
	data_2.drop(drop_list_2, axis = 0, inplace = True)
	data_3.drop(drop_list_3, axis = 0, inplace = True)

	data_1.to_csv('new_data_1.csv')
	data_2.to_csv('new_data_2.csv')
	data_3.to_csv('new_data_3.csv')

	print(data_1.describe)
	print(data_2.describe)
	print(data_3.describe)
	

main()