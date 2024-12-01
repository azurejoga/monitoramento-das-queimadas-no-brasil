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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38788f01-8708-30e9-88d5-420928783c85 | -2.7493 | -46.1054 | 2024-12-01 00:38:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b878dbe5-ad0c-3193-ae47-b46a2719ca92 | -3.2172 | -45.765301 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2c8397b-05fd-3b36-89c3-3f2f8eecc1e4 | -3.8507 | -46.5401 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85b5e97d-7cc0-3cf9-b829-f42183d842a0 | -3.7635 | -50.1674 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d76a158-b4cd-37d1-a568-935b77b5c84a | -1.4797 | -52.667999 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97dcde9-4c00-32d1-8755-5f6bcb8ef029 | -1.3224 | -51.662102 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1b5da4-ca2b-3550-a11f-a660021fa547 | -2.6007 | -45.4198 | 2024-12-01 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3ef7dbc-8079-31ee-ad18-ddf9d112cc7e | -4.0507 | -46.8251 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdc23c9-b4e8-3a96-aa98-b21c80a85336 | -3.8473 | -46.5257 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0a8f2e3-1bb4-3f93-8bea-2297299aba3e | -3.8901 | -47.068298 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76ed2eea-83ee-3d93-bfb0-80ecf92b11a9 | -4.0099 | -49.9366 | 2024-12-01 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60f58962-4786-3d8d-82ac-25773ede0503 | -1.0981 | -53.384899 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00e501dd-cef6-3a2c-a614-e40c5919d017 | -1.9398 | -53.3344 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2346579-17cf-3fbb-8a84-693898cb9573 | -2.6086 | -45.409401 | 2024-12-01 00:38:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c86086a3-a903-3a73-a759-3b4974a5ee7a | -1.2402 | -51.7985 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 433fa612-78e0-303c-980d-fc9ccd0f45ea | -4.0342 | -46.932499 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13d5d890-c24f-38b7-a3cf-266ee9ceb4b7 | -1.2463 | -51.780201 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a8eb8c-6db7-3b08-a3d1-ce5e06b94151 | -4.2052 | -48.124699 | 2024-12-01 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0b623a-9b26-357a-a29e-349d1d32ee92 | -3.1326 | -45.978699 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7019b1ea-c61e-327d-a38a-9ce278045d43 | -1.5944 | -52.539001 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5669c46-aad1-33a2-9569-e847dcc50113 | -1.3174 | -51.730499 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e95c2d97-7944-3465-9d36-39482f93022a | -5.487 | -46.342499 | 2024-12-01 00:38:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb61c20-0871-3174-82e2-b8a14854ba79 | -1.1426 | -53.669998 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0af47625-25c1-3fb1-9cd7-c7156591deb0 | -4.0805 | -50.020401 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a5fd8a-b5b1-33b3-bce7-16351259364b | -2.8477 | -54.080799 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5416156-e89a-39be-b924-f574431b34a6 | -1.2781 | -51.739201 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5b01ca-2c63-3747-91cc-6b7e7204c82b | -3.8457 | -46.518398 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bac83d3-93bc-3838-a749-242cc1ffbc7b | -4.55 | -43.572399 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7bebda9-79f5-3de9-aec1-e4a50a0a9776 | -4.5551 | -43.288898 | 2024-12-01 00:38:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96f47c4b-c126-3e63-8d88-17f69f618569 | -4.4301 | -48.296398 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8e29d91-afd3-3334-88c8-cc28c9ca855d | -3.7861 | -48.096802 | 2024-12-01 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b9c97a-3ddb-3ca9-8f6d-fda950c5355c | -2.3303 | -54.605301 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769f0ec2-4463-35ca-aab1-8aeb54b76752 | -2.7447 | -51.759701 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2a2c6d-b81e-3212-a7d6-cf2fd7bcbda0 | -3.8575 | -47.060902 | 2024-12-01 00:38:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 582f54a4-1237-3dd1-9253-b353178ae1d6 | -2.1222 | -45.9804 | 2024-12-01 00:38:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f81fadae-01da-3720-89fc-f3139570cdf9 | -2.7409 | -51.742901 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a70e0c-6a4f-3d2d-a4a4-bdbe2567a86c | -1.5924 | -52.530102 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3647c4ef-9cc4-31d0-af4d-0e396e187447 | -1.2322 | -51.808701 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf2e203-7acf-3afc-a099-ee8324331343 | -3.6906 | -43.425098 | 2024-12-01 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05179b01-1a29-302a-9564-a7894e157209 | -1.1819 | -51.769001 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5208b442-416c-3837-8bb4-e7e25125ecaf | -4.0197 | -49.934399 | 2024-12-01 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9434602-d3aa-333e-b49a-63508c82b06c | -1.9496 | -53.332199 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc015af3-3abe-30a5-8b4d-975f94931526 | -4.4757 | -50.766602 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d639f0c-b0ab-30b4-a599-67e066a644e0 | -1.2941 | -51.7188 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d6691d-0def-3c8a-a955-89e8ca1fb58c | -2.8503 | -54.0923 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2501b69-b425-3ffd-9a2c-333ce51e5a02 | 1.1552 | -56.0009 | 2024-12-01 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd413785-bf08-353f-aa6b-a92c0d449667 | 3.2872 | -60.048199 | 2024-12-01 00:38:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 86180ac3-ada3-3202-a810-9a0817691b53 | -4.1908 | -50.690102 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9d4c2f-35f1-3e2b-8d63-3849d063a279 | -4.4988 | -49.639099 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a95ae46-4012-3804-bc9e-f31b1566f4ff | -4.8147 | -47.319199 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 910353a5-ed2e-3e38-a06a-b68539385c42 | -4.3497 | -45.932701 | 2024-12-01 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9210255c-a399-3dec-a7b1-f8063300f162 | -4.3669 | -50.923302 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8e6f50d-bbfa-379d-b86d-cef47dca03e3 | -3.0205 | -49.528999 | 2024-12-01 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 105a680a-5c8e-3639-80fd-77fe116f479b | -3.2428 | -53.922401 | 2024-12-01 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c397222-e4d3-3932-8bce-ea9cbe0ab6d5 | -3.1246 | -45.988499 | 2024-12-01 00:38:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a38a078f-7565-37a7-b538-d02288e90c15 | -3.0034 | -45.422298 | 2024-12-01 00:38:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5bdc52d-570b-3648-8c70-5418191e4e25 | -5.8005 | -47.075001 | 2024-12-01 00:38:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a58b50f-f9ed-30f9-8328-0e4fe01511c2 | -1.326 | -51.678001 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074ff73f-6d96-37ea-82c4-ecac9c3dc445 | -2.1827 | -53.771099 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533dce97-57de-3fef-83ee-7338dba45b76 | -4.3213 | -48.091499 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe2b965c-eab5-3bc2-a495-cc9521fda074 | -4.1873 | -50.674599 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4563ce-0bab-3f79-8009-7b17ec6b005b | -5.5863 | -45.216 | 2024-12-01 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cae2da4d-5cc1-33f5-87c2-e7c8dda52a99 | -2.34 | -54.603199 | 2024-12-01 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7d92f7c-b5ac-3ac1-b03d-194bfd1f0240 | -4.444 | -45.362499 | 2024-12-01 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9525104-c096-3ef5-89d1-4461bb0fbac5 | -1.3211 | -51.7467 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec73d5c-7bfd-3121-943c-74c65790e2c6 | -4.4055 | -49.773102 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79f5f2e-c732-37e2-aa6b-dfed7417b051 | -1.6667 | -52.494999 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7eb86f4-4388-3c93-a67e-ba20e2a19f82 | -4.0706 | -50.022499 | 2024-12-01 00:38:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c5e6be-9c4b-37f8-a43e-b50f1b66d17b | 0.9588 | -50.210701 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f8d43d6d-4f4b-30fe-b7c5-a01c8dc54fc9 | -1.6293 | -52.466099 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfb2885-6919-3f9a-9d59-a8e310c7341a | 2.6661 | -50.8629 | 2024-12-01 00:38:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0c209928-b216-388b-8804-512ee447912e | -3.6207 | -49.856201 | 2024-12-01 00:38:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d88ad5ea-f6aa-32c7-8e7f-19cbcac117a7 | -1.5287 | -52.6572 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c048cf-6411-39dc-ae17-0b19925bc634 | -1.2712 | -54.549 | 2024-12-01 00:38:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8dc5f72-0620-3c04-b059-23feb22a92e7 | -3.8524 | -46.547298 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cba21a2-b9cb-33c3-828e-6170c1a83d92 | -1.296 | -51.726799 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05818bdb-6632-313c-b8f2-3e47eb9e81a1 | -1.3076 | -51.7327 | 2024-12-01 00:38:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13e1be9-c23d-303b-8294-89a3174c1bcd | -1.6313 | -52.474899 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48f6fa7a-d7ae-3b18-8e2b-8d79a52cce64 | -4.8517 | -47.570702 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2349f8-9d80-31e0-9652-0b32732c4dee | -1.0724 | -53.227402 | 2024-12-01 00:38:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c073579d-0b02-3bd0-9cdc-0cede330aecf | -4.2652 | -50.837601 | 2024-12-01 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eabe684-3d70-3e13-8170-dae68336f381 | -4.5012 | -42.065899 | 2024-12-01 00:38:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 78bb546f-51b7-329d-b8af-354a47f20a13 | -3.6305 | -49.854 | 2024-12-01 00:38:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bac485c-1c44-387e-a858-7b6190a5a3c5 | -4.4157 | -48.594101 | 2024-12-01 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7347fdd-5015-379d-8d10-3a6c259ca833 | -3.1063 | -50.312801 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dedda2e1-b5e5-395d-aff0-9d9f219cf0c1 | -2.8687 | -53.9921 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573e342b-08f4-3f43-91dc-0f81e3b3b949 | -3.2988 | -50.797699 | 2024-12-01 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3ed4b36-f749-3bfe-9cb2-38a24f95fe55 | -4.8974 | -47.1409 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 240a6035-6f8f-3c26-a7fa-f80e2f7a1060 | -1.6508 | -53.419201 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99762a1b-99fd-3926-b74b-1e9055622a9e | -3.6671 | -52.291901 | 2024-12-01 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8536d32-de9e-318b-a73c-49be063b5fde | 0.3572 | -50.8988 | 2024-12-01 00:38:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5947ddcb-1eb1-3854-9368-524704cfb52c | -4.2125 | -47.7071 | 2024-12-01 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7947c9d5-3173-3ae8-a641-29cdd284a267 | -4.0425 | -46.834301 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 192ae223-ce66-3056-8824-2380dce44dc4 | -4.0605 | -46.822899 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f037285-f15f-3d22-8e06-f822e5ba63c5 | -4.5303 | -45.733002 | 2024-12-01 00:38:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd6b9c67-70a4-3c37-86bf-a1e91ee76d3e | -4.0703 | -46.820599 | 2024-12-01 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74c5762a-105a-3df6-a64f-3d822b733985 | -2.8811 | -54.0014 | 2024-12-01 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2ae9f6a-4f63-3b5a-bcb8-1688dc8a0f9b | -1.7018 | -52.468601 | 2024-12-01 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc01f7ef-55df-33ae-8ccd-8b035e6e35ef | -1.0398 | -51.733101 | 2024-12-01 00:38:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e3734c9d-3368-310c-8f14-4ff622cca6bd | -4.8533 | -47.577499 | 2024-12-01 00:38:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
