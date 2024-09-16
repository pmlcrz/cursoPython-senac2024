import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='compravenda'
)

cursor = connection.cursor()

sql = "UPDATE funcionario SET nome = %s, cpf = %s, endereco = %s, datanasc = %s WHERE codfuncionario = %s"
data = (
    'Novo Nome',
    '111.222.333-44',
    'Novo Endereco',
    '1990-01-01',
    1
)

try:
    cursor.execute(sql, data)
    connection.commit()
    print("Funcionário atualizado com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    cursor.close()
    connection.close()
