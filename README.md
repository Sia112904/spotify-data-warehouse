 Spotify Data Warehouse Project

 Extraction Pipeline

Run the complete pipeline:

bash
python scripts/extract.py

Pipeline Flow:

Spotify API
    ↓
JSON Extraction
    ↓
AWS S3 Raw Layer
