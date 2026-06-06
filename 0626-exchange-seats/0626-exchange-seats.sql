SELECT 
    CASE 
        -- 1. If it's an odd ID AND it's the absolute last row, keep it the same
        WHEN id % 2 = 1 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        -- 2. If it's just a normal odd ID, move it to the next even number
        WHEN id % 2 = 1 THEN id + 1
        -- 3. If it's an even ID, move it back to the previous odd number
        ELSE id - 1
    END AS id, 
    student
FROM Seat
ORDER BY id;