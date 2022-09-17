from keys import client_id, client_secret
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))


def playlist_details(url):
    playlist_id = f'spotify:playlist:{url}'
    results = sp.playlist(playlist_id)
    for key, value in results.items():
        if key == "name":
            name = value
        if key == "owner":

            for key, value in value.items():
                if key == "display_name":
                    owner = value
        if key == "description":
            description = value

    return [name, owner, description]


def check_description(url):
    playlist_id = f'spotify:playlist:{url}'
    results = sp.playlist(playlist_id)
    for key, value in results.items():
        if key == "description":
            description = value

    return description
