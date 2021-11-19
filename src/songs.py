import spotipy, json
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# for each category, get all the playlists and then all the tracks from the playlist 
def get_songs(sp, category_ids, limit=20):
    songs = {}
    songs_set = set()

    # loop through a list of tuples containing category id's and genres 
    # category id's are spotify's way of formatting a genre 
    for c_id, g in category_ids:
        songs[g] = []
        # get a limited number of playlists from 20 <= limit <=  50 
        retries = 0

        while True:
            try:
                sp_playlists = sp.category_playlists(category_id=c_id, limit=limit)['playlists']['items'] 

                for p in sp_playlists:
                    # for each playlist, get the playlists songs
                    
                    sp_tracks = sp.playlist_tracks(playlist_id=p['id'], limit=limit)['items']

                    # for each song, get the name of the song and the artist. If the song 
                    # comes up twice, remove it from it's previous genre. This is because 
                    # the song now has 2 genres associated with it. 
                    for song in sp_tracks:
                        if song['track'] is None:
                            continue
                        
                        if (song['track']['name'] not in songs_set):
                            songs[g].append((song['track']['name'], song['track']['artists'][0]['name']))
                            songs_set.add(song['track']['name'])
                        else:
                            duplicate = (song['track']['name'],  song['track']['artists'][0]['name']) 
                            for k in songs.keys():
                                if (k != g and duplicate in songs[k]):
                                    songs[k].remove(duplicate)
                break  
            except:
                continue
    return songs 

def main():
     # instantiate a spotify instance using your client_id, client_secret, and redirect
    # url from your spotify app     
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='de296bc0ace0461a8d983ca53d171126',
            client_secret='d33960db9b1c48fbb38ed4dfe1b8e8f3', 
            redirect_uri="http://localhost:8888/callback",
            scope=scope))

    genres = ['Rock', 'Pop', 'Hip-Hop', 'Metal', 'Christian & Gospel', 
                  'Folk & Acoustic', 'Dance/Electronic', 'R&B', 'Country']

    category_ids = []
    c_dict = {}
    c_name = set()

    # get a list of (category_id, category)
    sp_categories = sp.categories(limit=50)['categories']['items']
    for c in sp_categories:
        c_dict[c['name']] = c['id']
        c_name.add(c['name'])

    for g in genres:
        if (g in c_name):
            category_ids.append((c_dict[g], g))
        else:
            category_ids.append((g.lower(), g))

    songs = get_songs(sp, category_ids, 50)

    for g in songs:
        print(len(songs[g]))

    with open("songs.json", 'w') as f:
        json.dump(songs, f)

if __name__ == '__main__':
    main()