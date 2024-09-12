# Databricks notebook source
Delta:It's a open souce storage framework
helps you to build lakehouse (existing data lake(s3))
1.it brings ACID properties to your existing data lake

All tables in databricks are Delta by defualt

# COMMAND ----------

# MAGIC %sql
# MAGIC select*FRom teqdata.naval_schema.employees

# COMMAND ----------

table=("sirisha","90")
table_schema=("name string","id" int)
df=spark.createDataFrame(table,table_schema)
df.write.format("delta").mode("overwrite").saveAsTable("newtable")

