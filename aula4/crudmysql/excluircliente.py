import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "DELETE FROM cliente WHERE codcliente = %s"
data = (5,)

try:
    cursor.execute(sql, data)
    connection.commit()
    print("Cliente excluído com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
