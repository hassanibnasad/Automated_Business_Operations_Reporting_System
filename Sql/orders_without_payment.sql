SELECT
    o.order_id,
    o.order_date,
    o.amount
FROM orders o
LEFT JOIN payments p ON o.order_id = p.order_id
WHERE p.order_id IS NULL;
