

SET search_path = data_bank;


SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;


SELECT
    r.region_name,
    COUNT(DISTINCT cn.node_id) AS node_count
FROM customer_nodes cn
JOIN regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;

SELECT
    r.region_name,
    COUNT(DISTINCT cn.customer_id) AS customer_count
FROM customer_nodes cn
JOIN regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY customer_count DESC;

SELECT
    ROUND(AVG(end_date - start_date), 2) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date != '9999-12-31';

───────────
WITH reallocation AS (
    SELECT
        r.region_name,
        (cn.end_date - cn.start_date) AS days_in_node
    FROM customer_nodes cn
    JOIN regions r ON cn.region_id = r.region_id
    WHERE cn.end_date != '9999-12-31'
)
SELECT
    region_name,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY days_in_node) AS median_days,
    PERCENTILE_CONT(0.80) WITHIN GROUP (ORDER BY days_in_node) AS pct_80_days,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days_in_node) AS pct_95_days
FROM reallocation
GROUP BY region_name
ORDER BY region_name;


SELECT
    txn_type,
    COUNT(*)          AS transaction_count,
    SUM(txn_amount)   AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;

WITH customer_deposits AS (
    SELECT
        customer_id,
        COUNT(*)        AS deposit_count,
        AVG(txn_amount) AS avg_deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)
SELECT
    ROUND(AVG(deposit_count), 2)       AS avg_deposit_count,
    ROUND(AVG(avg_deposit_amount), 2)  AS avg_deposit_amount
FROM customer_deposits;


WITH monthly_activity AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', txn_date)                                   AS txn_month,
        SUM(CASE WHEN txn_type = 'deposit'    THEN 1 ELSE 0 END)        AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase'   THEN 1 ELSE 0 END)        AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END)        AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, DATE_TRUNC('month', txn_date)
)
SELECT
    TO_CHAR(txn_month, 'Month YYYY')  AS month,
    COUNT(customer_id)                AS qualifying_customers
FROM monthly_activity
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY txn_month
ORDER BY txn_month;
