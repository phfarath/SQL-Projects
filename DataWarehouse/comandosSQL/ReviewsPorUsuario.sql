-- Contando as Reviews por Usuário, os 20 usuários com mais reviews
SELECT 
    u.user_name,
    COUNT(r.review_id) AS review_count
FROM dim_user u
LEFT JOIN review r ON u.UserKey = r.UserKey
GROUP BY u.user_name
ORDER BY review_count DESC
LIMIT 20;
