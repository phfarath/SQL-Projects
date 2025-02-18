-- Contagem de Review por Produto, os 10 mais avaliados do database
SELECT 
    p.product_name,
    COUNT(r.review_id) AS review_count
FROM dim_produto p
LEFT JOIN review r ON p.ProductKey = r.ProductKey
GROUP BY p.product_name
ORDER BY review_count DESC
LIMIT 10;
