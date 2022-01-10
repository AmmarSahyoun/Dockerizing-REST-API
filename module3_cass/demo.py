from cassandra.cluster import Cluster

cluster = Cluster(['0.0.0.0'], port=9042)
session = cluster.connect("employee")

#read samples

rows = session.execute('SELECT * FROM employee_details;')
for employee_row in rows:
    print(employee_row)