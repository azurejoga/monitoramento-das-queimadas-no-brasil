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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 340d6a89-605c-38cd-ba01-940eddfce92a | -9.078 | -65.43475 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e56189f3-43cf-39a5-a90d-c609c5ac66a9 | -9.13899 | -65.546 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b5acf2-ba9b-3dfb-bdaa-7a78b5538111 | -9.12901 | -65.83952 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d37d9a05-8e59-3e0f-bb0a-15ae6a86c5d5 | -7.80895 | -71.94714 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06807d0a-0d4f-355d-b3bd-201f1fe13ba6 | -7.74932 | -70.26763 | 2025-09-01 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 998aa6fe-1918-3eaf-9633-b608aefe64bb | -12.44582 | -63.92925 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b64a6e-8fbc-302b-8ced-0f9934d4df1b | -9.70781 | -64.53841 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eeed409e-a453-33a4-a2ee-7a4c58fcf31e | -9.12481 | -65.76482 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f836f49e-2148-390f-9d8d-79282d33491f | -9.87095 | -65.03213 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2af2d3fa-6f1c-35db-adec-d2f2cea8d812 | -8.38201 | -70.75509 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53325fb4-6e57-30ce-a778-128e24f6050e | -8.37437 | -70.85407 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af40ee0b-54d9-371c-9a3e-22543205095a | -9.87875 | -65.01308 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dec6dd8c-46bb-3236-a2b5-fd72989e815c | -9.83011 | -65.06312 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3277ebe-2c09-3628-a1b7-4553150b4065 | -12.44474 | -63.928 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2131bd3-923a-3f88-b8f1-a908dee2de3c | -8.65516 | -62.92821 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c8e4359-3487-3909-93c4-2aea3473b31f | -8.70479 | -62.41253 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cafe4bf7-f4ed-307c-864d-b63d0ed63459 | -7.70131 | -61.47937 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef9e4975-656d-3103-9c6c-b8dd139589e0 | -9.82526 | -65.05918 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64add35-91f8-35f7-a4ad-6a7ba87d8a51 | -9.83097 | -65.05661 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf122110-9e4e-3134-bffc-2b7a854f66e9 | -12.42433 | -63.90928 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be7d6e0-e0e5-3f85-9f84-5f104311f23d | -9.06631 | -65.43315 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16897380-dbad-38a4-982a-e5701a4505ea | -7.27973 | -60.6574 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db8d2481-414d-3b57-9e94-0c04e1aa2ac7 | -8.74238 | -62.4132 | 2025-09-01 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111b2d30-028a-3009-a88f-e7640d499886 | -10.26667 | -68.78767 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8785fc26-4f28-3e74-aa5e-b235ab34793a | -9.14063 | -65.83665 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eef31de-1c93-36c9-8415-ce58566019cb | -8.72161 | -62.42168 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e58696-d4ea-3d89-bceb-8c306c13dd63 | -8.22199 | -62.94077 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b9ed430-a415-37c3-b810-661b372019ae | -8.84364 | -64.15253 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192d83f0-c94d-31b6-ae00-91b162e57d4c | -8.74303 | -62.40829 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b075e0c-a0ae-3143-8d79-f0c17bc90c5e | -8.21235 | -73.01092 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 574da4c1-9b44-39f6-8cb1-e4fa262e8b25 | -8.6807 | -62.4047 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fde8464a-77fc-36a4-85d0-0481a4de7fde | -9.48319 | -65.59717 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 309ef18f-0a3d-3a6a-8111-afd451693620 | -8.81875 | -71.06823 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4e9fabf-ffa3-32ae-93d3-bf7aa0c3b88a | -8.68687 | -62.40553 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d930f025-0be0-344f-b896-7748961b02eb | -8.38558 | -70.75563 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0bf9d8d-e721-3cda-83a9-fc824e5c2e9d | -9.34842 | -65.4283 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 836e1fd5-ebda-3dbd-b45d-4a9dc2d53727 | -9.82612 | -65.05266 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60339ade-e5df-37a6-86df-5d0ffcc840f7 | -9.34411 | -65.42162 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f964f05-1f77-3e38-8b58-5cebadd7f572 | -10.08743 | -68.99819 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 172202c8-e59f-3ff0-9961-e7a1d32ecaad | -8.6582 | -62.92649 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa5556fd-e597-3cb2-843b-4c48cb8963db | -8.72881 | -62.42078 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e9d545f-d966-3f84-ab03-76951ea6f156 | -7.92809 | -63.00867 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fa5e139-be26-34cb-bb8d-0f61153e9124 | -8.69444 | -71.03138 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf27e01-14d9-351c-9260-416cb2d3a0ee | -9.9582 | -66.87572 | 2025-09-01 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14ca5cdb-afac-33da-b386-529873cc1555 | -9.83668 | -65.05405 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee884e90-70b3-310c-9685-e4a1a60a5eb2 | -8.76431 | -61.43834 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8eee6dbe-c4ae-3e7d-8a85-c40679fc7633 | -8.44452 | -70.13565 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ad1350-711b-32b4-9bea-18874ebd2902 | -8.36413 | -70.75237 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f4dfffa-ae2d-3fa5-b47e-1cb8b4411056 | -8.96285 | -65.97407 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ded5cf1d-9df6-38fc-a176-d0fb964a3f76 | -8.95117 | -65.95011 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be8c11de-c431-3167-8b99-83ba049a58f9 | -9.07292 | -65.43405 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a3c282-1b5c-3ef3-9251-589caa932076 | -8.73819 | -62.39743 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 270c95c4-e4fe-3efa-bc21-08a955cceb27 | -9.13396 | -65.84023 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 175d8547-2c2b-37f5-ab44-46908112e93e | -8.73622 | -62.41227 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 473f49e6-8471-37d5-b579-cdc3f885b0ce | -8.23289 | -72.81258 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ab78985-2a0f-32ab-957c-12c0635a45ec | -12.43405 | -63.92786 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab03b745-6187-316f-b7d7-bd6f7dca251a | -8.23622 | -73.33651 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc5a3ed9-72f0-3cf3-9ed2-1faa4d3c30a0 | -8.37782 | -70.75864 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6c2c7a-c165-3148-9b9e-f920aa0f8b3e | -7.28418 | -60.65734 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e546ec3-eb5d-3cf2-a450-a599f86c3a78 | -10.26255 | -68.78712 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da214dac-374f-3eee-bbfd-4a773ea845ec | -9.13733 | -65.85214 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1df56cf-0042-3c6f-a610-ad5cbea639db | -8.70418 | -62.41721 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ecea9fa-18da-3830-9e1c-bf63551fc03b | -9.05725 | -65.43499 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83bd262f-c130-3685-bb60-5ccd479bc044 | -9.27216 | -67.64631 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e28fe9c1-d928-3b08-bd86-1243f01f094e | -8.73688 | -62.40728 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d5d010-9e24-37d0-8655-fba3e2b0bb7c | -8.7165 | -62.41897 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18e8d027-2642-3bad-b303-18cc0f54d9f9 | -10.26615 | -68.79144 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b56d2d5d-82aa-3052-bbdc-aeb87f1b2869 | -9.13239 | -65.8514 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 649efe00-9085-38fc-9852-2cfe3c60bafe | -9.0667 | -65.43014 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b644bf63-d50d-39e7-bd3a-e6e5760b5841 | -7.81235 | -71.94766 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8134894a-2794-3bdb-bfcc-101c0ec2d01a | -7.46295 | -70.13278 | 2025-09-01 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85786ab7-fe14-38a8-9056-e1506d18df4b | -9.88024 | -65.00981 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bff1923-1d9c-38b8-8d8a-1917fc4d9825 | -9.11546 | -61.21066 | 2025-09-01 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc2d7f4c-1208-342d-971c-b5719ba83483 | -9.13317 | -65.84584 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39dbb513-dd33-34b2-af9b-c9351adc2a30 | -8.50932 | -67.12746 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c964151c-4e72-3b76-8a70-88e6cd36c4fa | -7.09455 | -63.1395 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02422f7c-dec8-341b-a75f-adf698116b38 | -8.765 | -61.43279 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dec1c46e-1316-35da-99ee-0d9aefedc368 | -7.07444 | -63.07081 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b566bbd-0a06-3409-98bd-760106c4e0d7 | -7.28568 | -60.66444 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa32a24c-ac40-3c62-99f6-35cff993442f | -9.12383 | -65.54398 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c57a5e24-2bbb-3f8b-86bf-a5d9c6cf9db4 | -9.06709 | -65.42713 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fdfae4a-d7ef-3361-bd54-a71acaeeeb7d | -9.87918 | -65.00977 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d929cf31-5a42-3fda-9611-60e0a1623115 | -9.06748 | -65.42413 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdbe519d-beb8-3844-885c-44be7efa44a5 | -9.8314 | -65.05334 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a1bfdbd-6191-31ff-8bd9-b59408be4d1c | -7.10204 | -63.04131 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec851010-06db-3daf-8806-cbd08853185c | -9.06787 | -65.42112 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06db500c-bd5d-34ef-a410-0df2be8471ae | -8.65458 | -62.93258 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cec42248-060c-39cd-990f-5f8212fa7b25 | -8.7351 | -62.41415 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5ee4bb4-c510-32e9-a174-ef42f21ca3bc | -8.17088 | -71.45554 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b26e44e-e0e2-3a52-b06b-8ecc911b081a | -9.83183 | -65.05007 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 651342d9-5f6b-335e-9003-4d154cf3a769 | -9.87935 | -65.01642 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e6c341c-fc98-3051-ba7f-3776c607f288 | -9.07084 | -65.44907 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b66a114-5af1-33bb-9b2f-6c01e45fad35 | -8.09624 | -70.21806 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7cde3d6-a72e-3853-a727-70a8f1b3c9d1 | -8.41856 | -70.73129 | 2025-09-01 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f9d0119-9887-3bdc-9256-b1303f34cb6e | -8.22792 | -62.94157 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ceb1d75-0686-3215-addf-7b67223ad24f | -8.73635 | -62.40423 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2604262-748d-36b7-8ce0-5bbc8cdd19a4 | -8.64639 | -67.24549 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dc22c42c-c683-3ebf-87aa-00291b2bbf27 | -8.72329 | -62.41507 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d306d90a-1832-3d4d-8708-023cdc9a20b2 | -8.6986 | -62.41187 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a88f248c-6b64-3739-9c1f-b8622454c38a | -9.48281 | -65.60014 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README94.md)
