DROP TABLE IF EXISTS covid;
DROP TABLE IF EXISTS populacao;

CREATE TABLE covid (
    city TEXT,
    confirmed INTEGER,
    city_ibge_code TEXT,
    confirmed_per_100k_inhabitants REAL,
    date TEXT,
    death_rate REAL,
    deaths INTEGER,
    estimated_population INTEGER,
    estimated_population_2019 INTEGER,
    is_last BOOLEAN,
    order_for_place INTEGER,
    place_type TEXT,
    state TEXT
);

CREATE TABLE populacao (
    ID TEXT,
    Sigla TEXT,
    Nome TEXT,
    Pop_2020 INTEGER,
    Pop_2021 INTEGER,
    Pop_2022 INTEGER,
    Pop_2023 INTEGER,
    Pop_2024 INTEGER
);
