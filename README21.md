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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcc103b5-cbdc-391a-8962-7da2d72b9f45 | -8.34619 | -46.81403 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a416d30-fe68-391f-b24a-7f7907596f3e | -7.10158 | -46.50725 | 2026-07-01 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 564a9713-f788-34db-8218-f994082bbe79 | -9.88761 | -50.39577 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c30042af-56df-3325-a66c-ef008e4eb2a1 | -7.00218 | -42.76717 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e1356a27-9778-3b59-b505-08b4a332feb2 | -6.9034 | -48.04257 | 2026-07-01 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 78addce6-e877-3a31-a71d-c5b51894854b | -6.15717 | -44.64937 | 2026-07-01 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e7baf82-f675-309c-9240-a78ba7e305ab | -8.49225 | -47.20729 | 2026-07-01 04:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa5e3315-9e3c-3b89-a75e-715bd9f19b46 | -10.92699 | -43.05655 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8a33f1eb-de5d-30d2-ae6a-fa858a0da243 | -8.12488 | -47.88372 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a172adac-35db-3079-a572-f46e40803f7b | -10.383 | -49.58644 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3d299707-e235-3f6e-8a84-f307ef4224fc | -8.7254 | -47.83793 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ef3d3d2-ea04-31a8-bf9f-f95bc8004cbd | -10.92799 | -43.05769 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 929933e8-9f86-3cc2-8000-c595c9bea71c | -5.81078 | -43.8027 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dac8b230-718c-384a-90a3-26539b8833c0 | -7.73915 | -45.9191 | 2026-07-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 587d8ef6-3b93-3290-8d0c-9f3ce86f6098 | -9.97571 | -48.23928 | 2026-07-01 04:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ac782e0-fa60-3fe0-9305-19bf8ecd39b1 | -9.11352 | -58.25808 | 2026-07-01 04:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31c42882-0b28-3c98-9261-7a3c2728030b | -9.58227 | -57.01741 | 2026-07-01 04:55:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03c5e590-849b-3c9c-8e9b-bf6836a05c6f | -5.35048 | -45.19159 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 918f0283-44b3-347d-8770-947bb407a7ce | -10.92213 | -43.04729 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| bbb103bc-1234-3434-9624-d905c0885f90 | -7.09718 | -46.50659 | 2026-07-01 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 516dc9fb-b8d2-3787-adcd-74b5f1a40ec9 | -9.17232 | -58.05914 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 404b9439-0865-3779-a5c7-43b3edb4853f | -10.92428 | -43.03999 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 07204a33-0ae4-3cf1-9729-fb2bb442f803 | -9.6013 | -56.92643 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41600732-dcc0-3e8d-b704-a3594384cd4d | -5.80663 | -43.79939 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b58c52e3-f202-3458-b050-12917fd67d33 | -7.47218 | -44.74611 | 2026-07-01 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1c1c224-fbd7-308e-a0fe-bc99195d38d3 | -9.60862 | -56.9277 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5658cfae-1435-33b4-a716-b0a2ca94ad82 | -9.33259 | -58.01643 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a029704b-dbbd-310e-b5ab-5cf175494138 | -7.47595 | -44.75548 | 2026-07-01 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95daaab1-bcbc-3fda-986b-2eec7eeb36ea | -10.92162 | -43.05155 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 82219e95-4927-3025-bdbe-527ec76cda59 | -10.92751 | -43.05228 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0c545578-2ffe-37c3-ab5b-af16309c7d10 | -10.12468 | -52.0859 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1fae3ce6-a503-3757-9085-71de412a9172 | -5.80211 | -45.04779 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 078ffcbd-166e-35d4-acff-7fc7e18c43d0 | -8.05929 | -46.7163 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a68566a-ffee-3e41-b1e0-e03b4b3c5dfd | -9.59765 | -56.92579 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b3fa5c0-1367-35b1-abb9-f392e2085083 | -10.92854 | -43.05342 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| ab7b7906-6e82-35a1-8b0a-b0aee2ea8104 | -9.68514 | -56.09717 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62a081ff-b926-318a-bf9b-76646f22e342 | -10.37855 | -49.59052 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12bb83ff-21dd-3564-b589-76ba0a2e8e1b | -7.0057 | -42.78331 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2bd44e3-e5bc-3c21-a31e-378026c494bc | -9.97518 | -48.24297 | 2026-07-01 04:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3502c1d5-a2bc-3a6e-b4fd-d0a9a87639ba | -9.60423 | -56.93142 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e2b5df2a-eb2e-31cf-a17d-7c37ef2dacb7 | -10.12075 | -52.08901 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e416dc1b-f2f2-3616-8952-b4cf42f3d48b | -11.49617 | -47.41985 | 2026-07-01 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3dea484a-52a1-36ff-8445-cb0829fc5554 | -9.16406 | -56.93964 | 2026-07-01 04:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c65dbf64-ba83-3f40-8f6a-9f29a01fd6df | -9.02897 | -59.53555 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ead8d41-4ca5-3937-aa67-dc3562ab8b36 | -9.68999 | -56.08979 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c249eb-d89f-3e16-9439-1b8221db80bc | -9.20435 | -45.33112 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b22cc1c7-3997-3024-b01b-414582a7df4a | -8.64029 | -47.53033 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 192fe931-57d0-3ffd-9f7a-7dbde35735ba | -8.12094 | -47.88305 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e88132e4-96b6-35a8-bfd9-8055292833e3 | -9.19942 | -45.33045 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b972131d-aa6e-3caf-8e5b-268ec5027aef | -9.0903 | -59.49068 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 313b8a37-4e8f-37b0-a2d1-c7f85b3527a0 | -8.12556 | -47.88002 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2dbbba2-1de0-358b-a959-f19db85c406d | -9.59399 | -56.92515 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 031f2666-a15b-3ce1-b1e7-f0da512a577a | -8.52133 | -54.76926 | 2026-07-01 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df7c00d4-b5be-3b7e-b6b4-facfd2e72bdb | -8.1259 | -47.87646 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| adefdd5a-f559-39cf-81f7-1812d6fe2feb | -9.60276 | -56.91773 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c71ead0-8ea9-35d2-a4b3-3f58e7db6c78 | -5.55151 | -43.96247 | 2026-07-01 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c874df6-9c39-336e-8317-dd3855cbd2a6 | -4.34816 | -47.76223 | 2026-07-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ca4286f-d91a-3bb4-beec-da08efa527eb | -9.1169 | -58.26222 | 2026-07-01 04:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cfe6219-a995-3e3b-b96c-ced25824afdc | -5.55063 | -43.96847 | 2026-07-01 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bada8cd-6e02-311a-b1cc-f8f82c22cded | -8.50461 | -50.14945 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccc56eb5-1740-365c-bd5a-821cc0257125 | -6.84092 | -47.94344 | 2026-07-01 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f40615b3-8132-31f7-aa8c-1f5875fbaba0 | -8.12609 | -47.87641 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f8cdc0c-d80b-3a6d-b610-07e997174b80 | -5.79578 | -45.05769 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f415ea81-06db-3be4-a7e6-3ecd91374fd5 | -10.93072 | -43.03642 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4951b4e-7a7e-33e3-ac1a-367ffe424233 | -9.20019 | -45.32482 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c78251f-c7d1-3433-9a06-09c6952abf61 | -7.00832 | -50.076 | 2026-07-01 04:55:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f2e403-67a6-3652-bfed-d09a8408f876 | -8.59188 | -50.9797 | 2026-07-01 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f273472-3eb4-3307-8e17-988643ce7d64 | -9.20513 | -45.32548 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d647da7-23c7-3520-82bf-29004e43a558 | -8.50231 | -50.4277 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f2b3167-6859-309c-9ee9-3b46cb1a580d | -7.70227 | -55.38433 | 2026-07-01 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 633747df-1bca-3615-be70-98a06fe81575 | -9.59838 | -56.92143 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 867354f0-07fc-3c97-80dc-4e2a593d085f | -8.69256 | -50.70095 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f17ef0-8810-328d-adee-590919017ea1 | -7.47554 | -44.75835 | 2026-07-01 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fb04683-16f9-32eb-836f-b48648c38237 | -11.54557 | -47.44973 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dc0dc9f5-9cdf-3e3b-a74c-b52b3749960d | -9.01882 | -59.54242 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3b7b91d-389a-3b86-aedf-2618512ee2ce | -11.50063 | -47.42022 | 2026-07-01 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca224476-57c9-3ae6-ac98-ca282a64a1ac | -11.91295 | -43.39303 | 2026-07-01 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42900b10-9256-3653-ac7a-681a2a4a4cf5 | -7.00624 | -42.77947 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba4ee040-e380-3540-b754-ffeb8549a591 | -5.86286 | -46.2524 | 2026-07-01 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96dd915d-2c9b-325d-be0e-ca2e60dd1eec | -10.91622 | -43.05626 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2f3419b0-2448-30fc-8290-76d3dc8ad31f | -3.91697 | -47.81927 | 2026-07-01 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fceb385-0832-3a28-8a9c-37441d1b2944 | -7.0175 | -45.43397 | 2026-07-01 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b09937d3-71a4-3e9b-892b-5d10f4ac1779 | -5.80707 | -43.79624 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68f352c0-bb2d-3eab-ad10-37a334e1d1d8 | -9.68798 | -56.10176 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdb0f16e-4aff-3068-8e46-4e831ae2d4d0 | -7.0978 | -46.50231 | 2026-07-01 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f7e9d4dc-2b0d-349a-b3b6-e3057b50dbc1 | -7.29029 | -46.24928 | 2026-07-01 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 546333cb-ece3-3c67-a1e9-07018ad631ea | -5.78848 | -45.04076 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8193f31d-b30f-3532-9f6e-0cac46af8a06 | -9.68932 | -56.09378 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae822f3a-75ae-3bcc-b6a5-4cef5315e715 | -10.44109 | -49.5856 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abddddcd-48b2-3ac6-8e0e-54267afb6f91 | -9.93584 | -54.91755 | 2026-07-01 04:55:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc83ce6c-9226-3b7a-93c1-3f9f972b4262 | -10.92802 | -43.04802 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 479491a2-cf9c-3746-8130-212d643df7a0 | -10.91624 | -43.04656 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| d6f531b4-533d-3e62-86c4-19eb9ff6d4e7 | -3.91832 | -47.82167 | 2026-07-01 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c1f8360-6e1e-35c7-b493-4e05d700981f | -10.59736 | -53.45819 | 2026-07-01 04:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69d27126-8b9c-31cd-aa07-740353cc0b16 | -11.50008 | -47.42421 | 2026-07-01 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 193e6d38-a8ec-3008-8351-1aeed1497863 | -11.91879 | -43.39369 | 2026-07-01 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48951624-3154-3a19-8caf-7c8ed5f08919 | -6.16291 | -44.6445 | 2026-07-01 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 740766b6-45bd-3c6c-82d7-01fbaf8a5293 | -4.18312 | -47.84208 | 2026-07-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f06891d1-7d82-32ac-88ef-7b70ae243d10 | -7.01823 | -45.42888 | 2026-07-01 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ed0d13d-62d9-3933-80f9-83740731ea72 | -5.81124 | -43.79957 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README22.md)
