EXPLAIN
SELECT st.status_name, COUNT(DISTINCT sb.id) AS species_count
FROM status s
JOIN status_type st ON s.status_type = st.id
JOIN species_book sb ON s.species_id = sb.id
GROUP BY st.status_name;
