SELECT DISTINCT
    m1.movie_id AS movie1_id, 
    m1.title AS movie1_title,
    m2.movie_id AS movie2_id, 
    m2.title AS movie2_title,
    ABS(r1.avg_rating - r2.avg_rating) AS diferença_rating
FROM movies m1
JOIN movies m2 ON m1.directors = m2.directors AND m1.movie_id < m2.movie_id
JOIN ratings r1 ON m1.movie_id = r1.movie_id
JOIN ratings r2 ON m2.movie_id = r2.movie_id
WHERE ABS(r1.avg_rating - r2.avg_rating) < 0.5;
