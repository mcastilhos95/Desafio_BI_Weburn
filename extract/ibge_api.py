import requests
import pandas as pd

def extrair_dados_ibge():
    # 1. Obter siglas e nomes dos estados
    url_estados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    estados = requests.get(url_estados).json()
    mapa_estados = {
        str(uf["id"]): {"sigla": uf["sigla"], "nome": uf["nome"]}
        for uf in estados
    }

    # 2. Obter população de 2020 a 2024
    anos = "2020|2021|2022|2023|2024"
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/{anos}/variaveis/9324?localidades=N3[all]"
    response = requests.get(url)
    dados_pop = response.json()

    series = dados_pop[0]["resultados"][0]["series"]

    tabela = []
    for item in series:
        local = item["localidade"]
        id_uf = local["id"]
        nome_uf = local["nome"]
        sigla = mapa_estados.get(id_uf, {}).get("sigla", "??")

        linha = {
            "ID": id_uf,
            "Sigla": sigla,
            "Nome": nome_uf
        }

        for ano in range(2020, 2025):
            valor = item["serie"].get(str(ano))
            linha[f"Pop_{ano}"] = int(float(valor)) if valor else None

        tabela.append(linha)

    df = pd.DataFrame(tabela)
    df = df.sort_values("ID").reset_index(drop=True)

    return df
