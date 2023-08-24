# Shows the top tracks for a user

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import json
import matplotlib.pyplot as plot
import sys
import math

VERY_LARGE_INT = 2**63 - 1

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
def get_danceability(spotify, songs):
    #make a 10 element array for the frequency of danceability ratings in the following ranges:
    #0-0.1
    #0.1-0.2 index is danceability times 10 integer divided by 1
    #0.2-0.3
    #etc
    danceabilities = []
    for track in songs:
        features = spotify.audio_features(track)
        danceability = features[0]['danceability']
        danceabilities.append(danceability)
    
    fig, ax = plot.subplots()
    ax.hist(danceabilities, bins=10)
    ax.set_title("Danceability")

    return fig, ax

def get_energy(spotify, songs):
    energies = []
    for track in songs:
        features = spotify.audio_features(track)
        energy = features[0]['energy']
        energies.append(energy)

    fig, ax = plot.subplots()
    ax.hist(energies, bins=10)
    ax.set_title("Energy")

    return fig, ax

def get_key(spotify, songs):
    #pie chart
    keys = [0] * 12
    for track in songs:
        features = spotify.audio_features(track)
        key = features[0]['key']
        if (key != -1):
            keys[key] += 1

    labels = 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    fig, ax = plot.subplots()
    ax.pie(keys, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    ax.set_title("Key")
    
    return fig, ax

def get_loudness(spotify, songs):
    loudnesses = []
    for track in songs:
        features = spotify.audio_features(track)
        loudness = features[0]['loudness']
        loudnesses.append(loudness)

    fig, ax = plot.subplots()
    ax.hist(loudnesses, bins=10)
    ax.set_title("Loudness")

    return fig, ax

def get_tempo(spotify, songs):
    tempos = []
    #also keep track of max and min tempo
    max = -VERY_LARGE_INT
    min = VERY_LARGE_INT
    for track in songs:
        features = spotify.audio_features(track)
        tempo = features[0]['tempo']
        if (tempo > max):
            max = tempo
        elif (tempo < min):
            min = tempo
        tempos.append(tempo)

    num_bins = math.floor((max - min) / 5)
    
    fig, ax = plot.subplots()
    ax.hist(tempos, bins=num_bins)
    ax.set_title("Tempo")

    return fig, ax


def get_duration(spotify, songs):
    durations = []
    max = -VERY_LARGE_INT
    min = VERY_LARGE_INT
    for track in songs:
        features = spotify.audio_features(track)
        duration = features[0]['duration_ms'] / 1000 #puts it from ms into s
        if (duration > max):
            max = duration
        elif (duration < min):
            min = duration
        durations.append(duration)

    num_bins = math.floor((max - min) / 10)
    
    fig, ax = plot.subplots()
    ax.hist(durations, bins=num_bins)
    ax.set_title("Duration")

    return fig, ax

def get_mode(spotify, songs):
    major = 0
    minor = 0
    for track in songs:
        features = spotify.audio_features(track)
        mode = features[0]['mode']
        if (int(mode) == '1'):
            major += 1
        else:
            minor += 1
    data = [major, minor]
    labels = ["Major", "Minor"]
    
    fig, ax = plot.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    ax.set_title("Mode")
    
    return fig, ax

def get_time_sig(spotify, songs):
    #time sig is between 3 and 7 inclusive
    meters = [0] * 5
    for track in songs:
        features = spotify.audio_features(track)
        meter = features[0]['time_signature']
        meters[meter - 3] += 1
    labels = '3', '4', '5', '6', '7'
    
    fig, ax = plot.subplots()
    ax.pie(meters, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    ax.set_title("Time Signature")
    
    return fig, ax

def get_speechiness(spotify, songs):
    speechinesses = []
    for track in songs:
        features = spotify.audio_features(track)
        speechiness = features[0]['speechiness']
        speechinesses.append(speechiness)

    fig, ax = plot.subplots()
    ax.hist(speechinesses, bins=10)
    ax.set_title("Speechiness")

    return fig, ax


