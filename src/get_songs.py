import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

def get_user_top_songs(spotify, timeframe, num_songs):
    """
    Fetches a dict of the users <num_songs> top songs over short, medium or long term
    timeframe: string, must be 'short_term', 'medium_term' or 'long_term'
    num_songs: the number of songs to analyze, must be between 1 and 1000, inclusive
    """
    response = spotify.current_user_top_tracks(time_range=timeframe, limit=num_songs)
    songs = []
    for song in response['items']:
        songs.append(song)
    return songs

# def get_user_playlist_songs(spotify, username):
#     # from the api starter code
#     # Get all the playlists for this user
#     playlists = []
#     total = 1
#     # The API paginates the results, so we need to iterate
#     while len(playlists) < total:
#         playlists_response = spotify.user_playlists(username, offset=len(playlists))
#         playlists.extend(playlists_response.get('items', []))
#         total = playlists_response.get('total')

#     # Remove any playlists that we don't own
#     playlists = [playlist for playlist in playlists if playlist.get('owner', {}).get('id') == username]

#     # List out all of the playlists
#     print('Your Playlists')
#     for i, playlist in enumerate(playlists):
#         print('  {}) {} - {}'.format(i + 1, playlist.get('name'), playlist.get('uri')))

#     # Choose a playlist
#     playlist_choice = int(input('\nChoose a playlist: '))
#     playlist = playlists[playlist_choice - 1]

#     # Get the playlist tracks
#     tracks = []
#     total = 1
#     # The API paginates the results, so we need to keep fetching until we have all of the items
#     while len(tracks) < total:
#         tracks_response = spotify.user_playlist_tracks(playlist.get('owner', {}).get('id'), playlist.get('id'), offset=len(tracks))
#         tracks.extend(tracks_response.get('items', []))
#         total = tracks_response.get('total')

#     # Pull out the actual track objects since they're nested weird
#     tracks = [track.get('track') for track in tracks]
#     return tracks

def get_playlist_songs(spotify, playlist):
    """
    returns the songs in the given playlist
    """
    # Get the playlist tracks
    tracks = []
    total = 1
    # The API paginates the results, so we need to keep fetching until we have all of the items
    while len(tracks) < total:
        tracks_response = spotify.playlist_tracks(playlist.get('id'))
        tracks.extend(tracks_response.get('items', []))
        total = tracks_response.get('total')

    # Pull out the actual track objects since they're nested weird
    tracks = [track.get('track') for track in tracks]
    return tracks

def get_user_saved_songs(spotify):
    result = spotify.current_user_saved_tracks(limit=50)['items']
    songs = []
    for song in result:
        songs.append(song['track'])
    return songs

def get_artist_top_songs(spotify, artist):
    result = spotify.artist_top_tracks(artist['uri'])
    songs = []
    for song in result['tracks']:
        songs.append(song['uri'])
    return songs



