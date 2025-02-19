SELECT DISTINCT
    m.movie_id, 
    m.title, 
    r.avg_rating, 
    r.num_ratings,
    RANK() OVER (ORDER BY r.avg_rating DESC, r.num_ratings DESC) AS ranking
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
ORDER BY avg_rating DESC, num_ratings DESC;