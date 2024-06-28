EXPLAIN
SELECT COUNT(*)
FROM butterfly b
JOIN species_book sb ON b.species_id = sb.id
WHERE sb.species_name = 'name 5567';
