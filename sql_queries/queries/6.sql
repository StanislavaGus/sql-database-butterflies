--EXPLAIN
--SELECT observation_count, COUNT(*) AS species_count_with_same_observation_count
--FROM (
  --  SELECT sb.species_name, COUNT(*) AS observation_count
    --FROM species_book sb
    --JOIN butterfly b ON sb.id = b.species_id
    --GROUP BY sb.species_name
--) AS subquery
--GROUP BY observation_count
--HAVING COUNT(*) > 1;

EXPLAIN
SELECT observation_count, COUNT(*) AS species_count
FROM (
    SELECT COUNT(*) AS observation_count
    FROM butterfly
    GROUP BY species_id
) AS observations_per_species
GROUP BY observation_count
ORDER BY observation_count;