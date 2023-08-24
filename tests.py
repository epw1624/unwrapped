# tests for data collection and API-related functions

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

#create a spotipy object and define current user
API_ID = config('SPOTIPY_CLIENT_ID')
API_SECRET = config('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = config('REDIRECT_URI')
USERNAME = config('USERNAME')
scope = ['user-library-read', 'user-top-read']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = API_ID, client_secret = API_SECRET, redirect_uri = REDIRECT_URI, scope=scope))

# tests for each song-fetching method
from src import get_songs

def test_get_user_top_songs():
    num_songs = [0, 1, 50]
    timeframes = ["short_term", "medium_term", "long_term"]
    for n in num_songs:
        for time in timeframes:
            songs = get_songs.get_user_top_songs(sp, time, n)
            assert len(songs) == n, f"Expected {n} songs but got {len(songs)} songs"

def test_get_playlist_songs():
    # using a public playlist "Rock Classics"
    PLAYLIST_LEN = 200 
    search_results = sp.search(q='Rock Classics', type='playlist')
    playlist = search_results['playlists']['items'][0]

    songs = get_songs.get_playlist_songs(sp, playlist)

    assert(len(songs) == PLAYLIST_LEN)

def test_get_user_saved_songs():
    songs = get_songs.get_user_saved_songs(sp)
    assert len(songs) > 0

def test_get_artist_top_songs():
    result = sp.search(q="Nazca Space Fox", limit=1, type='artist')
    artist = result['artists']['items'][0]
    top_songs = get_songs.get_artist_top_songs(sp, artist)
    assert len(top_songs) == 10
    song = sp.track(top_songs[0])
    assert song['artists'][0]['uri'] == artist['uri']