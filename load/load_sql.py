import sqlite3

def executar_script_sql(arquivo_sql, conexao):
    with open(arquivo_sql, 'r', encoding='utf-8') as f:
        script = f.read()
    conexao.executescript(script)

def salvar_no_banco(df_covid, df_ibge):
    conn = sqlite3.connect("dados.db")

    # Executa o script SQL para criar as tabelas com esquema definido
    executar_script_sql("load/create_tables.sql", conn)  # ajuste caminho se necessário

    # Insere os dados mantendo o esquema criado
    df_covid.to_sql("covid", conn, if_exists="replace", index=False)
    df_ibge.to_sql("populacao", conn, if_exists="replace", index=False)

    conn.close()