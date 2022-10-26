import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class ApiManager:
    def __init__(self):
        self.id = "5b691f19a3544c318839658870ec248c"
        self.secret = "31b8c85485c04f1a93e7ef31402d6f93"
        self.search_url = "https://api.spotify.com/v1"
        self.redirect_uri = "http://example.com"
        self.sp = spotipy.oauth2.SpotifyOAuth(
            client_id=self.id,
            client_secret=self.secret,
            redirect_uri=self.redirect_uri,
            scope="playlist-modify-public"
        )
        self.token = self.get_token()
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.id, client_secret=self.secret))
        self.user_id = self.client.current_user()["id"]

    def get_token(self):
        return self.sp.get_access_token()["access_token"]

    def search_musics_id(self, music_name):
        result = self.client.search(q=music_name, limit=3)
        return result["tracks"]["items"][0]["id"]

    def create_playlist(self, playlist_name):
        self.client.user_playlist_create(user=self.user_id, name=playlist_name)
        return self.client.current_user_playlists()["items"][0]["id"]

    def add_musics_into_playlist(self, track_ids, playlist_id):
        self.client.user_playlist_add_tracks(
            user=self.user_id,
            playlist_id=playlist_id,
            tracks=track_ids
        )