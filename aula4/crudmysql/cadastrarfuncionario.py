import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "INSERT INTO funcionario (nome, cpf, endereco, datanasc) VALUES (%s, %s, %s, %s)"
data = (
    'Teste',
    '000.899.655-09',
    'Rua ABC, 123',
    '2000-11-10'
)

try:
    cursor.execute(sql, data)
    connection.commit()
    codfuncionario = cursor.lastrowid
    print("Funcionário cadastrado com sucesso, Seu código é:", codfuncionario)
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
