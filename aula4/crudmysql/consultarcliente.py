import mysql.connector
import datetime
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda'
)
cursor = connection.cursor()
sql = "SELECT * FROM cliente"
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
connection.close()
for result in results:
    print(result)
