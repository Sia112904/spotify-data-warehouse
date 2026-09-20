# Spotify Analytics Platform

An end-to-end data engineering and analytics project that collects Spotify
data through an API, stores raw data in Amazon S3, transforms the data
using PySpark, loads it into a PostgreSQL data warehouse, and visualizes
the resulting star schema in Tableau.

---

## Project Overview

The **Spotify Analytics Platform** demonstrates a complete data
engineering workflow from data ingestion to analytics and visualization.

The pipeline processes Spotify track data through the following stages:

1. Extract data from the Spotify Web API
2. Store raw data in Amazon S3
3. Clean and transform the data using PySpark
4. Load structured data into PostgreSQL
5. Organize the warehouse using a star schema
6. Analyze the data using SQL
7. Export warehouse tables for visualization
8. Build an interactive Tableau dashboard

The project demonstrates practical experience with:

- REST API integration
- Data ingestion
- Cloud object storage
- ETL pipelines
- PySpark data processing
- PostgreSQL data warehousing
- Dimensional modeling
- Analytical SQL
- Data visualization
- Git and GitHub

---

## Architecture

The overall pipeline follows this architecture:

```text
flowchart TD
    A[Spotify Web API] --> B[AWS S3]
    B --> C[PySpark]
    C --> D[PostgreSQL]
    D --> E[Tableau]
```

Pipeline Flow

Spotify Web API → AWS S3 → PySpark → PostgreSQL → Tableau

Architecture Components
Component	Purpose
Spotify Web API	Source of Spotify track and metadata information
AWS S3	Stores raw ingested data
PySpark	Cleans and transforms raw data
PostgreSQL	Stores the structured data warehouse
SQL	Performs analytical queries
Tableau	Visualizes warehouse data
Data Model

The PostgreSQL warehouse uses a star schema consisting of one central fact
table and three dimension tables.

Fact Table
fact_tracks

Contains track-level records used for analysis.

Column	Description
track_id	Unique Spotify track identifier
track_name	Track name
artist_id	Foreign key to dim_artist
album_id	Foreign key to dim_album
date_id	Foreign key to dim_date
Dimension Tables
dim_artist

Stores unique artist information.

artist_id
artist_name
dim_album

Stores unique album information.

album_id
album_name
dim_date

Stores date attributes used for analysis.

date_id
date
year
month
day
ETL Process
1. Extract

Spotify data is collected through the Spotify Web API.

Spotify Web API
      ↓
Track / Metadata JSON

The extraction scripts retrieve Spotify data and prepare it for downstream
processing.

2. Load Raw Data

Raw data is stored in Amazon S3 before transformation.

Spotify Web API
      ↓
AWS S3
      ↓
Raw JSON Data

This creates a separate raw-data layer before transformation.

3. Transform

PySpark is used to process and transform the raw data.

The transformation process includes:

Cleaning raw records
Selecting relevant fields
Structuring track information
Preparing dimension data
Preparing fact data
Handling duplicate records
Creating relationships between fact and dimension data
Raw JSON
    ↓
PySpark
    ↓
Processed Data
4. Load into PostgreSQL

The processed data is loaded into a PostgreSQL data warehouse.

The warehouse follows a star schema:

dim_artist
      \
       \
dim_album ---> fact_tracks
       /
      /
dim_date

The loading process creates and populates the fact and dimension tables.

5. Analyze

SQL queries are used to analyze the warehouse.

Example analytical questions include:

Which artists have the most tracks?
Which albums contain the most tracks?
How are tracks distributed across artists?
How are tracks distributed across albums?
How does the number of tracks vary by date?

The SQL analysis is located in:

sql/analytics_queries.sql
6. Export for Visualization

The PostgreSQL warehouse tables are exported as CSV files using:

python/export_csv.py

The exported datasets are stored in:

data/dashboard/

These files are then used as the data source for Tableau.

Dashboard

The final data warehouse output is visualized using Tableau.

The dashboard provides an overview of:

Total tracks
Total artists
Total albums
Tracks by artist
Tracks by album
Spotify Analytics Dashboard

Project Structure
spotify-data-warehouse/
│
├── docs/
│   ├── spotify_dashboard.png
│   └── star_schema.png
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── dashboard/
│
├── python/
│   ├── clean_tracks.py
│   ├── export_csv.py
│   ├── load.py
│   └── transform.py
│
├── scripts/
│   ├── extract.py
│   ├── extract_tracks.py
│   └── upload_to_s3.py
│
├── sql/
│   ├── analytics_queries.sql
│   └── create_schema.sql
│
├── spotify-data-warehouse/
│   └── spotify_spark_exploration.ipynb
│
├── README.md
├── requirements.txt
├── extract.py
└── extract_tracks.py
Technologies Used
Technology	Purpose
Python	API ingestion and ETL scripting
Spotify Web API	Source data
AWS S3	Raw data storage
PySpark	Data transformation
PostgreSQL	Data warehouse
SQL	Data analysis
Pandas	Data processing and CSV export
SQLAlchemy	PostgreSQL connection and data loading
Tableau	Data visualization
Git / GitHub	Version control
How to Run
1. Clone the Repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd spotify-data-warehouse
2. Install Dependencies
pip install -r requirements.txt
3. Configure PostgreSQL

Create the warehouse database:

CREATE DATABASE spotify_dw;

Create the required warehouse tables using:

sql/create_schema.sql
4. Load the Data

Run the PostgreSQL loading script:

python python/load.py
5. Export Dashboard Data

Run:

python python/export_csv.py

This exports the warehouse tables to:

data/dashboard/
6. Visualize in Tableau

Import the exported CSV files into Tableau and build the dashboard using
the warehouse data.

Analytics

The project includes SQL queries demonstrating common analytical
techniques, including:

SELECT
Filtering
Sorting
GROUP BY
Aggregate functions
JOIN
Counting and summarization

The SQL analysis is located in:

sql/analytics_queries.sql
Key Learning Outcomes

This project provided hands-on experience building an end-to-end data
warehouse pipeline.

Key skills demonstrated include:

Designing an ETL pipeline
Working with REST APIs
Using cloud object storage
Processing data with PySpark
Designing a star schema
Creating fact and dimension tables
Writing analytical SQL
Loading data into PostgreSQL
Preparing warehouse data for BI tools
Building Tableau dashboards
Managing a project with Git and GitHub
Future Improvements

Potential improvements include:

Automating scheduled Spotify API ingestion
Expanding the dataset with additional Spotify attributes
Adding historical listening data
Implementing incremental data loading
Adding automated data quality checks
Adding pipeline monitoring
Expanding the Tableau dashboard
Deploying the dashboard for public access
Migrating the warehouse to a cloud database
Author

Shriya Patnayakuni

Computer Science @ UT Dallas

This project was built as an end-to-end data engineering and analytics
portfolio project.
