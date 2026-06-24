from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# ─────────────────────────────────────────────
# 1. Initialize Spark Session
# ─────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("\n" + "=" * 55)
print("       PySpark Sales Data Analysis")
print("=" * 55)

# ─────────────────────────────────────────────
# 2. Read CSV into DataFrame
# ─────────────────────────────────────────────
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("\n📋 Raw Sales Data:")
df.show()

# ─────────────────────────────────────────────
# 3. Sort all products by sales (Descending)
# ─────────────────────────────────────────────
print("=" * 55)
print("🔽 All Products Sorted by Sales (Descending):")
print("=" * 55)
df_sorted = df.orderBy(col("sales").desc())
df_sorted.show()

# ─────────────────────────────────────────────
# 4. Top 3 products with highest sales
# ─────────────────────────────────────────────
print("=" * 55)
print("🏆 Top 3 Products with Highest Sales:")
print("=" * 55)
df_top3 = df_sorted.limit(3)
df_top3.show()

# ─────────────────────────────────────────────
# 5. Filter products with sales > 80,000
#    and save as CSV
# ─────────────────────────────────────────────
print("=" * 55)
print("💰 Products with Sales Greater than 80,000:")
print("=" * 55)
df_filtered = df.filter(col("sales") > 80000)
df_filtered.show()

output_path = "output/high_sales_products"
df_filtered.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

print(f"✅ Filtered results saved to: {output_path}/")
print("=" * 55 + "\n")

spark.stop()
