import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'compravenda')
cursor = connection.cursor()
sql = "INSERT INTO cliente (nome, endereco, cpf) VALUES (%s, %s, %s)"
data = (
    'Ana Senac',
    'Rua Santa Luzia, 735',
    '000.899.655-09')
cursor.execute(sql, data)
connection.commit()
codcliente = cursor.lastrowid
cursor.close()
connection.close()
print("Cliente cadastrado com sucesso, Seu código é :", codcliente)

