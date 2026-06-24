# Assignment 18: PySpark Partitioning — repartition() & coalesce()

This project demonstrates how PySpark manages data partitioning using `spark.range()`, `repartition()`, and `coalesce()` on a DataFrame of **5 million records**, all running inside a Docker container.

---

## 📁 Project Structure

```
assignment18/
├── partition_demo.py     # PySpark application script
├── Dockerfile            # Docker config (Java + Python + Spark)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (this file)
```

---

## ⚙️ Operations Performed

### 1️⃣ Generate 5 Million Records
```python
df = spark.range(0, 5_000_000)
```
Creates a DataFrame with 5,000,000 rows using the built-in `spark.range()` method.

### 2️⃣ Display Initial Partitions
```python
df.rdd.getNumPartitions()
```
Displays the default number of partitions assigned by Spark (based on available CPU cores).

### 3️⃣ Increase Partitions to 12 — `repartition()`
```python
df_repart = df.repartition(12)
```
Performs a **full shuffle** to redistribute data evenly across 12 partitions. Use when increasing partitions or rebalancing skewed data.

### 4️⃣ Reduce Partitions to 3 — `coalesce()`
```python
df_coalesced = df_repart.coalesce(3)
```
Reduces partitions to 3 **without a full shuffle** by combining existing partitions. More efficient than `repartition()` when only reducing partition count.

---

## 🔍 Key Differences: repartition() vs coalesce()

| Feature              | `repartition()`        | `coalesce()`              |
|----------------------|------------------------|---------------------------|
| Shuffle              | ✅ Full shuffle         | ❌ No full shuffle         |
| Use case             | Increase or rebalance  | Decrease only             |
| Performance          | Slower (more expensive)| Faster (more efficient)   |
| Data distribution    | Even across partitions | May be slightly uneven    |

---

## 🐳 Docker Setup

| Tool         | Version |
|--------------|---------|
| Python       | 3.11    |
| Java (JRE)   | 17      |
| Apache Spark | 3.5.1   |
| PySpark      | 3.5.1   |

---

## 🚀 How to Run

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (must be running)
- [Git](https://git-scm.com/)

### Step 1: Clone the Repository
```bash
git clone https://github.com/thesuraj-005/my-project.git
cd my-project/assignment18
```

### Step 2: Build the Docker Image
```bash
docker build -t pyspark-partition-demo .
```

### Step 3: Run the Docker Container
```bash
docker run --rm pyspark-partition-demo
```

---

## 📤 Sample Output

```
=======================================================
   PySpark Partitioning Demo — 5 Million Records
=======================================================

📦 Total Records       : 5,000,000
🔢 Initial Partitions  : 8

🔼 After repartition(12): 12 partitions
🔽 After coalesce(3)    : 3 partitions

=======================================================
✅ Partition operations completed successfully!
=======================================================
```

> **Note:** The initial partition count depends on the number of CPU cores available in the environment.

#assignment
