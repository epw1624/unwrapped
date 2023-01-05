from data import (
    get_songs,
    get_danceability,
    get_energy,
    get_key,
    get_loudness,
    get_tempo,
    get_duration,
    get_mode,
    get_time_sig,
    get_speechiness
)
from get_songs import (
    get_user_top_songs,
    get_user_playlist_songs,
    get_user_saved_songs,
    get_artist_top_songs

)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config
import json

def main():
    #create a spotipy object
    API_ID = config('SPOTIPY_CLIENT_ID')
    API_SECRET = config('SPOTIPY_CLIENT_SECRET')
    REDIRECT_URI = config('REDIRECT_URI')
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = API_ID, client_secret = API_SECRET, redirect_uri = REDIRECT_URI, scope=scope))

    #give the user the option to choose their own songs, or songs from a certain artist or genre
    songs_option_chosen = False
    while (not songs_option_chosen):
        print("""What songs would you like to analyze?
        1) Your top songs
        2) Your playlists
        3) Your saved songs
        4) By artist
        5) By genre
        6) Top charts""")
        songs_option_int = input("Enter 1-7 to make your selection: ")
        if int(songs_option_int) == 1:
            songs = get_user_top_songs(sp)
            songs_option_chosen = True
        elif int(songs_option_int) == 2:
            songs = get_user_playlist_songs(sp)
            songs_option_chosen = True
        elif int(songs_option_int) == 3:
            songs = get_user_saved_songs(sp)
            songs_option_chosen = True
        elif int(songs_option_int) == 4:
            songs = get_artist_top_songs(sp)

    #get the time frame and number of songs from the user
    timeframe_chosen = False
    while (not timeframe_chosen):
        print("""Enter the time frame that you wish to analyze: 
        1) Short term
        2) Medium term
        3) Long term""")
        timeframe_int = input("Enter 1, 2 or 3 to make your selection: ")
        if int(timeframe_int) == 1:
            timeframe = 'short_term'
            timeframe_chosen = True
        elif int(timeframe_int) == 2:
            timeframe = 'medium_term'
            timeframe_chosen = True
        elif int(timeframe_int) == 3:
            timeframe = 'long_term'
            timeframe_chosen = True
        else:
            print("Invalid input! Please enter 1, 2 or 3 to make your selection: ")

    #number of songs should be between 1 and 1000 and must be an integer
    number_chosen = False
    while (not number_chosen):
        input_number = input("Enter the number of songs you wish to analyze: ")
        if (input_number.isdigit()):
            num_songs = int(input_number)
            if (num_songs >= 1 and num_songs <= 1000):
                number_chosen = True
        else:
            input_number = input("Invalid input! Please enter an integer between 1 and 1000, inclusive: ")

    #fetch the songs from spotify
    songs = get_songs(num_songs, timeframe, sp)

    #graph the danceability
    get_key(songs, sp)

main()