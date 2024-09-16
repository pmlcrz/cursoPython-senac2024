import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "UPDATE cliente SET nome = %s, endereco = %s, cpf = %s WHERE codcliente = %s"
data = (
    'Novo Nome',
    'Novo Endereco',
    '111.222.333-44',
    1
)

try:
    cursor.execute(sql, data)
    connection.commit()
    print("Cliente atualizado com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
