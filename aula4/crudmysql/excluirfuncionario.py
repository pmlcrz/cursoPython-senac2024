import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "DELETE FROM funcionario WHERE codfuncionario = %s"
data = (1,)

try:
    cursor.execute(sql, data)
    connection.commit()
    print("Funcionário excluído com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
