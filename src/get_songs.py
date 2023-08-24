import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

def get_user_top_songs(spotify, timeframe, num_songs):
    """
    Fetches the users top <num_songs> top songs over short, medium or long term
    timeframe: string, must be 'short_term', 'medium_term' or 'long_term'
    num_songs: the number of songs to analyze, must be between 1 and 1000, inclusive
    returns a list of song uris
    """
    response = spotify.current_user_top_tracks(time_range=timeframe, limit=num_songs)
    songs = []
    for song in response['items']:
        songs.append(song['uri'])
    return songs

def get_playlist_songs(spotify, playlist):
    """
    returns the songs in the given playlist
    return value is a list of the song uris for all songs in the playlist
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
    tracks = [track.get('track')['uri'] for track in tracks]
    return tracks

def get_user_saved_songs(spotify):
    result = spotify.current_user_saved_tracks(limit=50)['items']
    songs = []
    for song in result:
        songs.append(song['track']['uri'])
    return songs

def get_artist_top_songs(spotify, artist):
    result = spotify.artist_top_tracks(artist['uri'])
    songs = []
    for song in result['tracks']:
        songs.append(song['uri'])
    return songs



