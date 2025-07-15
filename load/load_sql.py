import sqlite3

def executar_script_sql(arquivo_sql, conexao):
    with open(arquivo_sql, 'r', encoding='utf-8') as f:
        script = f.read()
    conexao.executescript(script)

def testar_criacao_banco():
    conn = sqlite3.connect("dados.db")
    executar_script_sql("create_tables.sql", conn)  # arquivo está na mesma pasta do script
    print("Script SQL executado com sucesso. Tabelas criadas.")
    conn.close()

if __name__ == "__main__":
    testar_criacao_banco()
