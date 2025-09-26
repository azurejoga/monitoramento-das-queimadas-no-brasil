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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92cafd11-bf5a-3088-bbbc-6ac960e749d8 | -17.19188 | -56.37087 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c4096989-4858-3893-a55e-8e41778102bc | -15.9774 | -59.48954 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae153fe5-fea6-359e-895d-ebd446eb7d6b | -18.30317 | -57.10367 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d0e2a637-71cf-36d5-8743-822dd86d2973 | -15.99771 | -59.49287 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f765b692-0a87-39f4-a045-7ca335273af3 | -18.54348 | -46.96334 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9849349-bbd3-353d-bbac-f29a3c245a74 | -17.93456 | -55.85023 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 33125e51-df9b-38c3-95a3-3cb37c22f84d | -15.94047 | -59.50243 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67017542-7fb7-3e85-bba3-b98342111d1a | -17.17521 | -56.36468 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cfe0a048-6875-345d-8910-b43b743b46b8 | -17.18603 | -56.36248 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e1ab489c-42cc-37f3-8f68-bc5ba49f3fe0 | -15.27306 | -59.43854 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 062fe22f-0ec4-39b3-82dd-4195f185e495 | -15.83561 | -59.60467 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea6a6eb0-9d7f-3585-83b7-64b508dcf40c | -15.5204 | -50.43233 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fe5ee83-74a3-34f4-a169-c201e8480b1a | -15.35479 | -59.18015 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118967f5-125d-35a7-9251-b6e3e8bbb8c5 | -15.26382 | -51.47251 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7b23a6fb-42fa-3526-9346-4272574b2c54 | -15.53853 | -44.33373 | 2025-09-26 05:06:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de0726f2-e8b6-3e93-b825-77dd5d2965a0 | -15.83095 | -59.61163 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46c0d08b-3e9b-3912-91a6-b881b894c925 | -15.74511 | -59.51487 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9a2c1b7-a3c0-31e8-a984-d7e60ae6655a | -18.17917 | -53.33741 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdc80f01-6026-37ec-a88f-7fbbecc7a2a1 | -15.88042 | -59.3344 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d41a2b4-8915-30fb-a13d-a05811f7907f | -15.99433 | -59.49229 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c83990f-b103-3054-9bd5-88b435575e69 | -18.29643 | -57.10256 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8fb463a3-4000-3604-b8c8-461237453e07 | -15.26816 | -51.47313 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b98ae55d-d98a-37fe-b49e-ec5ca0070a80 | -17.5944 | -52.49018 | 2025-09-26 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33acacc5-4dc0-3af6-93b4-0af3bb094b22 | -15.27707 | -59.43534 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af4bddb4-0438-3c2b-a433-6d9af474b394 | -15.91957 | -57.50138 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c4b8fcf-6b2d-3df8-8446-113b43e333ed | -15.89053 | -59.33611 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcc2029a-6c9a-353e-b6f3-1f82092be2f7 | -18.18808 | -53.33162 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0a372e4-4f75-3f0a-bd98-32d995c0978a | -15.25914 | -59.45956 | 2025-09-26 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5c1015-2461-31b7-b67c-62fc70507ca5 | -15.2693 | -46.4354 | 2025-09-26 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| add14e54-a108-3ed8-9a19-0df4ab61098d | -15.02704 | -46.93868 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9931ee33-657c-3429-8019-ac53d36c375a | -15.64143 | -58.46624 | 2025-09-26 05:06:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c26b9e-6fd6-39c9-96d7-5306eda04889 | -17.19928 | -56.36813 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fb3901e9-ce73-3df6-99c8-4c89ec03982a | -19.74496 | -48.15415 | 2025-09-26 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf951741-2652-322d-bc93-1060c723c9eb | -14.98377 | -50.05984 | 2025-09-26 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ab3a0b1-8df2-30fc-a165-7b80857bfadd | -17.23567 | -52.40596 | 2025-09-26 05:06:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aad69575-e231-34c5-8b6f-c5aff1a79930 | -17.94273 | -55.86811 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f5b786e4-4655-3d9f-a73c-6c12b929a1a1 | -15.89054 | -59.42022 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 706d542b-510d-30bb-a314-29f05266252e | -18.2998 | -57.10312 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54e486bf-5601-3fab-b6b2-617fbfcf3ad5 | -15.53163 | -44.33306 | 2025-09-26 05:06:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e65032a3-a809-3ed7-ada0-409d3d23ffe5 | -16.22296 | -48.81017 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5faca042-a8ba-39ea-8c14-a60c8e13e93f | -15.51316 | -50.4332 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1835496a-4291-3136-b8c4-6e2debad1376 | -15.99996 | -49.02806 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04f4ee7a-42b4-38b0-9a8c-0232e7d03940 | -15.98353 | -59.49451 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a2e59f2-eb32-36e1-adf1-dd93ff7e8583 | -15.53098 | -44.33957 | 2025-09-26 05:06:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8acfdd5c-f2f2-3ddf-be1e-2aca7c0ac624 | -15.62872 | -53.62523 | 2025-09-26 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2938e1a9-e1d8-38cd-9f53-70b579bea428 | -15.35143 | -59.17959 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a14d368-87db-3e4f-8035-bf4e1faa8279 | -16.2189 | -48.79914 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 940c06b5-e75e-3989-85bb-7ba99c559516 | -15.74573 | -59.5111 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b7eaa1b-f8d4-368a-86f2-e5e9c983e068 | -15.93713 | -59.47506 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d504658a-5c33-3545-87fd-579f5fa596a3 | -14.82374 | -45.40886 | 2025-09-26 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 214c9edd-0503-380d-bb5c-405c76ce8b2a | -15.26987 | -46.43003 | 2025-09-26 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcb36f5f-6b67-3c6f-8a50-d24e5e24a592 | -15.06339 | -44.98555 | 2025-09-26 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c76480-3892-3eb0-ad7c-cafcf9772873 | -15.90741 | -57.49204 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 868a2839-a5ae-3300-8869-45b5bdcd22a8 | -15.91625 | -57.50083 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4f475df-30e1-30cb-acb3-ff2d110199cc | -15.93709 | -59.5018 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40149e7f-553c-32cb-9aed-8488fe0d00fd | -16.22336 | -48.80669 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84b1ffba-314d-3c4c-9e5c-8cea5fab0fc5 | -15.91735 | -57.49371 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13af6fc7-c10a-345d-8879-36b5b6d26f3d | -15.2502 | -59.45024 | 2025-09-26 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7f52ba9-50fa-3e85-84a7-d3ae60429a4b | -18.1787 | -53.34103 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a77b4db2-72d6-3728-b058-3a727ab4c1d3 | -18.31272 | -57.10909 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a6444f9c-8b82-3641-97cd-32c62053df79 | -16.85521 | -50.50594 | 2025-09-26 05:06:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 437a2c4b-2557-3e40-954a-c3a634ebbff4 | -15.07007 | -44.98552 | 2025-09-26 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e361881-f7c7-3a5c-9205-794299cff8ad | -16.00108 | -59.49349 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45566225-695d-3ab6-a85c-8e28341949ae | -17.54382 | -52.01352 | 2025-09-26 05:06:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f054d5ac-f563-34fa-a8c7-2406ca15395f | -15.52101 | -50.42754 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4b0fd2df-d5ad-3030-b2b4-245dae2bea6b | -18.30598 | -57.10798 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 261e33b7-7d9b-380c-9c2f-623f20b6c36e | -17.92698 | -55.85319 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 29324b3a-86ab-326f-9214-88cfa452fd03 | -14.82274 | -45.40772 | 2025-09-26 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d53b15e5-a1e0-3073-bda3-62d90950ba08 | -15.51901 | -50.42407 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc16da72-0d7c-3e19-a440-371016d8a1a4 | -15.89389 | -59.33673 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 831803f3-805b-36a7-b162-a88dddadf7c3 | -18.18363 | -53.33448 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2237c60-e53e-36c4-85fc-89eeae8e01eb | -15.91072 | -59.33976 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74f32c7-2d74-3cfe-b239-3e151baeaaf9 | -15.98947 | -59.47962 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca07c12-4d4c-30e9-ba17-87af340d6264 | -18.30261 | -57.10742 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 28b06313-c89a-3767-aabb-1f31f7bf16ab | -17.19016 | -56.3588 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 985cbc0b-0f9e-35b9-9023-8fbb0da20665 | -17.19002 | -56.35919 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f93f9893-fc87-351c-aefb-bdfe51c7b44e | -17.17863 | -56.36523 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fea4d632-a33d-3d2a-bdca-dbd069e449e3 | -18.3071 | -57.10047 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b4eaab76-94b9-355e-9d15-0a18f966ecf0 | -15.82819 | -59.60725 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb7f8557-e200-3fd9-82f3-20980d5ab516 | -18.30654 | -57.10423 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 82bbb0b0-e979-3059-a13d-1cffd781f02d | -15.0262 | -46.94625 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56a8c160-d606-30a2-8c8e-a73c70d83f15 | -18.29699 | -57.09881 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 548b0463-772f-3d30-9a55-7ef1317fa5f9 | -17.54441 | -52.0089 | 2025-09-26 05:06:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b5df515-8112-3dc2-8dbb-e1f3eeb4db2b | -16.12976 | -50.76334 | 2025-09-26 05:06:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af91f1e2-0d17-3ee0-8a06-68966b802098 | -15.25635 | -46.44183 | 2025-09-26 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d449ef0d-60c4-3c94-b9a7-cc3ca7f0d600 | -15.27487 | -49.47372 | 2025-09-26 05:06:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9ca8e65-051c-3639-835a-807f60923582 | -18.30373 | -57.09992 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f7a319f0-ddbb-3272-9f5d-ea57144814be | -15.97466 | -59.4851 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05cf2da0-e48e-3376-b1a3-fbb98ddb83c6 | -18.30991 | -57.10478 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a8736361-e391-300c-91e6-64b4542787ee | -15.36673 | -59.17078 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e74edc78-4a23-3268-955b-75a206519742 | -18.54241 | -46.96497 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d2f7260-fe84-3523-8d6e-15846f29854e | -15.91293 | -57.50027 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc890599-0a9f-3926-9d37-464f51605f2c | -15.26174 | -46.44883 | 2025-09-26 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b00e04bf-e0f0-310c-9f4f-ebfddd3629d4 | -15.91072 | -57.49259 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5689ca5-8f49-3136-bac5-8328d3f5be2d | -16.21811 | -48.80595 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0a11317-ebef-3839-a25b-130b04cd35ac | -15.93984 | -59.50621 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e7a8e2e-33f6-3104-b6fc-bf1902966817 | -15.744 | -59.47961 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f7ae6ed-7acc-34e0-8d15-9971c51c0846 | -15.37825 | -46.11597 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf86e7df-b630-3680-91b6-d4e7f0cb3a27 | -15.99369 | -59.49619 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d689efb-c565-38e1-86ff-b444c42998d3 | -15.91017 | -57.49614 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README46.md)
