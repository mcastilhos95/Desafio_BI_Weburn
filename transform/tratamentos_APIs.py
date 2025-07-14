import pandas as pd


def tratar_dados_covid(df):
    df = df.copy()

    # Normalizar
    df['state'] = df['state'].str.upper().str.strip()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Preencher nulos em casos e óbitos
    if 'confirmed' in df.columns:
        df['confirmed'] = df['confirmed'].fillna(0).astype(int)
    elif 'casos_confirmados' in df.columns:
        df['casos_confirmados'] = df['casos_confirmados'].fillna(0).astype(int)

    if 'deaths' in df.columns:
        df['deaths'] = df['deaths'].fillna(0).astype(int)
    elif 'obitos' in df.columns:
        df['obitos'] = df['obitos'].fillna(0).astype(int)

    # Remover duplicatas
    df = df.drop_duplicates()

    return df


def tratar_dados_ibge(df):
    df = df.copy()

    # Normalizar
    df['Sigla'] = df['Sigla'].str.upper().str.strip()
    df['Nome'] = df['Nome'].str.title().str.strip()

    # Tratar valores nulos nas populações
    pop_cols = [col for col in df.columns if col.startswith('Pop_')]
    for col in pop_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Remover duplicatas
    df = df.drop_duplicates()

    return df
