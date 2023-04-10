# Databricks notebook source
# MAGIC %md Dummy functions for SDLC testing

# COMMAND ----------

def validate_counts(table1:str, table2:str):
  ct1 = spark.table(table1).count()
  ct2 = spark.table(table1).count()
  return (ct1, ct2)

def validate_stats(table1:str, table2:str):
  stats_df1 = spark.table(table1).describe()
  stats_df2 = spark.table(table2).describe()
  return (stats_df1, stats_df2)

def validate_table(table1:str, table2:str):
  res1 = validate_counts(table1, table2)
  res2 = validate_stats(table1, table2)
  results = [res1, res2]

# COMMAND ----------

def validate_all():

  t1 = "tmp_vw"
  spark.range(100).createOrReplaceTempView(t1)

  tables = [
    (t1, t1),
    (t1, t1)
  ]

  results = []
  for t in tables:
    results.append(validate_counts(t[0], t[1]))
    results.append(validate_stats(t[0], t[1]))

  return results

# COMMAND ----------

t1 = "tmp_vw"
spark.range(100).createOrReplaceTempView(t1)

res = validate_counts("tmp_vw", "tmp_vw")
print(res)

