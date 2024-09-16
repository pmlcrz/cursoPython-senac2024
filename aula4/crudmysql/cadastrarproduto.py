import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "INSERT INTO produto (nomeproduto, qtd, valor) VALUES (%s, %s, %s)"
data = (
    'Notebook XYZ',
    10,
    2999.99
)

try:
    cursor.execute(sql, data)
    connection.commit()
    codproduto = cursor.lastrowid
    print("Produto cadastrado com sucesso, Seu código é:", codproduto)
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
