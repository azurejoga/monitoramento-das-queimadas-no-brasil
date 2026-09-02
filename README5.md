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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dbfe500-6018-348c-85e0-f21a801eaecb | -8.12642 | -54.94051 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 70287643-c227-31db-a795-45d72732e54a | -7.54104 | -60.72078 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 04f4639e-bd01-3b32-9a39-15117a087c74 | -8.75438 | -62.58391 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.6 |
| f39ea50a-0589-342d-8606-f14b604d6c2d | -13.99213 | -58.67845 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d05bbdf7-f09f-3b03-9f2a-8397ac299acd | -14.00449 | -58.6856 | 2026-09-02 01:05:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a0cd5c92-34ff-3569-a715-0e00d99f81b6 | -8.46558 | -54.70286 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 1e9d19b5-d4d1-3aef-88a0-a2d90cca9776 | -6.85345 | -59.48647 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| baf3fdbe-874a-30f5-ac4a-c9c39d827f6c | -7.44822 | -61.4127 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 78f4eac5-e0e0-32ce-bb08-2f846847676a | -7.57271 | -60.46617 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5e76dc3b-a005-31b1-900b-dc4395ef6828 | -9.03723 | -65.40411 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 8c3ce63b-445b-38e3-9503-cae6e5434122 | -8.92724 | -62.36774 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d2c13bdc-3ea5-3ca1-9cfe-b9c57922b4e9 | -10.94497 | -61.65053 | 2026-09-02 01:05:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e16fc0d7-f6a6-324f-b3af-0d144b9efbff | -9.01193 | -65.41679 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c4df2422-5c29-3e70-982a-27998204e877 | -7.68472 | -67.12842 | 2026-09-02 01:05:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 75945d61-a6c7-38fe-a0d6-46917a3a1252 | -8.55493 | -63.19401 | 2026-09-02 01:05:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9e26a1ec-dc12-3f40-a8ef-3c0df99ba550 | -14.49955 | -59.84791 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f864aa64-4cd2-3ce7-abfa-342cff1eba85 | -9.82891 | -63.00761 | 2026-09-02 01:05:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 212f1f83-c970-3a77-81fb-e0de48b36e77 | -2.121 | -56.80784 | 2026-09-02 01:07:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| fed34e84-1259-3d09-8a9a-07fdc7a76471 | -3.11521 | -61.23114 | 2026-09-02 01:07:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e6e3be6d-e0c0-30e4-a69d-7a83651c2723 | -3.65843 | -58.91087 | 2026-09-02 01:07:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 539823f3-87c2-3dfa-92de-59ea1493a367 | -3.61516 | -60.55933 | 2026-09-02 01:07:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 8a538d29-258d-357d-8b84-a59de3286808 | -5.54594 | -60.22588 | 2026-09-02 01:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b8937ce8-d473-3180-84a7-54f9fff9c3c7 | -7.50009 | -70.05045 | 2026-09-02 01:07:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 272e34e4-f2ba-31a7-8da8-a7a6315519c6 | -5.57859 | -60.20439 | 2026-09-02 01:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c10e31a0-4c0f-390e-b69f-03a84a603d87 | -4.23902 | -62.23317 | 2026-09-02 01:07:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 46cf6dd4-46ad-3a48-b0cf-db1ca5ad0d9e | -5.33927 | -60.1525 | 2026-09-02 01:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4895baad-abeb-3b62-aa74-b4f0f25f51f7 | -5.57428 | -60.19842 | 2026-09-02 01:07:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 33d452a1-acb2-3d6a-87be-f357a45a8099 | -3.12643 | -61.22947 | 2026-09-02 01:07:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0e445d7c-16c4-3b3e-8495-b08e834dbd1c | -3.61757 | -60.57566 | 2026-09-02 01:07:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 62ad91a2-ff1c-3f6a-bd59-2bef0d802d04 | -10.4945 | -64.314499 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbb9e2f-fd35-39c9-b03b-b7b600c830eb | -9.0082 | -65.403999 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a112ae82-892d-36bd-aaa5-b2e4aa400c20 | -17.0746 | -56.847698 | 2026-09-02 01:10:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8d4b08e3-14db-3256-95bf-5e7d55257e26 | -6.9495 | -56.4487 | 2026-09-02 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9e5537e0-70a5-3ae4-8dc9-df01036e9ea5 | -6.6765 | -58.7492 | 2026-09-02 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 28ee0ce1-3ca6-3a16-9082-34d02fdade88 | -7.2006 | -60.6706 | 2026-09-02 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2382560c-3740-3d3a-b9ed-af4e35b7a343 | -8.1298 | -54.9471 | 2026-09-02 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 7031e42f-bf95-3ff3-a866-93b144dd88c7 | -16.1534 | -46.6286 | 2026-09-02 01:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6a0b7d81-7ed0-34a8-85fe-99a7dc9671c2 | -9.8806 | -64.9764 | 2026-09-02 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1f88f4cd-976d-3b7a-b582-f93c456b7110 | -10.9013 | -45.3279 | 2026-09-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f9791c42-35eb-3197-9590-a185c64cb090 | -12.1512 | -47.0833 | 2026-09-02 01:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 0436950f-56e7-31e0-80b6-612ec8b87d91 | -16.7339 | -47.0688 | 2026-09-02 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 194.7 |
| a32b2aa9-4f87-346b-ad54-64041d8328e4 | -12.1704 | -47.0806 | 2026-09-02 01:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fbf7bd7d-e575-38c2-a0b7-471f328c0b53 | -16.7334 | -47.0918 | 2026-09-02 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 128.8 |
| c2a93978-4a39-32f8-ae6b-f6a59626b7ae | -6.6948 | -58.7678 | 2026-09-02 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 17ffd90b-b574-3655-a230-118dc37a6741 | -16.7538 | -47.0649 | 2026-09-02 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 06d6765e-2e3f-32ee-8d69-009f0745884d | -16.1528 | -46.6517 | 2026-09-02 01:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bb35f70c-3046-3d0c-bb5d-9c32c3715bed | -6.6764 | -58.7686 | 2026-09-02 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4447a46c-e2f7-3a89-91dc-6a05c10e016e | -12.1324 | -47.0635 | 2026-09-02 01:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 15cfa0b0-9080-3df7-a4a6-106f4ca1480b | -10.442 | -46.7235 | 2026-09-02 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5be9be2c-bf53-3552-a1ef-3f9c6313f06a | -10.9009 | -45.3509 | 2026-09-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1d88a57c-6447-3e22-b9dd-8fcfa7c3c7f1 | -8.7613 | -62.5869 | 2026-09-02 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| aa3fbc6d-76d8-38c5-a3be-22ad34075251 | -7.2005 | -60.6897 | 2026-09-02 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 22c625cf-e977-3077-b9a4-fee744cdac3a | -11.6624 | -50.1954 | 2026-09-02 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a57b01b1-0c68-39ee-980e-cac64853caab | -12.1516 | -47.0608 | 2026-09-02 01:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 887ca954-8f11-3526-be62-e6b3ebe42d40 | -17.0878 | -56.8534 | 2026-09-02 01:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 2a58676a-92d9-374e-99e0-0d6dd9f2d184 | -8.1112 | -54.9483 | 2026-09-02 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 15936a6a-6c1f-3c29-8690-618014cd502e | -7.2191 | -60.6699 | 2026-09-02 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| dc12da0d-cb5c-3307-8749-5230a944b78f | -12.1508 | -47.1058 | 2026-09-02 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3a10f77e-6d66-3450-9028-6e9dabf01947 | -8.1296 | -54.9672 | 2026-09-02 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0319e2e6-bb91-3e2b-870c-8506870cd2bd | -16.7141 | -47.0726 | 2026-09-02 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3d2602fb-06a2-3443-abd7-ce7224533320 | -12.1312 | -47.1309 | 2026-09-02 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d03d5896-79a3-3837-a801-ca9125f1a6b3 | -12.1504 | -47.1283 | 2026-09-02 01:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1bc18150-ceca-3bab-8826-1c1d8ed2c130 | -8.111 | -54.9684 | 2026-09-02 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c539ded5-9d3a-3c3d-b475-7d2d3309eebd | -6.6949 | -58.7485 | 2026-09-02 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 99b92393-6cfe-3b37-b271-3e41886bfa38 | -7.4714 | -63.744499 | 2026-09-02 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 236ce16f-d484-3183-a2b4-3c1dbd2b9db9 | -8.7515 | -62.580601 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 615a0c43-61fe-38dc-8e58-ceb708d98ea8 | -17.077499 | -56.859299 | 2026-09-02 01:10:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54b3f219-9a95-33ec-a144-17453097a56c | -8.8947 | -62.351101 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcf6951-86d6-3643-9c76-fe5272350320 | -9.8811 | -64.980103 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aab3030c-cc9a-3017-bf37-f9bbcc9ecbaa | -14.4903 | -59.835999 | 2026-09-02 01:10:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d103b679-73f3-3d1c-ae06-d5a163f6225b | -8.9045 | -62.3489 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7271ebf8-d733-3933-8855-1d66627cb23c | -9.8682 | -64.9683 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 89414fea-2274-3233-b39c-139605928ec3 | -9.4447 | -67.447304 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d54ef45a-706b-3d2d-89aa-b716d8fef9b8 | -7.7608 | -61.199402 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e4ab575-03eb-3fdc-bb66-ee033766175c | -7.5323 | -60.709099 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b5e206a-06b0-3ad5-b769-8114aa3f23f9 | -9.8279 | -63.003799 | 2026-09-02 01:10:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6a207c-ee54-3eb6-a2bf-17db35881a7d | -9.0076 | -67.797798 | 2026-09-02 01:10:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5402b647-4a8e-3cc3-841c-50ca0e6a4975 | -9.8419 | -64.988899 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a789718-2865-3a93-9ec8-eaf5f304bd84 | -9.1355 | -60.947399 | 2026-09-02 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3756f1-279f-3686-8fa7-bd9a5efefb2c | -10.4652 | -64.459999 | 2026-09-02 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6aedee-8c35-32ff-8b73-7a4698a190d5 | -3.2836 | -60.642601 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c953d83-825b-30ee-8196-0bd47605bcec | -7.688 | -67.109001 | 2026-09-02 01:10:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b55207f9-a315-33c8-918d-a0922ece7d18 | -3.1127 | -61.2369 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5a11e8-4697-3221-af0a-03886d07d306 | -9.085 | -65.379501 | 2026-09-02 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b496ad8b-2cdb-3500-929b-b90bc91498c5 | -10.9412 | -61.6549 | 2026-09-02 01:10:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24fbde70-866b-35b4-ba2d-3d24395f9d79 | -8.2641 | -62.7477 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be26cd4d-5e35-32c4-b651-0429d714667d | -10.9394 | -61.647202 | 2026-09-02 01:10:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb54856-0575-347e-ba6f-7e4149f5c378 | -9.9239 | -60.483101 | 2026-09-02 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8a0159a-c7a6-3693-847d-1e237a06fd72 | -9.8296 | -63.011002 | 2026-09-02 01:10:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1761c01c-6bfa-380c-a228-3132e32ee4d7 | -9.4491 | -64.5653 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2089b1f-f05f-3fd4-b0c1-6396b8a78b6e | -7.7251 | -60.959 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26b0a311-9773-3d72-ae64-6429853a5994 | -9.8263 | -62.9967 | 2026-09-02 01:10:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b50f93ee-f6e0-36a6-8e27-994555a20c23 | -8.2372 | -62.900398 | 2026-09-02 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a080d69-dfd4-3ea5-9473-d452afd28a2b | -6.8145 | -58.857399 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8de4f5d0-ab9f-30f5-93f9-6187a897f516 | -8.4242 | -54.7076 | 2026-09-02 01:10:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8798d847-ec17-3ad9-a069-660a07bc1306 | -5.5535 | -60.226398 | 2026-09-02 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38d3bb38-9710-3e44-bceb-697b2b7545af | -6.6399 | -59.420502 | 2026-09-02 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbeec5d2-e805-331a-9979-567d756750b7 | -8.8964 | -62.358601 | 2026-09-02 01:10:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b85d44c-9819-3c1f-9948-e38bc3f886d1 | -11.0398 | -61.5909 | 2026-09-02 01:10:00 | METOP-B | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adf0cd88-1b80-325e-baa9-bdb45d8c4628 | -3.1203 | -61.224899 | 2026-09-02 01:10:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
