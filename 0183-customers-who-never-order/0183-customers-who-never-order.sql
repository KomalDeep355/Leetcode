SELECT
    c.name AS Customers
FROM Customers c
LEFT JOIN Orders
ON c.id = Orders.customerId
WHERE Orders.customerId IS NULL;