from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# ---------------------------
# Create Spark Session
# ---------------------------
spark = SparkSession.builder \
    .appName("SpotifyTransformation") \
    .getOrCreate()

# ---------------------------
# Read cleaned data
# ---------------------------

df = spark.read.option("multiline", "true").json("data/raw/tracks_raw.json")

print("Raw Data")
df.show(5)

# ---------------------------
# DIM ARTIST
# ---------------------------
dim_artist = (
    df.select("artist_name")
      .distinct()
      .withColumnRenamed("artist_name", "artist")
)

# ---------------------------
# DIM ALBUM
# ---------------------------
dim_album = (
    df.select("album_name")
      .distinct()
      .withColumnRenamed("album_name", "album")
)

# ---------------------------
# FACT TRACKS
# ---------------------------
fact_tracks = (
    df.select(
        "track_id",
        "track_name",
        "artist_name",
        "album_name",
        "played_at"
    )
)

# ---------------------------
# Write outputs
# ---------------------------
dim_artist.write.mode("overwrite").json(
    "data/processed/dim_artist"
)

dim_album.write.mode("overwrite").json(
    "data/processed/dim_album"
)

fact_tracks.write.mode("overwrite").json(
    "data/processed/fact_tracks"
)

print("Transformation Complete!")

spark.stop()
