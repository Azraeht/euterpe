import typer
import requests
from rich import print

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

app = typer.Typer()

test_uri = "spotify:track:3v9GhZEIMWPJcWH0tbbSyT"  # Cancre - Vol de nuit
test_device = "Euterpe"


def get_account():
    r = requests.get("http://localhost:8000/accounts")
    accounts = r.json()
    return accounts[0]


@app.command()
def run():
    print("[blue]Starting server...[/blue]")
    account = get_account()
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=account["client_id"],
            client_secret=account["client_secret"],
            redirect_uri="http://localhost:8000/callback",
            scope=scope,
            open_browser=False,
        )
    )
    device = [d for d in sp.devices()["devices"] if d["name"] == test_device][0]
    print(f"[blue]Device:[/blue] {device['name']}")
    track = sp.track(test_uri)
    print(f"[blue]Currently playing:[/blue] {track['name']} by {track['artists'][0]['name']}")
    # Change track
    sp.start_playback(uris=[test_uri], device_id=device["id"])


if __name__ == "__main__":
    app()
