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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4b445d7-2c5f-3c85-b8a5-bd39d1121ae2 | -2.40893 | -57.89912 | 2026-09-03 04:55:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79374dac-e62b-369b-8dbe-aff2a8d67ac2 | -3.59493 | -55.37407 | 2026-09-03 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ea3a6fb-79a5-3eed-baee-6cab353e3f45 | -1.09356 | -48.05787 | 2026-09-03 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eac9b902-d8e8-39e8-8db1-7159a3673cc1 | -3.81573 | -50.10979 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0ee5d7f-c651-3f3e-9e38-37a66e3e931a | -3.59132 | -55.37349 | 2026-09-03 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c0b0be7-7318-33b0-a755-768a93122c21 | -3.60021 | -49.56367 | 2026-09-03 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844cda3b-8109-36d9-9713-c0170ab13636 | -3.24962 | -47.24962 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 0b14b366-e445-3d0b-b6d8-6ef613d3bf6b | 2.02847 | -55.87595 | 2026-09-03 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bda57c6-390c-3987-ad50-33ad464684f9 | -3.44775 | -56.31969 | 2026-09-03 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ad059b9-95a0-3e22-8cec-0c2a491c32dd | -1.02892 | -53.72227 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea5dbc0-6898-3c5f-a790-a91f0a33bc39 | -3.18314 | -48.01913 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2df3415-4984-3eef-9639-8706dd6643ab | -1.27355 | -55.71857 | 2026-09-03 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5b69574-5e6a-3aad-a1f9-cff6a2b66606 | -3.21631 | -48.81521 | 2026-09-03 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6e7f2b-2791-3490-ac85-0a6851991716 | -3.37549 | -52.79661 | 2026-09-03 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d81a0bd-5cf0-3bbb-ba47-85d0ee478d58 | -1.02088 | -53.72838 | 2026-09-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08f58911-1058-3d12-b0e0-9b509f94d535 | -1.97645 | -50.79607 | 2026-09-03 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54177057-d7c1-3f93-b707-33464f6f2574 | -3.2491 | -47.25305 | 2026-09-03 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| fee1fe66-fc84-3da9-84ac-336417351c88 | -0.16608 | -50.40608 | 2026-09-03 04:55:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce3acd8f-c4cb-3ebd-997a-c45d78ffc6e4 | -4.17475 | -42.44049 | 2026-09-03 04:55:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 56e138b0-363e-3216-ba12-fcf4ebcc897f | -1.79556 | -47.95164 | 2026-09-03 04:55:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b50d85-d155-3aea-99bd-2c7412ef8260 | -4.11044 | -51.02565 | 2026-09-03 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a461331-742a-34c1-ba5d-1154fc4c0393 | -3.02752 | -61.4903 | 2026-09-03 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4593b93-8866-31a6-af82-56b10b4963ec | -6.26007 | -55.42893 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bf3830f-db8b-3a3b-a0bf-20a0e9b1dae3 | -8.0753 | -50.96224 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 39e4a966-9acb-3d2a-ac69-cbf30e34eef6 | -6.7707 | -59.43353 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 330bd623-f5b2-34a5-9259-38bf0ec3ddfa | -8.79111 | -54.58619 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92d04597-2d0f-307d-9c82-43c5dbb3be5d | -5.5669 | -60.17867 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3da80f94-9304-3ef0-888f-704dde55ab11 | -6.06962 | -53.67195 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e189540-d802-361b-a02b-9b18aa297e1a | -10.89953 | -45.32865 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eff574fc-70f3-30a4-95eb-447a2d2727d0 | -11.28932 | -45.17722 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ede5f41-acfb-30a2-aa0f-786d48bfe9b1 | -6.14441 | -55.6692 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85abad83-0da1-33f3-bff0-673c4e409ed6 | -5.80025 | -43.64621 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea2bfe30-7f19-3c00-b008-c0f4b6927c1a | -7.04099 | -59.2243 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ff35c0f-ad7d-30a4-a8bb-8a290693210b | -6.04476 | -53.44512 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c51dad6-ff47-342e-aad1-f717937f6bf3 | -11.31335 | -50.51965 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0c956fda-58cf-3a65-a745-4c949dff355c | -8.07858 | -50.95422 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f4e6d6c-1a7a-35cb-be64-b9278536a44f | -8.46913 | -54.67753 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f6f00d-6b02-35e4-a8ae-04c0b08ced6d | -5.97813 | -53.58492 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6cda689-4d0b-37c9-8c9a-8f4b6ece0ad2 | -5.98146 | -53.58546 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0195a55-6bef-3cee-bb7e-05b4ecbf182b | -3.38474 | -59.42606 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d97968e9-0707-3205-9f1b-29520d02d759 | -9.7038 | -57.88734 | 2026-09-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45e436b0-d526-3c9f-b003-921e214ba275 | -10.88156 | -45.30759 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b585abe3-0921-3f40-8a8b-431a4426673e | -6.764 | -59.44594 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4e394f9-8128-3477-9b8a-b0bc55531e6f | -10.88545 | -45.31747 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2f8a743-fe3a-30df-a10d-1689df7ab53f | -6.19006 | -55.27791 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be6a8636-7dd7-3c5e-830c-0ca252df2d98 | -9.73952 | -58.40243 | 2026-09-03 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3dfa93a-9120-3d7c-9073-9b5dd9d4d8f6 | -8.08089 | -50.96238 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d7f50b7-341b-3a25-bc40-a04414984b52 | -8.45402 | -54.67503 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b90f883-9082-3cf0-92e3-a372e48fe519 | -8.71599 | -52.36055 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72de00cb-31c2-37d6-8f43-5e3139e5c237 | -6.11075 | -59.96229 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b30bed-e80f-3144-92a1-02c16ae71358 | -7.05478 | -59.22241 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd3ec92-b092-3e4e-b5be-b481a2f44381 | -6.49175 | -53.60263 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc7d75c-bc59-3c1e-aa6f-23fc333a62c2 | -8.43311 | -54.69754 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fd6a0ac-5278-3e5b-84b3-f423afb4bd6c | -6.76506 | -56.3339 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46090e5b-0e8f-3e05-b114-cf05c431fb4b | -6.32296 | -54.75535 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 086b1c1c-02ca-396f-b90d-6ca286c2ce38 | -8.07281 | -50.96897 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0925fbc-d7a5-3e1b-bcf6-320fbc43c515 | -6.42799 | -55.53288 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fd3c066-f4b5-362f-98c2-dfae814ba6af | -9.0193 | -65.72763 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a93079-924f-3a14-a4b7-84887e1868a8 | -10.18397 | -50.28019 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3fd5776-0082-31bc-9add-0821ea971206 | -7.07608 | -44.35727 | 2026-09-03 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1eaac1f-d433-3b0b-a65a-7182eebe56ee | -11.30603 | -50.51855 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1295bf1f-c876-39bb-9674-5c7792624b46 | -6.30811 | -56.03761 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d3e87f0-1da5-377e-bf7d-37bf1b9b7fde | -4.26815 | -55.15593 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aae7fdd9-99b3-338b-bc2a-ba3c44a02a14 | -6.77383 | -56.4135 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20051168-2a1e-3f08-8403-583c7f085daa | -8.07471 | -50.96606 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f2584da-0f44-3e44-8f3d-47d30773e270 | -8.61951 | -54.847 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e214d5-b99a-3169-ac9c-4afe4e0e0f2b | -8.4676 | -54.65506 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c0635eb-4890-3b28-bc08-78c3edf30640 | -7.72182 | -61.12296 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e704374a-6675-3442-957d-f30327ab367c | -7.05113 | -59.21737 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30085968-af06-3def-b3b2-a15b0f6fd6f2 | -6.25718 | -55.42448 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb90df8f-8e71-37be-98d9-d3bfe04559b9 | -6.36456 | -55.23279 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9cce34c-9bab-3b5a-bbe5-40a90fce2b65 | -8.46854 | -54.68113 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18dfb45f-ac6a-3cf8-8c8f-4129e140e8b2 | -8.26322 | -54.94716 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fbebab2-00bb-35dc-88f2-308ea432749c | -6.31172 | -56.03823 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6502fdad-6e04-3cd1-9308-e9d96f5c5078 | -8.70155 | -52.36542 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b18483-ff5e-39c5-9b12-3599ad2fc78c | -6.25654 | -55.42842 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0a6a9ce-b6ff-3df0-a367-11147a955337 | -10.18524 | -50.27156 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5d1bbb2-bfdd-340f-9a2f-1bc03f20e5f5 | -6.64134 | -59.44982 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6fe53a85-4bea-3c8f-a5ed-4f1be5f9b62d | -10.3394 | -49.96005 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01562b0a-6e34-3430-9cb5-30fa51999e01 | -6.68829 | -59.94423 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a8f5f866-7b34-3f86-b31d-9cb85c3442c2 | -3.11722 | -61.18666 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7dc97c8-88cb-3a41-b486-7c243294210e | -5.84151 | -52.06816 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a3dd8f1-fe32-3141-a532-dda68440e917 | -6.68369 | -59.94337 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45a8cbd4-3f4b-348d-a8b5-39987128ef05 | -5.2005 | -60.05203 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11efcf61-bcc7-3e88-9ae0-a0c388d5fe21 | -5.79979 | -43.6495 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09fcf47f-e401-3c5a-8b73-f04ccb4ebc93 | -11.3194 | -50.52942 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7d8251aa-3567-32a9-a1e3-ccd2584b56bc | -6.64447 | -59.4315 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1b80152-495f-399c-b109-2acfffb8b33f | -11.30969 | -50.5191 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 30cb4f77-c6cc-390b-a50e-812cda3ec2b4 | -5.4693 | -60.05952 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8f760c1-1222-3d0f-a4bc-8c136ff38871 | -12.0886 | -47.06832 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece2f895-e5cd-308f-b513-c6f77de75d61 | -9.0418 | -65.74931 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 198afe59-514e-36af-899e-4da651d08b44 | -6.6293 | -55.22737 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d588eeec-f8fa-3534-8a24-e19d9ba6601e | -4.96644 | -55.85376 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| abca977e-7d3a-3492-9af2-8a6067e2578c | -10.87604 | -45.31008 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43338db8-7396-388c-ae8a-ee6c52531234 | -8.45623 | -54.68275 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84167509-68cf-309a-bee1-e1167712b474 | -7.25167 | -59.52252 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b491b339-f6aa-378b-8fef-01a5ad1c8ce4 | -6.87852 | -56.5056 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01248c13-b490-3ba0-b9f5-55d18c6b558f | -7.61384 | -49.93429 | 2026-09-03 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b13a529-537a-3ecb-8503-441e46d127f2 | -5.46844 | -60.06461 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3bb99ea-e365-326a-84cb-3bb336df3d7c | -3.12547 | -61.23605 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
