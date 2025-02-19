SELECT DISTINCT
    m2.movie_id,
    m2.title,
    r2.avg_rating,
    r2.num_ratings,
    ABS(r2.avg_rating - r1.avg_rating) AS diff_rating
FROM movies m1
JOIN ratings r1 ON m1.movie_id = r1.movie_id
JOIN ratings r2 ON m1.movie_id <> r2.movie_id
JOIN movies m2 ON r2.movie_id = m2.movie_id
WHERE m1.movie_id = 123  -- ID do filme de interesse 
  AND ABS(r2.avg_rating - r1.avg_rating) <= 0.5
ORDER BY diff_rating ASC, r2.num_ratings DESC
LIMIT 5;
