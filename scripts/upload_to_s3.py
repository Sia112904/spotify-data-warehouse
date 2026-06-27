import boto3

s3 = boto3.client("s3")

bucket_name = "spotify-data-lake-shriya"

file_name = "data/raw/tracks_raw.json"

s3.upload_file(
    file_name,
    bucket_name,
    "raw/recent_tracks.json"
)

print("Upload complete!")
