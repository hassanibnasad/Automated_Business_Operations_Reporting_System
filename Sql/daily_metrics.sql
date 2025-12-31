SELECT
    o.order_date,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_revenue,
    SUM(CASE WHEN p.status = 'FAILED' THEN 1 ELSE 0 END) AS failed_payments,
    SUM(CASE WHEN p.status = 'PENDING' THEN 1 ELSE 0 END) AS pending_payments
FROM orders o
LEFT JOIN payments p ON o.order_id = p.order_id
GROUP BY o.order_date
ORDER BY o.order_date;
-- This SQL query retrieves daily metrics including total orders, total revenue,
-- number of failed payments, and number of pending payments by joining the orders