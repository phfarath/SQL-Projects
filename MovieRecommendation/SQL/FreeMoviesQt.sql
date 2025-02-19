SELECT COUNT(DISTINCT movie_id) AS free_movies_count
FROM movie_prices
WHERE price_dollars = 0.00;