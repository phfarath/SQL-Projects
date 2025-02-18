-- Listando as 5 categorias com mais avaliações
SELECT 
    category as categoria,
    SUM(rating_count) AS avaliação_total
FROM dim_produto
GROUP BY category
ORDER BY avaliação_total DESC
LIMIT 5;