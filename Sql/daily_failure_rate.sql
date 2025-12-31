SELECT
    p.payment_date,
    COUNT(*) AS total_payments,
    SUM(CASE WHEN p.status = 'FAILED' THEN 1 ELSE 0 END) AS failed_payments,
    ROUND(
        (SUM(CASE WHEN p.status = 'FAILED' THEN 1 ELSE 0 END) * 100.0) / COUNT(*),
        2
    ) AS failure_percentage
FROM payments p
GROUP BY p.payment_date
ORDER BY p.payment_date;
