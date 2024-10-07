# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2ef738d-6972-3253-973c-ed6cd4c3b81c | -22.53996 | -48.81583 | 2024-10-07 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1df872fd-33f1-3af4-90cc-9762244e48d6 | -22.53781 | -48.8139 | 2024-10-07 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feaef08e-5b8d-3844-a45e-ddfa37b1fd55 | -23.26546 | -49.45299 | 2024-10-07 04:04:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b8e60683-56b4-346a-963b-0b70842417c4 | -23.14436 | -49.8117 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 709fca09-d318-3559-a4ab-5284651947a3 | -23.14361 | -49.81547 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b1ec5ed-41ec-342f-ac87-0ce5f063e992 | -23.14288 | -49.81918 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b8b48f35-3dd8-3b6c-acc4-c2166293319e | -23.14024 | -49.81071 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ed23f117-7df7-3c15-b661-fb6517b9e2db | -23.1395 | -49.81443 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32a96f84-d4a9-36c7-bbd0-77fbf5c4c9a4 | -23.13878 | -49.81806 | 2024-10-07 04:04:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8a53937-3151-35c1-bee0-b0c28780490f | -23.05618 | -49.68219 | 2024-10-07 04:04:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bcb4d6e-4d7a-385b-84cb-102d607af43d | -23.04054 | -49.84877 | 2024-10-07 04:04:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c8ab714d-160a-3bc8-8510-e43cc78d3cb4 | -23.03973 | -49.85286 | 2024-10-07 04:04:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 9588737f-d791-34c2-9933-82c0aaf43d1b | -24.06435 | -50.28923 | 2024-10-07 04:04:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ee41ef4-91af-357f-be82-e252605428ff | -23.81043 | -50.13496 | 2024-10-07 04:04:00 | NOAA-20 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b4bc1daa-0cc6-337a-bdbb-b27ce929c345 | -19.16434 | -50.63525 | 2024-10-07 04:04:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d3835e5-19f5-30c5-b19f-9e7980c45d27 | -19.16326 | -50.64057 | 2024-10-07 04:04:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 04724fe8-e031-34bb-82be-4a697e5ad2c8 | -19.16218 | -50.64592 | 2024-10-07 04:04:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a1f4ced-d21f-31af-b8e6-d3a4dd33d063 | -19.15964 | -50.63428 | 2024-10-07 04:04:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7b15fc3-8ebb-3e94-8cca-2c499d8daf39 | -20.18855 | -50.96477 | 2024-10-07 04:04:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1e99c7a5-5a42-3d12-bc53-e38f2d67ae6c | -21.19704 | -50.98156 | 2024-10-07 04:04:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 58d6d063-2e46-3198-b8ff-c5e18193f8fd | -23.05743 | -51.4547 | 2024-10-07 04:04:00 | NOAA-20 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 87b483e2-426a-32a8-b7bb-ae61cdda9e7a | -23.05634 | -51.45998 | 2024-10-07 04:04:00 | NOAA-20 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b2d5563a-6768-3085-b8d4-a46c95c6af07 | -23.05288 | -51.45354 | 2024-10-07 04:04:00 | NOAA-20 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 445ef7e6-ce52-3e5b-92d0-cefe7b17276a | -23.05178 | -51.45881 | 2024-10-07 04:04:00 | NOAA-20 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1c74b2d6-0246-3c71-88bf-4a05aac0aa8e | -24.24195 | -50.74082 | 2024-10-07 04:04:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7308b6e7-e6d1-3c1c-aa7a-8f5e44ee3163 | -25.62162 | -51.42857 | 2024-10-07 04:04:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d2210c3a-72c6-3723-a0e8-b4516b4e9b4b | -25.62066 | -51.43328 | 2024-10-07 04:04:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ba084163-d5ba-31ec-95f2-00f69908c7fc | -25.35019 | -51.26042 | 2024-10-07 04:04:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7e9729b4-25a8-3215-9220-ba49efb1a4cd | -19.39478 | -51.68682 | 2024-10-07 04:04:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d91eb551-8fd4-3a6d-be6c-45c5e89399d7 | -19.39414 | -51.68987 | 2024-10-07 04:04:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3d1ea1e-2a9d-3fa4-a589-1f3c92764c05 | -22.71687 | -53.22823 | 2024-10-07 04:04:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c71e068b-1cbc-3271-a3fa-8bd8e5076829 | -22.71175 | -53.22691 | 2024-10-07 04:04:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 899314de-ebfc-32ad-b2ed-3f40f0859945 | -22.71103 | -53.23025 | 2024-10-07 04:04:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 11b83108-d5cd-3984-811c-7a69235c31c2 | -22.7103 | -53.23358 | 2024-10-07 04:04:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| d614fba0-33bd-3488-b3f1-90d3bb47bc5e | -18.46665 | -53.51246 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c42db15a-f402-370a-877d-50dba198fe01 | -18.46559 | -53.5173 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8556f353-b783-3f56-9d93-cf2e8b86fa6b | -18.46458 | -53.52196 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f92c8731-36eb-3d61-9573-30a0bb3069d9 | -18.46283 | -53.5026 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5fdcc53-2413-364e-afc2-0aebd42ba7a8 | -18.46183 | -53.50721 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e46c110-de59-36bb-9f4c-c124cc71bf0f | -18.46082 | -53.5118 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35d8e6bf-528a-378f-94e9-636617805ee8 | -18.45984 | -53.51634 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1716e49c-dcf1-3799-bcdf-67a83ecbe360 | -18.45886 | -53.52079 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a4d87ad3-286d-3599-a490-6d1dad05176a | -18.45813 | -53.49685 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7bf3e45-a3b1-373a-b45c-664830f31f66 | -18.45792 | -53.52511 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe425c49-aff3-3041-80de-c231b2f531b5 | -18.45705 | -53.50175 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a6c868e-1050-32eb-9364-c720b3671a16 | -18.45601 | -53.50655 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5385e97a-2f44-31ec-acec-44d05c83a1aa | -18.45503 | -53.51103 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cad061da-3643-35c6-bf93-777a31f4b300 | -18.45408 | -53.51535 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e13bcc7-16ad-3ed2-9bd8-8f777a9ee4be | -18.45316 | -53.51955 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e697c93d-907f-3cb7-a3b7-916f330f09cc | -18.45137 | -53.50048 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 196c7279-953d-3a74-9189-576dba0498b7 | -18.4503 | -53.50534 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a41bf133-55fd-3182-be68-fd392f35562e | -18.44937 | -53.50959 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 086df806-7573-37fb-809e-f7b37641a2e3 | -18.44846 | -53.51376 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97a7c827-3e55-308d-b684-7bb6452f93a2 | -18.44371 | -53.50821 | 2024-10-07 04:04:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cb304d7-498f-314c-a964-34275cc12f5e | -21.39419 | -57.2634 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8d97fbe-f39f-393a-8f7b-69c16dba0df0 | -18.70982 | -57.30481 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 122cc450-5948-3a01-b1cb-0a9abd994ff6 | -18.89814 | -54.53884 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75263a7c-fdeb-3a61-97f7-f445a0fc4081 | -18.89423 | -54.55628 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ce47bcc-2fff-37a6-96ff-67cc13e4e04e | -18.89316 | -54.56107 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5d17d97-1c28-302a-a20d-0e8c6336aaea | -18.89236 | -54.48059 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 60122c1f-c3e0-36fc-9257-ed9f47661f53 | -18.89223 | -54.56517 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b371e724-a387-39f0-9a3d-9a74e0e4da5f | -18.89193 | -54.53844 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29d627c0-f984-3fb6-9582-bdccdb3ad7cc | -18.89142 | -54.48477 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9c6600ef-1e32-3e4e-94c7-9758d34be6ef | -18.89062 | -54.54428 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ed36356-d037-3dcb-bd39-bbc8cbce782c | -18.89038 | -54.48938 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 98bd4099-712c-379d-adfc-ae12049ed09e | -18.88931 | -54.5501 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9a83781-74a5-3f2c-ac73-29fde6febd7c | -18.88914 | -54.4949 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5bac1ac6-f988-373b-8161-97c6a7c2232e | -18.88628 | -54.47972 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 914beade-9484-3e9c-809c-c093531d4483 | -18.88618 | -54.56401 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50d582cf-a895-344d-8bae-70deb46dfd23 | -18.88526 | -54.5681 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c69f7b1e-a018-31ac-a5eb-f9688f1ab2c2 | -18.88425 | -54.57257 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a0308790-f8a1-3209-a0b6-f96e9f38cd22 | -18.87819 | -54.57141 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ea36ddb-0ba1-3823-88f5-6b6e46ce2446 | -18.87702 | -54.57664 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d96151b-a0c9-3d3e-8ee4-39b2c76b2d22 | -18.87429 | -54.56071 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 773e163f-ecff-32ba-b88f-7ff2b93ab998 | -18.87328 | -54.5652 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 133c3ee5-bd2a-3203-90d0-08877d1f11b9 | -18.87204 | -54.57068 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd790da8-76a6-3b8d-8f93-67fa6eebe4da | -18.8682 | -54.55974 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 671d528b-73df-31b2-8a81-b9491d97fa65 | -18.86712 | -54.5645 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4315c875-bde1-3346-92a9-09dfc05a0566 | -18.86646 | -54.56118 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0176e2b-98a7-3068-a1bb-bba4fb6ae7e2 | -18.86588 | -54.56997 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 82640f83-fc96-3b62-825e-4f5c1d28f5f7 | -18.8642 | -54.57151 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9103f5a2-f72d-30a6-8b8b-ab61bd6cbce2 | -18.86197 | -54.55936 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2557d5d9-641b-3623-bf13-0aa6cb912342 | -18.86088 | -54.56414 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fd374ea-42b8-3d5e-972c-1cfd6910bd7e | -18.85981 | -54.56889 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a0ad505-636e-3596-b065-b995e1eaeded | -18.85924 | -54.56537 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 036f0948-eb91-3082-b4b6-15e995c055e1 | -18.8582 | -54.57007 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a376f282-095e-3039-a89b-b1cc030956f1 | -18.85384 | -54.56733 | 2024-10-07 04:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db8f34d8-81cd-3ea1-815d-00eb3c61b7f7 | -20.24818 | -54.79494 | 2024-10-07 04:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f9d71fb-58c6-3501-82fc-0b47945c1a53 | -20.07056 | -54.53679 | 2024-10-07 04:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cbd38d7-839e-36f4-be33-add91aa5b700 | -20.06955 | -54.54123 | 2024-10-07 04:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9574c935-5091-3ea5-b29c-ea4a807ccf42 | -20.06726 | -54.53428 | 2024-10-07 04:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63478fd7-279b-33c7-996a-21cf7ecc763a | -20.0663 | -54.5386 | 2024-10-07 04:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3c35c7d-d147-3ce5-8d77-53179ca28eac | -20.0646 | -54.53586 | 2024-10-07 04:04:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88c217de-670f-3d09-a42d-965be7a08f37 | -21.33463 | -54.6517 | 2024-10-07 04:04:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fcd9714-e5ad-373b-9e1a-ca98acf316b9 | -21.33439 | -54.65382 | 2024-10-07 04:04:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2d784bc-774b-3bd7-ae9a-ac417df95445 | -21.33361 | -54.6561 | 2024-10-07 04:04:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd6139a4-def1-335b-811c-fe1a1e349082 | -21.39845 | -57.25793 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b0a9943c-e5c7-30de-bccc-fc49fece4dda | -21.39765 | -57.249 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d64c07f-e51f-3a69-a7c4-88a5b9ee3f24 | -21.39651 | -57.2658 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f6a78c41-dad1-3649-8987-078542982a64 | -21.39601 | -57.25583 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README72.md)
