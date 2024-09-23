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
    'Teste 2',
    '999.222.333-44',
    'Rua tal',
    '1998-05-01',
    4
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
