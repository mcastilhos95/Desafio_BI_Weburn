import sqlite3


def salvar_no_banco(df_covid, df_ibge):
    conn = sqlite3.connect("dados.db")

    df_covid.to_sql("covid", conn, if_exists="replace", index=False)
    df_ibge.to_sql("populacao", conn, if_exists="replace", index=False)

    conn.close()