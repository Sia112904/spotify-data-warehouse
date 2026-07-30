import glob
import json
import pandas as pd
from sqlalchemy import create_engine, text

# -----------------------------
# PostgreSQL Connection
# -----------------------------
engine = create_engine(
    
"postgresql+psycopg2://postgres:Mianbao_Pang_2044@localhost:5432/spotify_dw"
)

# -----------------------------
# Read processed JSON
# -----------------------------
files = glob.glob("data/processed/fact_tracks/*.json")

rows = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))

df = pd.DataFrame(rows)

print(f"Loaded {len(df)} tracks")

# -----------------------------
# Build dimension tables
# -----------------------------
artists = (
    df[["artist_name"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

artists["artist_id"] = artists.index + 1

albums = (
    df[["album_name"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

albums["album_id"] = albums.index + 1

dates = pd.DataFrame({
    "full_date": pd.to_datetime(df["played_at"]).dt.date
})

dates = dates.drop_duplicates().reset_index(drop=True)

dates["date_id"] = dates.index + 1
dates["year"] = pd.to_datetime(dates["full_date"]).dt.year
dates["month"] = pd.to_datetime(dates["full_date"]).dt.month
dates["day"] = pd.to_datetime(dates["full_date"]).dt.day

# -----------------------------
# Build fact table
# -----------------------------
fact = df.merge(artists, on="artist_name")
fact = fact.merge(albums, on="album_name")

fact["full_date"] = pd.to_datetime(fact["played_at"]).dt.date

fact = fact.merge(
    dates[["date_id", "full_date"]],
    on="full_date"
)

fact = fact[
    [
        "track_id",
        "track_name",
        "artist_id",
        "album_id",
        "date_id",
    ]
]

# Remove duplicate track IDs
fact = fact.drop_duplicates(
    subset=["track_id"]
)

# -----------------------------
# Load into PostgreSQL
# -----------------------------
with engine.begin() as conn:

    conn.execute(text("DELETE FROM fact_tracks"))
    conn.execute(text("DELETE FROM dim_date"))
    conn.execute(text("DELETE FROM dim_album"))
    conn.execute(text("DELETE FROM dim_artist"))

artists[["artist_id", "artist_name"]].to_sql(
    "dim_artist",
    engine,
    if_exists="append",
    index=False,
)

albums[["album_id", "album_name"]].to_sql(
    "dim_album",
    engine,
    if_exists="append",
    index=False,
)

dates[
    [
        "date_id",
        "full_date",
        "year",
        "month",
        "day",
    ]
].to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False,
)

fact.to_sql(
    "fact_tracks",
    engine,
    if_exists="append",
    index=False,
)

print("\nSuccessfully loaded!\n")
print(f"Artists : {len(artists)}")
print(f"Albums  : {len(albums)}")
print(f"Dates   : {len(dates)}")
print(f"Tracks  : {len(fact)}")
