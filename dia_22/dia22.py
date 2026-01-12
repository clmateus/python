from flask import Flask, render_template, request, redirect
import sqlite3

# Blindagem de conexão com o banco
# def get_db_connection():
#     try:
#         conn = sqlite3.connect('banco.db')
#         return conn
#     except sqlite3.OperationalError:
#         # Se o banco não existir ou der erro, o Python cai aqui
#         return None

# @app.route("/", methods=["GET", "POST"])
# def index():
#     conn = get_db_connection()
    
#     # Verificação de segurança
#     if conn is None:
#         return "<h1>Erro Crítico: Banco de Dados não encontrado. Contate o administrador.</h1>"

app = Flask(__name__)

# Tratamento de erros personalizados
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    # Note que retornamos o número 404 junto com o template
    return render_template("404.html"), 404

@app.errorhandler(500)
def erro_servidor(erro):
    return "<h1>Erro interno do servidor. Tente novamente mais tarde.</h1>", 500

# Função auxiliar para conectar no banco (evita repetição de código)
def get_db_connection():
    conn = sqlite3.connect('banco.db')
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    
    # SE O USUÁRIO ENVIOU O FORMULÁRIO (POST)
    if request.method == "POST":
        # Pega os dados pelo 'name' do HTML
        nome_usuario = request.form["nome"]
        comentario_usuario = request.form["comentario"]
        
        # Insere no SQL (Atenção aos pontos de interrogação para segurança)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mensagens (nome, comentario) VALUES (?, ?)", 
                       (nome_usuario, comentario_usuario))
        conn.commit()
        
        # Limpa a conexão e recarrega a página para evitar envio duplicado
        conn.close()
        return redirect("/")

    # SE O USUÁRIO SÓ ACESSOU A PÁGINA (GET)
    # Vamos ler todas as mensagens para mostrar na tela
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mensagens ORDER BY id DESC") # DESC = Do mais novo pro mais velho
    mensagens_banco = cursor.fetchall()
    conn.close()
    
    return render_template("index.html", lista_mensagens=mensagens_banco)

if __name__ == "__main__":
    app.run(debug=True)