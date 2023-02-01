from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadpage")
def cadpage():

    con = mysql.connector.connect(
        host='containers-us-west-192.railway.app',
        user='root',
        password='yH5J1Z1FT02U0vxtKcXT',
        database='railway',
    )

    cur = con.cursor()
    cur.execute("select * from estados")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return render_template("cadastrar.html", rows=rows)

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():

    con = mysql.connector.connect(
        host='containers-us-west-192.railway.app',
        user='root',
        password='yH5J1Z1FT02U0vxtKcXT',
        database='railway',
    )
    cur = con.cursor()
    cur.execute("select * from estados")
    rows = cur.fetchall()

    msg = ""
    if request.method == 'POST':

        nome = request.form['nome']

        if nome > "":

            try:
                idade = request.form['idade']
                telefone = request.form['telefone']
                estado = request.form['estado']

                cur.execute("INSERT INTO pessoas (nome, idade, telefone, estado) VALUES(?, ?, ?, ?)", (nome, idade, telefone, estado))
                con.commit()
                msg = nome.upper() + " cadastrado com SUCESSO!!!"

            except:
                con.rollback()
                msg = "OCORREU UM ERRO DE CADASTRO!"
                cur.close()
                con.close()

            finally:
                cur.close()
                con.close()
                return render_template("cadastrar.html", msg=msg, rows=rows)

        else:
            cur.close()
            con.close()
            return render_template("cadastrar.html", msg="PREENCHA PELO MENOS O NOME!!!", rows=rows)

@app.route('/listar')
def listar():

    con = mysql.connector.connect(
        host='containers-us-west-192.railway.app',
        user='root',
        password='yH5J1Z1FT02U0vxtKcXT',
        database='railway',
    )

    cur = con.cursor()
    cur.execute("select * from pessoas")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return render_template("listar.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True)