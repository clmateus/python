# %%
from flask import Flask, render_template

app = Flask(__name__)

# Rota da Página Inicial
@app.route("/")
def homepage():
    # O Flask procura o 'index.html' automaticamente dentro da pasta 'templates'
    nome_usuario = 'Mateus'
    return render_template("index.html", nome=nome_usuario)

# Rota da Página Sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# Rota de Contato (simples, sem HTML, só para testar)
@app.route("/contato")
def contato():
    return "<h1>Página de Contato em Construção...</h1>"

if __name__ == "__main__":
    app.run(debug=True)
# %%
