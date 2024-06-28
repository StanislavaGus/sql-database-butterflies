EXPLAIN
SELECT sb.species_name, COUNT(*) AS observation_count
FROM species_book sb
JOIN butterfly b ON sb.id = b.species_id
GROUP BY sb.species_name
HAVING COUNT(*) > (
    SELECT COUNT(*)
    FROM species_book
    JOIN butterfly ON species_book.id = butterfly.species_id
    WHERE species_name = 'name 2'
);