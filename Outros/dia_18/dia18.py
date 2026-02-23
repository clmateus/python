# %%
from flask import Flask

# 1. Criar o aplicativo
app = Flask(__name__)

# 2. Criar a Rota (O endereço do site)
@app.route("/") 
def homepage():
    return "Olá, Mundo! Este é meu primeiro site em Python."

@app.route("/contatos")
def contatos():
    return "Fale comigo: email@exemplo.com"

@app.route("/ola/<nome>")
def ola_usuario(nome):
    return f"Olá, {nome}! Seja bem-vindo ao meu site."

@app.route("/perfil/<usuario>/<profissao>")
def perfil(usuario, profissao):
    return f"<h1>Perfil de {usuario}</h1> <p>Profissão atual: {profissao}</p>"

# 3. Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
# %%
