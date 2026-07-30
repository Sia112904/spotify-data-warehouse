-- =====================================================
-- Spotify Analytics SQL Layer
-- Day 11
-- Business-focused analytics queries
-- =====================================================


-- =====================================================
-- 1. Top Artists by Number of Tracks
-- Business Question:
-- Which artists have the largest presence?
-- =====================================================

SELECT
    a.artist_name,
    COUNT(*) AS total_tracks
FROM fact_tracks f
JOIN dim_artist a
ON f.artist_id = a.artist_id
GROUP BY a.artist_name
ORDER BY total_tracks DESC;



-- =====================================================
-- 2. Most Popular Albums by Track Count
-- Business Question:
-- Which albums have the most songs in the catalog?
-- =====================================================

SELECT
    al.album_name,
    COUNT(*) AS total_tracks
FROM fact_tracks f
JOIN dim_album al
ON f.album_id = al.album_id
GROUP BY al.album_name
ORDER BY total_tracks DESC;



-- =====================================================
-- 3. Total Tracks in Warehouse
-- Business Question:
-- How large is our Spotify dataset?
-- =====================================================

SELECT
    COUNT(*) AS total_tracks
FROM fact_tracks;



-- =====================================================
-- 4. Artist Catalog Size
-- Business Question:
-- Which artists have the biggest catalogs?
-- =====================================================

SELECT
    a.artist_name,
    COUNT(DISTINCT f.track_id) AS number_of_songs
FROM fact_tracks f
JOIN dim_artist a
ON f.artist_id = a.artist_id
GROUP BY a.artist_name
ORDER BY number_of_songs DESC;



-- =====================================================
-- 5. Album Catalog Size
-- Business Question:
-- Which albums contain the most songs?
-- =====================================================

SELECT
    al.album_name,
    COUNT(DISTINCT f.track_id) AS number_of_songs
FROM fact_tracks f
JOIN dim_album al
ON f.album_id = al.album_id
GROUP BY al.album_name
ORDER BY number_of_songs DESC;



-- =====================================================
-- 6. Listening Activity by Date
-- Business Question:
-- How many tracks were analyzed each day?
-- =====================================================

SELECT
    d.full_date,
    COUNT(*) AS tracks_played
FROM fact_tracks f
JOIN dim_date d
ON f.date_id = d.date_id
GROUP BY d.full_date
ORDER BY d.full_date;



-- =====================================================
-- 7. Artist and Album Relationship
-- Business Question:
-- Which artists appear across multiple albums?
-- =====================================================

SELECT
    a.artist_name,
    COUNT(DISTINCT al.album_id) AS album_count
FROM fact_tracks f
JOIN dim_artist a
ON f.artist_id = a.artist_id
JOIN dim_album al
ON f.album_id = al.album_id
GROUP BY a.artist_name
ORDER BY album_count DESC;



-- =====================================================
-- 8. Track List by Artist
-- Business Question:
-- What songs belong to each artist?
-- =====================================================

SELECT
    a.artist_name,
    f.track_name
FROM fact_tracks f
JOIN dim_artist a
ON f.artist_id = a.artist_id
ORDER BY a.artist_name;



-- =====================================================
-- 9. Duplicate Listening Candidates
-- Business Question:
-- Which songs appear multiple times?
-- =====================================================

SELECT
    track_name,
    COUNT(*) AS occurrences
FROM fact_tracks
GROUP BY track_name
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;



-- =====================================================
-- 10. Warehouse Summary Report
-- Business Question:
-- What is the overall size of our Spotify warehouse?
-- =====================================================

SELECT
    (SELECT COUNT(*) FROM dim_artist) AS total_artists,
    (SELECT COUNT(*) FROM dim_album) AS total_albums,
    (SELECT COUNT(*) FROM fact_tracks) AS total_tracks;
