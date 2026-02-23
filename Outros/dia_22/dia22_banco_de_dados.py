import sqlite3

# 1. Conectar ao banco (se não existir, ele cria o arquivo banco.db)
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# 2. Criar a Tabela 'mensagens'
# Ela terá 3 colunas: id, nome, texto
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mensagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        comentario TEXT NOT NULL
    )
""")

print("Banco de dados criado com sucesso!")
conexao.commit() # Salvar as alterações
conexao.close()