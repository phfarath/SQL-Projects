-- Listando reviews com informações sobre o Produto e o Usuários, ordenando por nome do produto
SELECT 
    r.review_title as titulo,
    r.review_content as conteudo_review,
    p.product_name as nome_produto,
    u.user_name as nome_dos_usuarios
FROM review r
JOIN dim_produto p ON r.ProductKey = p.ProductKey
JOIN dim_user u ON r.UserKey = u.UserKey
ORDER BY p.product_name;
