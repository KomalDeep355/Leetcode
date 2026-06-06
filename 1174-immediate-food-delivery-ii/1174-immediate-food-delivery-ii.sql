# Write your MySQL query statement below
-- Step 1: Filter the main table down to only include the first order for each customer
WITH FirstOrders AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)

-- Step 2: Calculate the aggregate percentage across all first orders
SELECT 
    ROUND(
        (SUM(d.order_date = d.customer_pref_delivery_date) * 100.0) / COUNT(*), 
        2
    ) AS immediate_percentage
FROM Delivery d
JOIN FirstOrders fo 
    ON d.customer_id = fo.customer_id 
    AND d.order_date = fo.first_order_date;