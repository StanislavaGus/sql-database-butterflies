EXPLAIN
SELECT COUNT(DISTINCT u.id) AS user_count
FROM user_ u
JOIN butterfly b ON u.id = b.author_id
JOIN species_book sb ON b.species_id = sb.id
WHERE sb.species_name = 'name 5567';
