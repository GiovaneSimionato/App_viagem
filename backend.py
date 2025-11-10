import sqlite3

# Conectar ou criar o banco de dados
def conectar():
    conexao = sqlite3.connect("viagem.db")
    cursor = conexao.cursor()

    # Criar tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS despesas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL
        )
    """)
    conexao.commit()
    return conexao, cursor


# Inserir despesa
def inserir(categoria, descricao, valor):
    conexao, cursor = conectar()
    cursor.execute("INSERT INTO despesas (categoria, descricao, valor) VALUES (?, ?, ?)",
                   (categoria, descricao, valor))
    conexao.commit()
    conexao.close()


# Listar todas as despesas
def listar():
    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM despesas")
    dados = cursor.fetchall()
    conexao.close()
    return dados


# Deletar despesa pelo ID
def deletar(id_item):
    conexao, cursor = conectar()
    cursor.execute("DELETE FROM despesas WHERE id = ?", (id_item,))
    conexao.commit()
    conexao.close()


# Atualizar orçamento total (armazenamos em outra tabela)
def atualizar_orcamento(valor):
    conexao, cursor = conectar()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orcamento (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            valor REAL NOT NULL
        )
    """)
    cursor.execute("INSERT OR REPLACE INTO orcamento (id, valor) VALUES (1, ?)", (valor,))
    conexao.commit()
    conexao.close()


# Pegar valor do orçamento atual
def pegar_orcamento():
    conexao, cursor = conectar()
    cursor.execute("SELECT valor FROM orcamento WHERE id = 1")
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado else 0.0


# Calcular total de despesas
def total():
    conexao, cursor = conectar()
    cursor.execute("SELECT SUM(valor) FROM despesas")
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado[0] is not None else 0.0