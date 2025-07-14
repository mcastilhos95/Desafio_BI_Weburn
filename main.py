from extract.covid_api import extrair_dados_covid
from extract.ibge_api import extrair_dados_ibge
from transform.tratamentos_APIs import tratar_dados_covid, tratar_dados_ibge
from load.load import salvar_no_banco


def main():
    df_covid = extrair_dados_covid()
    df_ibge = extrair_dados_ibge()

    df_covid_tratado = tratar_dados_covid(df_covid)
    df_ibge_tratado = tratar_dados_ibge(df_ibge)

    salvar_no_banco(df_covid_tratado, df_ibge_tratado)

if __name__ == "__main__":
    main()
