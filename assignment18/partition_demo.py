from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionDemo") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("\n" + "=" * 55)
print("   PySpark Partitioning Demo — 5 Million Records")
print("=" * 55)

df = spark.range(0, 5_000_000)

print(f"\n📦 Total Records       : {df.count():,}")
print(f"🔢 Initial Partitions  : {df.rdd.getNumPartitions()}")

df_repart = df.repartition(12)
print(f"\n🔼 After repartition(12): {df_repart.rdd.getNumPartitions()} partitions")

df_coalesced = df_repart.coalesce(3)
print(f"🔽 After coalesce(3)    : {df_coalesced.rdd.getNumPartitions()} partitions")

print("\n" + "=" * 55)
print("✅ Partition operations completed successfully!")
print("=" * 55 + "\n")

spark.stop()
