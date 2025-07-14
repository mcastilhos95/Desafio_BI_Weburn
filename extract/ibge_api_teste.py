import requests
import pandas as pd
import time

def get_populacao_estimada_ibge():
    estados = [
        {'sigla': 'AC', 'id': 12}, {'sigla': 'AL', 'id': 27}, {'sigla': 'AP', 'id': 16},
        {'sigla': 'AM', 'id': 13}, {'sigla': 'BA', 'id': 29}, {'sigla': 'CE', 'id': 23},
        {'sigla': 'DF', 'id': 53}, {'sigla': 'ES', 'id': 32}, {'sigla': 'GO', 'id': 52},
        {'sigla': 'MA', 'id': 21}, {'sigla': 'MT', 'id': 51}, {'sigla': 'MS', 'id': 50},
        {'sigla': 'MG', 'id': 31}, {'sigla': 'PA', 'id': 15}, {'sigla': 'PB', 'id': 25},
        {'sigla': 'PR', 'id': 41}, {'sigla': 'PE', 'id': 26}, {'sigla': 'PI', 'id': 22},
        {'sigla': 'RJ', 'id': 33}, {'sigla': 'RN', 'id': 24}, {'sigla': 'RS', 'id': 43},
        {'sigla': 'RO', 'id': 11}, {'sigla': 'RR', 'id': 14}, {'sigla': 'SC', 'id': 42},
        {'sigla': 'SP', 'id': 35}, {'sigla': 'SE', 'id': 28}, {'sigla': 'TO', 'id': 17}
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    dados_populacao = []

    for estado in estados:
        url = f"https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/{estado['id']}"
        print(f"Buscando dados de: {estado['sigla']}")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            populacao = data['projecao']['populacao']
            dados_populacao.append({
                'estado': estado['sigla'],
                'id': estado['id'],
                'populacao_estimada': populacao
            })
        else:
            print(f"Erro ao buscar dados de {estado['sigla']}: Status {response.status_code}")
        time.sleep(0.5)

    df_ibge = pd.DataFrame(dados_populacao)
    return df_ibge

if __name__ == "__main__":
    df_ibge = get_populacao_estimada_ibge()
    print(df_ibge)
