import requests
import pandas as pd
import time


def extrair_dados_covid():
    url = "https://brasil.io/api/dataset/covid19/caso/data/"
    params = {
        "place_type": "state"
    }

    token = "5f7a0cdb1eb8a308ff34357836056a91af8fc068"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": f"Token {token}"
    }

    dados = []

    while url:
        print(f"Buscando dados de: {url}")
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            print(response.text)
            break

        data = response.json()

        if 'results' in data and 'next' in data:
            dados.extend(data['results'])
            url = data['next']
            params = None
        else:
            print("Resposta inesperada ou final da paginação:", data)
            break

        time.sleep(1)

    df = pd.DataFrame(dados)

    print(df.head())
    print(f"\nTotal de registros: {len(df)}")

    return df
