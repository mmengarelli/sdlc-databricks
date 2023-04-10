# Databricks notebook source
# MAGIC %pip install nutter

# COMMAND ----------

from runtime.nutterfixture import NutterFixture

class TestFixture(NutterFixture):
  def before_all(self):
    print("in before all")
   
  def after_all(self):
    print("in after all")

  def run_tests(self):
    results = []
    notebooks = [
      "../notebooks/ValidationWorkflow"
    ]

    for n in notebooks:
      result = dbutils.notebook.run(n, 60)
      print(result)
      results.append(result)
    
    # Do some data validation or whatever

# COMMAND ----------

fix = TestFixture()
fix.run_tests()
