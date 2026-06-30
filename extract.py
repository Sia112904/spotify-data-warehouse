import logging
import subprocess

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

subprocess.run(
    ["python", "scripts/extract_tracks.py"],
    check=True
)

logging.info("Extraction complete")

subprocess.run(
    ["python", "scripts/upload_to_s3.py"],
    check=True
)

logging.info("Upload complete")
logging.info("Pipeline finished")
