CREATE TABLE dim_artist (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255)
);

CREATE TABLE dim_album (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(255)
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_tracks (
    track_id VARCHAR(100) PRIMARY KEY,
    track_name VARCHAR(255),
    artist_id INTEGER REFERENCES dim_artist(artist_id),
    album_id INTEGER REFERENCES dim_album(album_id),
    date_id INTEGER REFERENCES dim_date(date_id)
);
