import spotipy

def get_user_playlists(sp):
    playlists = []
    total = 1
    # The API paginates the results, so we need to iterate
    while len(playlists) < total:
        # playlists_response = sp.user_playlists(USERNAME, offset=len(playlists))
        playlists_response = sp.current_user_playlists(offset=len(playlists))
        playlists.extend(playlists_response.get('items', []))
        total = playlists_response.get('total')

    return playlists