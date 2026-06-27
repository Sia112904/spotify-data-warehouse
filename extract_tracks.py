import os
import json
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# -----------------------------
# USER AUTH (FIX FOR 401 ERROR)
# -----------------------------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-read-private playlist-read-collaborative"
))

# Use a stable public playlist (still works with user auth)
playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # Today's Top Hits

results = sp.playlist_tracks(playlist_id, limit=50)

tracks = []

for item in results["items"]:
    track = item["track"]

    if track is None:
        continue

    tracks.append({
        "track_id": track["id"],
        "track_name": track["name"],
        "artist_name": track["artists"][0]["name"],
        "album_name": track["album"]["name"],
        "popularity": track["popularity"],
        "duration_ms": track["duration_ms"],
        "release_date": track["album"]["release_date"]
    })

# Save raw data
os.makedirs("data/raw", exist_ok=True)

with open("data/raw/tracks_raw.json", "w") as f:
    json.dump(tracks, f, indent=4)

print(f"Saved {len(tracks)} tracks to data/raw/tracks_raw.json")
