from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("\n" + "=" * 55)
print("       PySpark Sales Data Analysis")
print("=" * 55)

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("\n📋 Raw Sales Data:")
df.show()

print("=" * 55)
print("🔽 All Products Sorted by Sales (Descending):")
print("=" * 55)
df_sorted = df.orderBy(col("sales").desc())
df_sorted.show()

print("=" * 55)
print("🏆 Top 3 Products with Highest Sales:")
print("=" * 55)
df_top3 = df_sorted.limit(3)
df_top3.show()

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
