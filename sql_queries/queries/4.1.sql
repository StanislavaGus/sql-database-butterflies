EXPLAIN
SELECT u.user_name, COUNT(b.id) AS observation_count
FROM user_ u
JOIN butterfly b ON u.id = b.author_id
GROUP BY u.user_name
HAVING COUNT(b.id) = (
    SELECT COUNT(b.id) AS max_observation_count
    FROM butterfly b
    JOIN user_ u ON u.id = b.author_id
    GROUP BY u.id
    ORDER BY max_observation_count DESC
    LIMIT 1
);
