EXPLAIN
SELECT u.user_name
FROM user_ u
WHERE NOT EXISTS (
    SELECT 1
    FROM butterfly b
    JOIN species_book sb ON b.species_id = sb.id
    WHERE u.id = b.author_id AND sb.species_name = 'name 35674'
);
