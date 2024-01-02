# tests for data collection and API-related functions

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import webapp.config as config

#create a spotipy object and define current user
CLIENT_ID = config.SPOTIPY_CLIENT_ID
CLIENT_SECRET = config.SPOTIPY_CLIENT_SECRET
REDIRECT_URI = config.REDIRECT_URI
scope = ['user-library-read', 'user-top-read']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, redirect_uri = REDIRECT_URI, scope=scope))

# tests for each song-fetching method
import get_songs

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

# tests for each attribute analysis method
import data

# data set for testing is the album "Reflections of a Floating World" by Elder
album = sp.search(q="Reflections of a Floating World", type='album', limit=1)['albums']['items'][0]
songs = sp.album_tracks(album['uri'])
song_uris = []
for song in songs['items']:
    song_uris.append(song['uri'])

def test_get_danceability():
    ax = data.get_danceability(sp, song_uris)[1]
    assert ax.get_title() == "Danceability"

def test_get_energy():
    ax = data.get_energy(sp, song_uris)[1]
    assert ax.get_title() == "Energy"

def test_get_key():
    ax = data.get_key(sp, song_uris)[1]
    assert ax.get_title() == "Key"

def test_get_loudness():
    ax = data.get_loudness(sp, song_uris)[1]
    assert ax.get_title() == "Loudness"

def test_get_tempo():
    ax = data.get_tempo(sp, song_uris)[1]
    assert ax.get_title() == "Tempo"

def test_get_duration():
    ax = data.get_duration(sp, song_uris)[1]
    assert ax.get_title() == "Duration"

def test_get_mode():
    ax = data.get_mode(sp, song_uris)[1]
    assert ax.get_title() == "Mode"

def test_get_time_sig():
    ax = data.get_time_sig(sp, song_uris)[1]
    assert ax.get_title() == "Time Signature"

def test_get_speechiness():
    ax = data.get_speechiness(sp, song_uris)[1]
    assert ax.get_title() == "Speechiness"


