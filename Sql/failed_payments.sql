SELECT
    o.order_id,
    o.order_date,
    o.amount,
    p.status
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE p.status = 'FAILED';
