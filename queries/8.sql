--EXPLAIN
SELECT 
    st.status_name, 
    u.user_name,
    (
        SELECT COUNT(p.id) 
        FROM photo p 
        JOIN butterfly b ON p.butterfly_id = b.id
        JOIN species_book sb ON b.species_id = sb.id
        JOIN status s ON sb.id = s.species_id AND b.author_id = u.id
        WHERE s.status_type = st.id
    ) AS photo_count
FROM 
    status_type st
CROSS JOIN 
    user_ u;