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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 235107b2-8e52-3de1-b953-61abcf323021 | -20.22861 | -41.02353 | 2026-07-26 03:49:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2fdd43b0-b53c-36ff-9b80-66c30e8aba33 | -14.66166 | -46.9612 | 2026-07-26 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edab992c-310a-3fb8-ac9c-1af1893d8a38 | -16.78525 | -41.46011 | 2026-07-26 03:49:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8352084c-78d0-3eee-b126-28ab96d2b4d0 | -12.67107 | -48.21776 | 2026-07-26 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bde08a79-0506-3660-b92e-953f5d51fdc4 | -19.08619 | -40.55024 | 2026-07-26 03:49:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ff88f33f-458f-3423-80d7-8a1bf63cc432 | -18.69456 | -44.55048 | 2026-07-26 03:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0adcb23b-6f5b-30d6-9406-5d8c6a289da9 | -14.80374 | -48.33107 | 2026-07-26 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8370fdbd-02c1-3c29-9724-f728830936a2 | -12.65897 | -48.21539 | 2026-07-26 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70f8d6ad-b314-3157-a234-a89bc8e0b79a | -13.40754 | -48.16242 | 2026-07-26 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da05f9b2-5e0a-3a6d-a028-c21a6842bfb5 | -7.01088 | -45.43257 | 2026-07-26 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e3adacd-f558-3290-86cc-3976a1c0bebc | -16.24794 | -46.29675 | 2026-07-26 03:49:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea27023-8e7b-33bd-ac15-352446bcfc8f | -13.74762 | -42.57184 | 2026-07-26 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 588b0941-b1bb-388f-9529-ae43d6b72fcb | -13.55009 | -42.50756 | 2026-07-26 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c54b918b-1ee5-31eb-80ee-bcd9cd657b80 | -13.19559 | -48.32464 | 2026-07-26 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb7ec660-5c58-3772-87a5-93239a86f0eb | -16.78444 | -41.46475 | 2026-07-26 03:49:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad33ccc7-8ea5-3dc3-8766-477c01f93be0 | -7.85205 | -39.89723 | 2026-07-26 03:49:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a3ccaa10-3975-33d2-b285-678c566b6271 | -9.23953 | -40.50744 | 2026-07-26 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 46fe5d10-033f-34d0-95be-032227207335 | -12.0292 | -47.80697 | 2026-07-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30116fcb-7bf5-31ff-bde6-adce875205b0 | -12.02841 | -47.81097 | 2026-07-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7b8f96e-b9a4-311b-82dd-53288ad978d9 | -16.24739 | -46.29426 | 2026-07-26 03:49:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57b207c1-e6e1-3126-bd68-5282130f23e1 | -12.0312 | -47.80917 | 2026-07-26 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d2311b8-7e6a-30de-bcc9-1fea63cf78b6 | -20.28847 | -46.43308 | 2026-07-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f93db587-e034-3315-a8cd-42bd8be6adf3 | -20.69022 | -47.52291 | 2026-07-26 03:51:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c068bf5-d779-3a04-b3ca-845fb005af4d | -20.28403 | -46.43084 | 2026-07-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81cb4830-0c51-30d8-b374-57d3337b4f61 | -3.96425 | -43.11165 | 2026-07-26 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0901c820-0fb2-3720-b142-a0ad3f6aa99c | -3.05178 | -48.74479 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f4d3899-1774-32e3-961c-69ed2a2c1738 | -2.76935 | -48.57516 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111ea107-4ea9-3ab9-819e-b2cbb9d3a385 | -4.9473 | -48.24828 | 2026-07-26 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94963c07-7387-302c-a972-e9628008fe1c | -5.93586 | -43.65321 | 2026-07-26 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2eaf4ecc-2488-35db-87be-2f696591d4d8 | -6.95417 | -39.89213 | 2026-07-26 04:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20376a5b-5bef-3757-a276-239e9baa90c7 | -5.48813 | -45.11858 | 2026-07-26 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0c4c067-a23c-341b-b737-a33bdfa06b21 | -3.48425 | -47.68425 | 2026-07-26 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7e66e2-397d-313c-a7a6-6fb354131f01 | -3.72936 | -48.87597 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6c979ca4-029f-38db-b9e5-171f6dbd1fba | -3.72655 | -48.87184 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9887eaef-af1d-3260-8ffe-18d0c37a434a | -3.06366 | -51.33643 | 2026-07-26 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76b7ee1f-9c1b-32bb-8057-c2502d46968b | -5.48463 | -45.11806 | 2026-07-26 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 142e51f9-3e54-34d7-a268-680afc485c43 | -3.72598 | -48.87545 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a975ba36-a62d-3f87-aac5-3bdb43eef198 | -2.9829 | -54.09384 | 2026-07-26 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4243aa30-4508-3ae2-b1a2-402d01fe157a | -3.15941 | -48.58806 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a2a155-cca9-3731-9f2f-4aad376e13f3 | -4.35105 | -48.9656 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1de28df3-5f62-3513-9e78-63a219870f86 | -4.94175 | -48.2403 | 2026-07-26 04:32:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f5d4ad-3ada-3f96-8d3d-f57bd134508d | -4.91349 | -43.47127 | 2026-07-26 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7168ac9c-74a8-366e-9320-12efc1ab7d07 | -4.3471 | -48.96868 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c62e23-509a-3e2f-a03c-3236e1827248 | -3.24055 | -47.91521 | 2026-07-26 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5950bcfd-67eb-38c8-99e8-13a919673b1a | -4.61514 | -49.05497 | 2026-07-26 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c73f91cb-e9c3-3693-9258-3fe691c825aa | -3.66915 | -48.99326 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4852f12-eaee-3015-8962-7e0797c5122d | -4.3886 | -47.75609 | 2026-07-26 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0ca6be2-2e32-34c6-9d81-8dd14bd5de25 | -4.41518 | -54.86497 | 2026-07-26 04:32:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59592cbc-849c-3cfd-8db5-ad29b3c62b14 | -2.76128 | -49.47193 | 2026-07-26 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd3a6b58-80b0-3e8b-95ef-dd9f22527f9c | -3.7226 | -48.87492 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22ca57e2-8272-3bac-9cc5-77c64989e091 | -3.83983 | -49.06502 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0b36e58-03f1-3d89-ab22-a7c5e76884c7 | -5.68027 | -49.81849 | 2026-07-26 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0ee77cb-6d89-3a4a-a4e2-3912d6673545 | -3.24611 | -47.92318 | 2026-07-26 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22779198-976d-302c-8fb8-12c526c8dab1 | -6.8586 | -39.20872 | 2026-07-26 04:32:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3de332b0-e8ad-3c91-9624-d4812b9923b1 | -4.37258 | -47.76775 | 2026-07-26 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 844b8019-42ae-38e3-b570-7f4d47d7273c | -3.79879 | -51.18426 | 2026-07-26 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7165e695-0374-3402-8a12-b3e57d844180 | -5.93897 | -43.65839 | 2026-07-26 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74324b1f-75fc-3ea7-9917-170924f23d96 | -2.82672 | -52.30246 | 2026-07-26 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa296a5-9ec7-3c18-ac1f-e4d9305fff30 | -3.24333 | -47.9192 | 2026-07-26 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 067a5064-6935-3bc9-8a2d-181eda0cd927 | -3.84735 | -48.95045 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4992f76b-edce-3ddd-a72c-cfef0a9f47ca | -3.34879 | -49.21948 | 2026-07-26 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12be1d2d-5e90-3037-bd84-e2b44e84dbf5 | -4.61852 | -49.0555 | 2026-07-26 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75987bd0-6c9b-32b0-8bc5-66d50400db99 | -5.39131 | -50.40759 | 2026-07-26 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f9b63ee-d434-3007-9eee-95f1e136bf88 | -4.86419 | -47.40797 | 2026-07-26 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e809829-cba0-3d1f-a6f1-9d29340d45f5 | -3.96042 | -43.11106 | 2026-07-26 04:32:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93393e0e-68dc-3b70-9816-238da8f30369 | -5.67968 | -49.82224 | 2026-07-26 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35665da7-4b44-3106-8be6-4de127d1440f | -2.91432 | -39.95885 | 2026-07-26 04:32:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 721dd829-f1d3-32d7-b0b8-3a30f47e851d | -5.4603 | -47.47004 | 2026-07-26 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a274cc2-3ad6-383c-87a5-b2114f5edcce | -6.85341 | -39.20792 | 2026-07-26 04:32:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c65b7337-3d11-3b55-8171-4540f1de9158 | -3.34938 | -49.21576 | 2026-07-26 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8a8fbdc-ede0-38d7-99d4-f98b4dc28c13 | -5.93517 | -43.65784 | 2026-07-26 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62e5401c-f419-3773-a81d-d6080109abe3 | -3.83643 | -49.06449 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46abd5e4-f332-3300-a662-48855363f9da | -5.67683 | -49.81796 | 2026-07-26 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c26d973b-460d-3809-b3c2-7d9c06b2a697 | -3.26397 | -49.5317 | 2026-07-26 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84dd1cc4-18bb-3d8b-ab79-4015b078acb8 | -2.80644 | -48.66954 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa81cbb6-7793-3909-9666-ea5fa2a167ae | -2.967 | -48.99014 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 126b02e1-59cc-3aa2-9123-0f6420f20175 | -3.24279 | -47.92267 | 2026-07-26 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5595156-c5cb-33ed-9238-821b076a453e | -3.84679 | -48.95407 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6084875-2be5-36f4-8592-0af6dd1f3f58 | -1.52986 | -52.62297 | 2026-07-26 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a0ca2d0-99be-3711-adf7-5295b8851e5f | -3.16131 | -48.5889 | 2026-07-26 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8590eb4a-ee76-3090-9014-e82044bbe2d6 | -3.72541 | -48.87906 | 2026-07-26 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01b561b2-d6fa-3415-aa27-7489f27f5a21 | -12.0299 | -47.80754 | 2026-07-26 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b451ab9-2643-3833-a36a-6d9b08903073 | -9.53283 | -47.11651 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce53664c-d4a6-3a54-b021-35c4c255e0be | -9.36996 | -48.54954 | 2026-07-26 04:34:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a174394a-5f14-34f2-b9a8-9a3ba514dd0e | -9.5362 | -47.11702 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f82f13d2-eea4-345d-996a-1f54da2d1097 | -12.32096 | -47.17173 | 2026-07-26 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6827f48-eacf-36d1-b2b1-095d2cac9779 | -10.39587 | -48.27337 | 2026-07-26 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| df1e5a6b-5e98-32a4-97a0-602dcfa5135a | -9.53228 | -47.12015 | 2026-07-26 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc48e24a-22b8-3608-8aed-6af609ff5155 | -13.77256 | -47.13323 | 2026-07-26 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d184396-de1d-3b53-ac5c-078ceec72331 | -13.78031 | -43.18229 | 2026-07-26 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cfec01e6-9486-3ac8-bb39-8b4f1ee41943 | -12.32495 | -47.16845 | 2026-07-26 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c43898a5-8d29-3759-8389-8ec310ed1955 | -8.6762 | -47.36592 | 2026-07-26 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31c2fb91-1e47-3e27-bb35-bd51bb36dc79 | -12.00669 | -49.26431 | 2026-07-26 04:34:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fa77cd3-77f1-3d4b-9c0a-966eecbef08c | -13.75111 | -42.57224 | 2026-07-26 04:34:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c4c7c00-4d48-3fd3-a11b-a2f056aa6154 | -11.02949 | -54.31892 | 2026-07-26 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4029bd7-9cd3-3614-b703-a06b481cf358 | -13.55385 | -42.50702 | 2026-07-26 04:34:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ef5f1f4-894d-3e15-97dc-54688961a48f | -11.53778 | -50.18249 | 2026-07-26 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cfadf8f-9cbd-3b07-81e2-824c4c4b1b94 | -10.96907 | -49.4156 | 2026-07-26 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f7a3521-5c8e-3b05-9afd-a8c35b749d1d | -13.82151 | -44.4693 | 2026-07-26 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eb1d6bd-19dd-3ff3-855f-fea59740005c | -9.24208 | -40.5112 | 2026-07-26 04:34:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |


[Clique aqui para ver as próximas entradas](README4.md)
