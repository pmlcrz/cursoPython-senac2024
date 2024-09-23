from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração do MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="compravenda"
)


# Rota para a página inicial de produtos
@app.route("/")
def index():
    return render_template("indexp.html")



# Rota para a página com a lista de produtos
@app.route("/indexp-data")
def indexp_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    cursor.close()
    return render_template("indexp-data.html", produtos=produtos)


# Rota para adicionar produto
@app.route("/adicionar", methods=["POST"])
def adicionar_produto():
    nomeproduto = request.form["nomeproduto"]
    qtd = request.form["qtd"]
    valor = request.form["valor"]


    cursor = conn.cursor()
    query = "INSERT INTO produto (nomeproduto, qtd, valor) VALUES (%s, %s, %s)"
    cursor.execute(query, (nomeproduto, qtd, valor))
    conn.commit()
    cursor.close()

    return redirect("/")


# Rota para atualizar produto
@app.route("/atualizar", methods=["POST"])
def atualizar_produto():
    codproduto = request.form["codproduto"]
    nomeproduto = request.form["nomeproduto"]
    qtd = request.form["qtd"]
    valor = request.form["valor"]


    cursor = conn.cursor()
    query = "UPDATE produto SET nomeproduto=%s, qtd=%s, valor=%s WHERE codproduto=%s"
    cursor.execute(query, (nomeproduto, qtd, valor, codproduto))
    conn.commit()
    cursor.close()

    return redirect("/indexp-data")


# Rota para excluir produto
@app.route("/excluir/<int:codproduto>")
def excluir_produto(codproduto):
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE codproduto=%s"
    cursor.execute(query, (codproduto,))
    conn.commit()
    cursor.close()

    return redirect("/indexp-data")


if __name__ == "__main__":
    app.run(debug=True)