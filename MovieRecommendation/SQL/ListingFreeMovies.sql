SELECT DISTINCT
    m.movie_id, 
    m.title, 
    r.avg_rating, 
    r.num_ratings, 
    mp.format
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
JOIN movie_prices mp ON m.movie_id = mp.movie_id
WHERE mp.price_dollars = 0.00;
