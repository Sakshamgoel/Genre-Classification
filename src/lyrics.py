import json
from pprint import pprint
from lyricsgenius import Genius
import azapi
from typing import Dict, List, Tuple

def get_lyrics_genius(genius, songs: Dict[str, List[str]]):
    songs_w_lyrics = {}
    songs_not_found = {}
    count = 0

    for g in songs:
        songs_w_lyrics[g] = []
        songs_not_found[g] = []
        for song_name, song_artist in songs[g]:
            while (True):
                try:
                    song = genius.search_song(song_name, song_artist)
                    if song is None:
                        head, _, _ = song_name.partition('(')
                        song = genius.search_song(head, song_artist)
                        if song is None:
                            head, _, _ = head.partition('-')
                            song = genius.search_song(head, song_artist)
                    if song is not None and song.artist == song_artist:
                        songs_w_lyrics[g].append((song_name, song_artist, song.lyrics))
                    else:
                        songs_not_found[g].append((song_name, song_artist));
                    break 
                except:
                    count += 1
                    print("Timeout:", count)
                    continue 

        print(len(songs_not_found[g]))
    return songs_not_found, songs_w_lyrics

def main():
    # instantiate a genius instance using you access token from Genius 
    token = None
    genius = Genius(token)
    genius.verbose = False # Turn off status messages
    genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching

    with open('songs.json', 'r') as f:
        songs = json.load(f)

    songs_w_lyrics = get_lyrics_genius(genius, songs)

    with open("songs_w_lyrics.json", 'w') as f:
        json.dump(songs_w_lyrics, f)

    with open("songs_without_lyrics.json", 'w') as f:
        json.dump(songs_not_found, f)

if __name__ == '__main__':
    main()
