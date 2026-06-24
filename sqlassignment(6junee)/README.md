# Assignment 19: SQL Case Study #4 — Data Bank

**Source:** [8 Week SQL Challenge — Case Study #4](https://8weeksqlchallenge.com/case-study-4/)

Data Bank is a digital-first neobank that stores customer data on secure distributed nodes. This case study explores **customer node allocation** and **transaction behavior** using SQL.

---



```
assignment19/
├── schema.sql       # Table definitions + sample data
├── solutions.sql    # All SQL query solutions (Section A & B)
└── README.md        # Documentation (this file)
```


### `regions`
| Column      | Type         |
|-------------|--------------|
| region_id   | INTEGER      |
| region_name | VARCHAR(9)   |

### `customer_nodes`
| Column      | Type    |
|-------------|---------|
| customer_id | INTEGER |
| region_id   | INTEGER |
| node_id     | INTEGER |
| start_date  | DATE    |
| end_date    | DATE    |

### `customer_transactions`
| Column      | Type         |
|-------------|--------------|
| customer_id | INTEGER      |
| txn_date    | DATE         |
| txn_type    | VARCHAR(10)  |
| txn_amount  | INTEGER      |

---

## 

### Q1: How many unique nodes are there on the Data Bank system?
```sql
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;
```
**Result:** `5` unique nodes

---

### Q2: What is the number of nodes per region?
```sql
SELECT
    r.region_name,
    COUNT(DISTINCT cn.node_id) AS node_count
FROM customer_nodes cn
JOIN regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;
```
| region_name | node_count |
|-------------|------------|
| Africa      | 5          |
| America     | 5          |
| Asia        | 5          |
| Australia   | 5          |
| Europe      | 5          |

---

### Q3: How many customers are allocated to each region?
```sql
SELECT
    r.region_name,
    COUNT(DISTINCT cn.customer_id) AS customer_count
FROM customer_nodes cn
JOIN regions r ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY customer_count DESC;
```
| region_name | customer_count |
|-------------|----------------|
| Africa      | 5              |
| America     | 2              |
| Asia        | 2              |
| Australia   | 3              |
| Europe      | 2              |

---

### Q4: How many days on average are customers reallocated to a different node?
```sql
SELECT
    ROUND(AVG(end_date - start_date), 2) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date != '9999-12-31';
```
> Filters out records where `end_date = '9999-12-31'` (still-active nodes).

**Result:** ~`14.63` days on average

---

### Q5: Median, 80th and 95th percentile for reallocation days per region
```sql
WITH reallocation AS (
    SELECT r.region_name,
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
```
> Uses `PERCENTILE_CONT` for interpolated percentile calculations.

---

## 💳 Section B — Customer Transactions

### Q1: Unique count and total amount for each transaction type
```sql
SELECT
    txn_type,
    COUNT(*)        AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;
```
| txn_type   | transaction_count | total_amount |
|------------|-------------------|--------------|
| deposit    | 50                | 26,863       |
| purchase   | 12                | 7,433        |
| withdrawal | 4                 | 1,568        |

*(Values based on sample data)*

---

### Q2: Average total historical deposit counts and amounts for all customers
```sql
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
    ROUND(AVG(deposit_count), 2)      AS avg_deposit_count,
    ROUND(AVG(avg_deposit_amount), 2) AS avg_deposit_amount
FROM customer_deposits;
```
> First computes per-customer deposit stats, then averages across all customers.

---

### Q3: Customers with >1 deposit AND (≥1 purchase OR ≥1 withdrawal) per month
```sql
WITH monthly_activity AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', txn_date) AS txn_month,
        SUM(CASE WHEN txn_type = 'deposit'    THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase'   THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, DATE_TRUNC('month', txn_date)
)
SELECT
    TO_CHAR(txn_month, 'Month YYYY') AS month,
    COUNT(customer_id)               AS qualifying_customers
FROM monthly_activity
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY txn_month
ORDER BY txn_month;
```
> Uses `CASE WHEN` inside `SUM()` to pivot transaction types into columns per customer per month.

---

## 🚀 How to Run

### Prerequisites
- PostgreSQL installed, or use [db-fiddle.com](https://www.db-fiddle.com/) / [SQLFiddle](http://sqlfiddle.com/)

### Steps
1. Run `schema.sql` first to create tables and insert sample data
2. Run `solutions.sql` to execute all queries

```bash
psql -U postgres -f schema.sql
psql -U postgres -f solutions.sql
```

---

## 📝 Key SQL Concepts Used

| Concept | Used In |
|--------|---------|
| `COUNT(DISTINCT ...)` | Q1, Q2, Q3 |
| `JOIN` | Q2, Q3, Q5 |
| `GROUP BY` | Q2, Q3, Q4, Q5, B1, B2, B3 |
| `PERCENTILE_CONT` | A5 |
| `CTE (WITH ...)` | A5, B2, B3 |
| `DATE_TRUNC` | B3 |
| `CASE WHEN` | B3 |
| `HAVING` / `WHERE` filter | A4, B3 |

#assignment
