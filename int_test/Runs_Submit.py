# Databricks notebook source
# MAGIC %pip install databricks-cli

# COMMAND ----------

# In CI/CD these would be CLI commands

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.jobs.api import JobsApi

client = ApiClient(
  host  = "https://adb-7954466279135483.3.azuredatabricks.net/",
  token = "" # Make this a secret
)

jobs_api = JobsApi(client)
