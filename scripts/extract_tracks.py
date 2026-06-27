import boto3
import os
import json
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Clean OAuth setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-recently-played"
))

# Use a SIMPLE endpoint (no browse, no playlists)
results = sp.current_user_recently_played(limit=20)

tracks = []

for item in results["items"]:
    track = item["track"]

    tracks.append({
        "track_id": track["id"],
        "track_name": track["name"],
        "artist_name": track["artists"][0]["name"],
        "album_name": track["album"]["name"],
        "played_at": item["played_at"]
    })

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/tracks_raw.json", "w") as f:
    json.dump(tracks, f, indent=4)

print(f"Saved {len(tracks)} recently played tracks")

s3 = boto3.client("s3")

s3.upload_file(
    "data/raw/tracks_raw.json",
    "spotify-data-lake-shriya",
    "raw/tracks_raw.json"
)

print("Uploaded to S3")
