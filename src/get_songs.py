import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

def get_user_top_songs(spotify, timeframe, num_songs):
    """
    Fetches a dict of the users <num_songs> top songs over short, medium or long term
    timeframe: string, must be 'short_term', 'medium_term' or 'long_term'
    num_songs: the number of songs to analyze, must be between 1 and 1000, inclusive
    """
    songs = spotify.current_user_top_tracks(time_range=timeframe, limit=num_songs)
    print(songs)
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
    #any number under 2000
    songs = spotify.current_user_saved_tracks(limit=2000)
    return songs

def get_artist_top_songs(spotify):
    #this will take 10 songs no matter what
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

def get_songs_from_genre(spotify):
    #let the user select from a list of genres and return 100 songs from that genre
    #uses the recommendations function
    genre_options = spotify.recommendation_genre_seeds()
    print("Available genres:")
    for i, genre in enumerate(genre_options):
        print(str(i+1) + ")" + genre)
    selection = input("Enter 1-" + len(genre_options)+" to make your selection")
    genre_list = [genre]
    songs = spotify.recommendations(seed_genres=genre_list, limit=100)
    return songs



