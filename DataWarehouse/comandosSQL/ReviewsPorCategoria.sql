-- Total de Reviews por categoria de produto, as 20 categorias com mais reviews
SELECT 
    p.category,
    COUNT(r.review_id) AS total_reviews
FROM dim_produto p
JOIN review r ON p.ProductKey = r.ProductKey
GROUP BY p.category
ORDER BY total_reviews DESC;