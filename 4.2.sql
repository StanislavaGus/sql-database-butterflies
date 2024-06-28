EXPLAIN --ANALYZE
SELECT u.user_name, COUNT(b.id) AS observation_count
FROM user_ u
LEFT JOIN butterfly b ON u.id = b.author_id
GROUP BY u.user_name
HAVING COUNT(b.id) = (
    SELECT COUNT(b.id) AS min_observation_count
    FROM butterfly b
    JOIN user_ u ON u.id = b.author_id
    GROUP BY u.id
    ORDER BY min_observation_count ASC
    LIMIT 1
);
