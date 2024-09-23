import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "UPDATE produto SET nomeproduto = %s, qtd = %s, valor = %s WHERE codproduto = %s"
data = (
    'Novo Produto',
    20,
    3499.99,
    1
)

try:
    cursor.execute(sql, data)
    connection.commit()
    print("Produto atualizado com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
