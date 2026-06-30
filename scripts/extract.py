import logging
import subprocess

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting Spotify extraction pipeline")

# Step 1: Extract data from Spotify
logging.info("Running extract_tracks.py")
subprocess.run(["python", "scripts/extract_tracks.py"])

# Step 2: Upload to S3
logging.info("Running upload_to_s3.py")
subprocess.run(["python", "scripts/upload_to_s3.py"])

logging.info("Pipeline completed successfully")
