from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import re

# -------------------------
# Create Spark Session
# -------------------------

spark = (
    SparkSession.builder
    .appName("Spotify Data Cleaning")
    .getOrCreate()
)

# -------------------------
# Load Raw Data
# -------------------------

df = spark.read.option("multiline", "true").json("data/raw/tracks_raw.json")

print("Raw Row Count:")
print(df.count())

df.show(5)

# -------------------------
# Remove Duplicates
# -------------------------

df = df.dropDuplicates()

print("After Removing Duplicates:")
print(df.count())

# -------------------------
# Handle Null Values
# -------------------------

df = df.dropna()

print("After Removing Nulls:")
print(df.count())

# -------------------------
# Convert camelCase to snake_case
# -------------------------

def camel_to_snake(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

new_columns = [
    camel_to_snake(column)
    for column in df.columns
]

df = df.toDF(*new_columns)

# -------------------------
# Standardize Column Names
# -------------------------

for column in df.columns:
    df = df.withColumnRenamed(
        column,
        column.strip().lower()
    )

print("Cleaned Columns:")
print(df.columns)

# -------------------------
# Show Final Dataset
# -------------------------

df.show(5)

# -------------------------
# Save as Parquet
# -------------------------

df.write.mode("overwrite").parquet(
    "data/processed/processed_tracks.parquet"
)

print("Saved cleaned parquet file!")
