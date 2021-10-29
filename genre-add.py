# Python code to add genres to the data frame of the data

import json
import pandas as pd


def main():
	
	data1 = pd.read_csv('data1.csv')
	data1.drop(data1.columns[[0]], axis = 1, inplace = True)

	data2 = pd.read_csv('data2.csv')
	data2.drop(data2.columns[[0]], axis = 1, inplace = True)

	print(data2.describe)

	data3 = pd.read_csv('data3.csv')
	data3.drop(data3.columns[[0]], axis = 1, inplace = True)

	artist_count_dict = dict()

	for ind in data1.index:
		if data1['artist'][ind] in artist_count_dict:
			artist_count_dict[data1['artist'][ind]] += 1
		else:
			artist_count_dict[data1['artist'][ind]] = 0

	for ind in data2.index:
		if data2['artist'][ind] in artist_count_dict:
			artist_count_dict[data2['artist'][ind]] += 1
		else:
			artist_count_dict[data2['artist'][ind]] = 0

	for ind in data3.index:
		if data3['artist'][ind] in artist_count_dict:
			artist_count_dict[data3['artist'][ind]] += 1
		else:
			artist_count_dict[data3['artist'][ind]] = 0

	with open('artist-count.json', 'w') as outfile:
		json.dump(artist_count_dict, outfile)



main()
