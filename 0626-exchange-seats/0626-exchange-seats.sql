# Write your MySQL query statement below
WITH max_id_table AS (
    SELECT MAX(id) AS max_id FROM Seat
)

SELECT 
    CASE
        WHEN id = max_id AND max_id % 2 = 1 THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
    END AS id,
student FROM Seat
CROSS JOIN max_id_table
ORDER BY id ASC;