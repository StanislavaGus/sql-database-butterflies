EXPLAIN
SELECT st.status_name, COUNT(b.id) AS butterfly_count
FROM status s
JOIN status_type st ON s.status_type = st.id
JOIN species_book sb ON s.species_id = sb.id
JOIN butterfly b ON sb.id = b.species_id
GROUP BY st.status_name
ORDER BY st.status_name;
