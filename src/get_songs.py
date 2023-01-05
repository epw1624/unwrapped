import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

def get_user_top_songs(spotify):
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
    songs = spotify.current_user_top_tracks(time_range = timeframe, limit = num_songs)
    return songs

def get_user_playlist_songs(spotify, username):
    # from the api starter code
    # Get all the playlists for this user
    playlists = []
    total = 1
    # The API paginates the results, so we need to iterate
    while len(playlists) < total:
        playlists_response = spotify.user_playlists(username, offset=len(playlists))
        playlists.extend(playlists_response.get('items', []))
        total = playlists_response.get('total')

    # Remove any playlists that we don't own
    playlists = [playlist for playlist in playlists if playlist.get('owner', {}).get('id') == username]

    # List out all of the playlists
    print('Your Playlists')
    for i, playlist in enumerate(playlists):
        print('  {}) {} - {}'.format(i + 1, playlist.get('name'), playlist.get('uri')))

    # Choose a playlist
    playlist_choice = int(input('\nChoose a playlist: '))
    playlist = playlists[playlist_choice - 1]

    # Get the playlist tracks
    tracks = []
    total = 1
    # The API paginates the results, so we need to keep fetching until we have all of the items
    while len(tracks) < total:
        tracks_response = spotify.user_playlist_tracks(playlist.get('owner', {}).get('id'), playlist.get('id'), offset=len(tracks))
        tracks.extend(tracks_response.get('items', []))
        total = tracks_response.get('total')

    # Pull out the actual track objects since they're nested weird
    tracks = [track.get('track') for track in tracks]
    return tracks

#if the user has more than 2000 saved tracks, this function will only take the first 2000
def get_user_saved_songs(spotify, username):
    songs = spotify.current_user_saved_tracks(limit=2000)
    return songs

def get_artist_top_songs(spotify):
    #let the user pick the artist
    name = input("Enter the name of the artist: ")
    search_results = spotify.search(q=name, type='artist')
    artists = search_results[0]['items']
    #now have the user pick from the search results
    for i, artist in enumerate(artists):
        print(i+1 + ") " + artist.get['name'])
    selection = input("Select a number " + str(1)+"-"+str(len(artists)) + "to make your selection")
    chosen_artist = artists[selection - 1]
    #now return this artist's top songs
    songs = spotify.artist_top_tracks(chosen_artist.get['uri'])
    return songs


