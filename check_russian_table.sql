-- SELECT * FROM nutrition;
SELECT n.*
FROM species_book sb
JOIN nutrition n ON sb.nutrition_id = n.id
JOIN wings w ON sb.wings_id = w.id
WHERE w.color = 'Red';