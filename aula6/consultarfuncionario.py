import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "SELECT * FROM funcionario"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
