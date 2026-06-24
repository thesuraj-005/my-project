# Assignment 17: PySpark DataFrame Sales Analysis

This project demonstrates a **PySpark DataFrame** application that reads a sales dataset, performs data analysis operations, and saves filtered results — all running inside a **Docker container** with Java, Python, and Apache Spark pre-installed.

---

## 📁 Project Structure

```
assignment17/
├── sales.csv                          # Input dataset
├── sales_analysis.py                  # PySpark application script
├── Dockerfile                         # Docker config (Java + Python + Spark)
├── requirements.txt                   # Python dependencies
├── output/
│   └── high_sales_products.csv        # Filtered output (sales > 80,000)
└── README.md                          # Project documentation (this file)
```

---

## 📊 Dataset

**File:** `sales.csv`

| product_id | product_name | category    | sales   |
|------------|--------------|-------------|---------|
| 101        | Laptop       | Electronics | 150000  |
| 102        | Mobile       | Electronics | 95000   |
| 103        | TV           | Electronics | 120000  |
| 104        | Chair        | Furniture   | 30000   |
| 105        | Table        | Furniture   | 45000   |
| 106        | Sofa         | Furniture   | 80000   |
| 107        | Headphones   | Electronics | 25000   |
| 108        | Bed          | Furniture   | 90000   |

---

## ⚙️ Operations Performed

### 1️⃣ Sort All Products by Sales (Descending)
All products are sorted from highest to lowest sales value using `orderBy(col("sales").desc())`.

### 2️⃣ Top 3 Products with Highest Sales
The top 3 best-selling products are extracted using `.limit(3)` on the sorted DataFrame.

### 3️⃣ Filter Products with Sales > 80,000 and Save
Products where `sales > 80000` are filtered and saved as a CSV file to the `output/` directory.

---

## 🐳 Docker Setup

### Technologies Used
| Tool         | Version  |
|--------------|----------|
| Python       | 3.11     |
| Java (JRE)   | 17       |
| Apache Spark | 3.5.1    |
| PySpark      | 3.5.1    |

---

## 🚀 How to Run

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (must be running)
- [Git](https://git-scm.com/)

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/my-project.git
cd my-project/assignment17
```

### Step 2: Build the Docker Image
```bash
docker build -t pyspark-sales-app .
```

### Step 3: Run the Docker Container
```bash
docker run --rm pyspark-sales-app
```

The application will **automatically start** when the container runs and print results to the terminal.

---

## 📤 Sample Output

```
=======================================================
       PySpark Sales Data Analysis
=======================================================

📋 Raw Sales Data:
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       102|      Mobile|Electronics| 95000|
|       103|          TV|Electronics|120000|
|       104|       Chair|  Furniture| 30000|
|       105|       Table|  Furniture| 45000|
|       106|        Sofa|  Furniture| 80000|
|       107| Headphones |Electronics| 25000|
|       108|         Bed|  Furniture| 90000|
+----------+------------+-----------+------+

=======================================================
🔽 All Products Sorted by Sales (Descending):
=======================================================
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
|       108|         Bed|  Furniture| 90000|
|       106|        Sofa|  Furniture| 80000|
|       105|       Table|  Furniture| 45000|
|       104|       Chair|  Furniture| 30000|
|       107| Headphones |Electronics| 25000|
+----------+------------+-----------+------+

=======================================================
🏆 Top 3 Products with Highest Sales:
=======================================================
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       103|          TV|Electronics|120000|
|       102|      Mobile|Electronics| 95000|
+----------+------------+-----------+------+

=======================================================
💰 Products with Sales Greater than 80,000:
=======================================================
+----------+------------+-----------+------+
|product_id|product_name|   category| sales|
+----------+------------+-----------+------+
|       101|      Laptop|Electronics|150000|
|       102|      Mobile|Electronics| 95000|
|       103|          TV|Electronics|120000|
|       108|         Bed|  Furniture| 90000|
+----------+------------+-----------+------+

✅ Filtered results saved to: output/high_sales_products/
=======================================================
```

---

## 📝 Notes

- `coalesce(1)` is used to write the filtered output into a single CSV file instead of multiple part files.
- Spark is configured with `local[*]` to use all available CPU cores inside the container.
- Log level is set to `ERROR` to suppress verbose Spark INFO logs.

#assignment
