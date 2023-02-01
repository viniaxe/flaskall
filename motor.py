from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/entrar", methods=['POST', 'GET'])
def entrar():

    nome = request.form['nome']
    return render_template("cadastrar.html", msg=nome)

@app.route('/listar')
def listar():

    return render_template("listar.html")

if __name__ == '__main__':
    app.run(debug=True)