# Requires Nutter PyPi package installed on the cluster

from runtime.nutterfixture import NutterFixture, tag

class MyTestFixture(NutterFixture):
   def run_test_name(self):
      dbutils.notebook.run('notebook_under_test', 600, args)

   def assertion_test_name(self):
      some_tbl = sqlContext.sql('SELECT COUNT(*) AS total FROM sometable')
      first_row = some_tbl.first()
      assert (first_row[0] == 1)

result = MyTestFixture().execute_tests()
print(result.to_string())
# Comment out the next line (result.exit(dbutils)) to see the test result report from within the notebook
result.exit(dbutils)