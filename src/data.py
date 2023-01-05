# Shows the top tracks for a user

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import json
import matplotlib.pyplot as plot
import sys

# API_ID = config('SPOTIPY_CLIENT_ID')
# API_SECRET = config('SPOTIPY_CLIENT_SECRET')
# REDIRECT_URI = config('REDIRECT_URI')

# scope = 'user-top-read'
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = API_ID, client_secret = API_SECRET, redirect_uri = REDIRECT_URI, scope=scope))

# ranges = ['short_term', 'medium_term', 'long_term']

# results = sp.current_user_top_tracks(time_range='medium_term', limit=1)
# for track in results['items']:
#     print(track)
#     print('title is: ' + track['name'])
#     analysis = sp.audio_features(track['uri'])
#     print(json.dumps(analysis, indent=4))
#     print('Key is: ' + str(analysis[0]['key']))
#     #now how to extract the data from the json


# for sp_range in ranges:
#     print("range:", sp_range)
#     results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], '//', item['artists'][0]['name'])
#     print()


#songs is a json object of a user's top songs, such as that obtained by using the get_songs() method
#spotify is an authenticated spotify object
#returns an array with the freuqencies of danceabilities within ranges of 0.1
def get_danceability(songs, spotify):
    #make a 10 element array for the frequency of danceability ratings in the following ranges:
    #0-0.1
    #0.1-0.2 index is danceability times 10 integer divided by 1
    #0.2-0.3
    #etc
    danceabilities = []
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        danceability = features[0]['danceability']
        danceabilities.append(danceability)
    #now plot this data in a histogram
    plot.hist(danceabilities, bins=10)
    plot.title("Danceability")
    plot.show()

def get_energy(songs, spotify):
    energies = []
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        energy = features[0]['energy']
        energies.append(energy)

    plot.hist(energies, bins=10)
    plot.title("Energy")
    plot.show()

def get_key(songs, spotify):
    #pie chart
    keys = [0] * 12
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        key = features[0]['key']
        if (key != -1):
            keys[key] += 1

    labels = 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    plot.pie(keys, labels=labels)
    plot.title("Key")
    plot.show()

def get_loudness(songs, spotify):
    loudnesses = []
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        loudness = features[0]['loudness']
        loudnesses.append(loudness)

    plot.hist(loudnesses, bins=10)
    plot.title("Energy")
    plot.show()

def get_tempo(songs, spotify):
    tempos = []
    #also keep track of max and min tempo
    max = sys.maxsize()
    min = -sys.maxsize()
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        tempo = features[0]['tempo']
        if (tempo > max):
            max = tempo
        elif (tempo < min):
            min = tempo
        tempos.append(tempo)

    num_bins = (max - min) // 5
    plot.hist(tempos, bins=num_bins)
    plot.title("Tempo")
    plot.show()


def get_duration(songs, spotify):
    durations = []
    max = sys.maxsize()
    min = -sys.maxsize()
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        duration = features[0]['duration']
        if (duration > max):
            max = duration
        elif (duration < min):
            min = duration
        durations.append(duration)

    num_bins = (max - min) // 10
    plot.hist(durations, bins=num_bins)
    plot.title("Duration")
    plot.show()

def get_mode(songs, spotify):
    major = 0
    minor = 0
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        mode = features[0]['mode']
        if (int(mode) == '1'):
            major += 1
        else:
            minor += 1
    data = [major, minor]
    labels = ["Major", "Minor"]
    plot.pie(data, labels=labels)
    plot.title("Mode")
    plot.show()

def get_time_sig(songs, spotify):
    #time sig is between 3 and 7 inclusive
    meters = []
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        meter = features[0]['time_signature']
        meters[meter - 3] += 1
    labels = '3', '4', '5', '6', '7'
    plot.pie(meters, labels=labels)
    plot.title("Time Signature")
    plot.show()

def get_speechiness(songs, spotify):
    speechinesses = []
    for track in songs['items']:
        features = spotify.audio_features(track['uri'])
        speechiness = features[0]['speechiness']
        speechinesses.append(speechiness)

    plot.hist(speechinesses, bins=10)
    plot.title("Speechiness")
    plot.show()


