# Desafio BI: Projeto de ETL com Dados de COVID-19 e População

Este projeto tem como objetivo aplicar um fluxo completo de **ETL (Extract, Transform, Load)** utilizando dados públicos do Brasil relacionados à COVID-19 e à população dos estados, através de APIs do Brasil.io e do IBGE.

## 🗂 Estrutura do Projeto

```
desafio_bi/
│
├── extract/
│   ├── covid_api.py       # Extração de dados da API Brasil.io (COVID-19)
│   └── ibge_api.py        # Extração de dados da API IBGE (População)
│
├── transform/
│   └── tratamentos_APIs.py  # Tratamento e normalização dos dados extraídos
│
├── load/
│   └── load.py            # Carregamento dos dados no banco de dados SQLite
│
├── main.py                # Arquivo principal que orquestra o processo ETL
├── dados.db               # Banco SQLite gerado com os dados processados
└── README.md              # Documentação do projeto
```

## 📦 Requisitos

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `requests`

Instale os pacotes necessários com:

```bash
pip install pandas requests
```

## 🚀 Como Executar

1. Clone este repositório ou baixe os arquivos.
2. No terminal, acesse o diretório do projeto.
3. Execute o script principal:

```bash
python main.py
```

Isso irá:

- Extrair os dados da API Brasil.io e da API do IBGE.
- Tratar e normalizar os dados.
- Salvar os dados tratados no arquivo `dados.db` (SQLite), com as tabelas `covid` e `populacao`.

## 🔐 Autenticação: API do Brasil.io

Para acessar os dados da API do Brasil.io, é necessário possuir um **token de autenticação**. Siga os passos abaixo para gerar o seu:

1. Acesse o site: [https://brasil.io/](https://brasil.io/)
2. Crie uma conta gratuita.
3. Vá até o seu perfil e copie o seu **token de acesso**.
4. No arquivo `covid_api.py`, substitua o valor da variável `token` pela sua chave pessoal:

```python
token = "SUA_CHAVE_AQUI"
```

> ⚠️ **Atenção**: Por segurança, nunca compartilhe seu token publicamente ou deixe salvo em repositórios públicos. Em projetos reais, o ideal é usar variáveis de ambiente com a biblioteca `python-dotenv` para proteger essas informações sensíveis.

## 🔗 Fontes de Dados

- [Brasil.io – Dados COVID-19](https://brasil.io/dataset/covid19/caso/)
- [IBGE – API de agregados populacionais](https://servicodados.ibge.gov.br/api/docs/agregados/)

## 📊 Saída

O banco gerado (`dados.db`) conterá:

- **covid**: Casos e óbitos por estado e por data.
- **populacao**: População estimada dos estados de 2020 a 2024.

## 🧠 Funcionalidades

- Paginação automática para extrair todos os dados da API Brasil.io
- Normalização e tratamento de dados faltantes
- Conversão de tipos e padronização de nomes
- Criação e substituição de tabelas em banco SQLite

## 📌 Observações

- O projeto foi desenvolvido com fins educacionais.
- Pode ser expandido para uso em dashboards no Power BI ou aplicações web.


## 👨‍💻 Autor

Matheus Castilhos  
Analista de Dados 
