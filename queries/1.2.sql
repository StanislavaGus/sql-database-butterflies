EXPLAIN
SELECT u.user_name, u.user_login, u.user_password
FROM user_ u
JOIN butterfly b ON u.id = b.author_id
JOIN species_book sb ON b.species_id = sb.id
JOIN status s ON sb.id = s.species_id
JOIN status_type st ON s.status_type = st.id
WHERE sb.species_name = 'name 15'
  AND st.status_name = 'likely extinct'
GROUP BY u.id, u.user_name, u.user_login, u.user_password
HAVING COUNT(b.id) >= 3;
