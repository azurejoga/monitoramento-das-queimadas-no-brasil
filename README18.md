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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75281a76-f3ae-36ac-9a6b-2c0ae5099a73 | -12.18624 | -52.89293 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08c6d785-376f-3918-bf9b-7e8d581f7b57 | -12.29008 | -57.55352 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d1a588-a44a-3b7f-b76b-4ecbe65b7494 | -12.19022 | -52.90051 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 719974d7-3294-3c32-a7c7-5252beaa26d9 | -11.52379 | -54.79412 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6c973f33-78a8-3f91-9cf1-71d1ed7c9604 | -12.19385 | -52.86581 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77f0f827-6226-371f-b77d-c0befbb59401 | -10.77952 | -54.10557 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7aa506d-8992-38b5-ad07-9cbea05ee23c | -11.9411 | -58.61415 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4bd7199-86ef-3e22-8ef8-bbf71558032e | -12.1799 | -57.1483 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6646bf7-0044-3f32-ad95-4186155250ad | -10.93929 | -56.84882 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7d0729e-504d-3ccf-a66e-061dfa5cc398 | -9.59753 | -56.92771 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bacc256-4077-3f80-8cf9-912e9bdcfce2 | -9.09375 | -59.40014 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1640c5ce-39d5-3ff9-82a7-fed392b5679c | -12.2273 | -56.55236 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60ef4dd5-3814-3af3-8304-48684beddc1e | -10.90195 | -56.85818 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c2f32a8-5f01-3fd0-92d5-59ae68013e2b | -12.09545 | -52.01223 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50165c15-098e-32ec-ba47-ca50cec1e5ae | -14.8401 | -48.14336 | 2026-06-28 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5350930d-75e7-313c-88e8-ce6ad70d0812 | -12.2334 | -56.55704 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 763639a8-6334-390e-a26d-fa9c7ab61459 | -12.18908 | -52.90839 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69ab8e49-d2c9-3b44-aecc-0ebf3c23c4d3 | -12.20874 | -52.87103 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 03a434c0-43c8-3abc-9784-6d0cd066a481 | -11.32266 | -54.46641 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd58c84-ff26-32fb-b74a-7a02cbb1b53d | -12.18158 | -52.90028 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 31e6af92-2438-3b43-922a-9a3c1d9514df | -12.1977 | -52.87338 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 08547539-94e5-328a-b19f-df2ee45279e0 | -12.1839 | -52.90868 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47243877-ef9b-356e-9e79-11edea9eea75 | -11.21586 | -54.29788 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 535bcd73-3754-34cb-9eff-220c6c7331b6 | -12.18559 | -52.90786 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 914f3c3f-8c40-39c1-8dc2-a1e18c8e1cd5 | -10.84932 | -49.12749 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4db2927-1aa1-3035-889c-8908daeb32fe | -12.20176 | -52.86996 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 889c0d3f-06d2-375a-952b-f42070914a7c | -12.0858 | -52.00205 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 315fd509-0a3f-3727-8bc8-d64e2db17e87 | -12.08943 | -52.00259 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169dc701-a779-35b5-97f7-cccaca98af6e | -11.91043 | -57.12264 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba56d5d-a8b5-332e-9016-d5e1635aac6b | -10.39261 | -56.76755 | 2026-06-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3179664b-8027-36bf-b2ed-db822a82a4f6 | -12.17869 | -52.89579 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d715e89e-4af0-3d8a-b91d-46530baadc58 | -11.52655 | -54.79815 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e114a2a5-3c34-3b9d-bbe9-4e62ad1b81be | -12.19265 | -57.16159 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7876a7f-4ac5-36c7-8408-7ceb6977e05f | -10.29645 | -57.12534 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dbcf7f26-fe6c-3b07-a3db-009a9a6c6e65 | -12.16195 | -57.13007 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 553b2ca6-3d1c-3ec2-9d30-bd531b357a13 | -11.52325 | -54.79763 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a52c7556-2a78-3431-87c2-ac97c89f80d5 | -12.08455 | -52.01064 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a530e1c1-74a0-3f06-8aad-07810ad6b5ca | -11.9074 | -57.14125 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8876ac01-2ef1-333b-9e34-83f9ab19b6a6 | -12.23007 | -56.55649 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f74c82e9-cefb-380b-86b2-3203eebb64bb | -12.60149 | -57.88669 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24d30476-5dde-3f6b-8e80-4b0e58873cd3 | -12.18918 | -52.87318 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d59745a-acec-3d9d-b2d3-f9dd0667d9ed | -12.17212 | -57.13174 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c940d487-6629-33d9-8b3c-4bdf5bf574f0 | -12.19484 | -52.89316 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09428f7a-f2df-3cb0-b649-b419b2b962ce | -9.08463 | -59.40593 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bde65437-9bd8-3fea-bd07-5b8e278aae6f | -12.4449 | -58.48412 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0a684cc-52c4-3b2c-8da9-727b09710bf7 | -12.60086 | -57.89061 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a8f518f-f4bb-337b-b129-2d2cdacbedcf | -11.93468 | -58.63056 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 137e4ea7-4b4d-3447-bde0-0aef65daf061 | -13.65582 | -60.62363 | 2026-06-28 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b532c42-af66-3244-bb3f-963354b9dd8f | -12.18901 | -52.88417 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d19f2183-1bbf-3107-93b4-62ad5a9a0794 | -11.90764 | -57.11835 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4641b7e6-d456-3bc5-9d70-bead8108995b | -11.21561 | -53.82887 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0dbd8c3b-f35c-3fdf-bc1d-e758cd14883a | -9.59471 | -56.92334 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21e12674-b034-38c0-ae2f-441805d14a40 | -12.18864 | -57.16476 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39dadf11-50a8-3290-817b-9dda3fd02d53 | -12.08642 | -51.99774 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ca040d2-fd88-3595-b173-f95e0fb2ea0c | -11.21368 | -54.31206 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4fc773e5-f5b9-3024-a2a9-624d1c266310 | -9.59532 | -56.91953 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5e27360-9d55-3e9b-b74d-d6d91c51606d | -12.19776 | -52.89764 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 860d1da5-3596-3700-808f-1ef539b94385 | -11.32543 | -54.47046 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 607aa41b-d839-3d18-b125-b9727f83b62c | -12.79515 | -54.88497 | 2026-06-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 11874f22-8212-3685-a2be-3bb9625e38be | -9.09201 | -59.38654 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d2fddf9-7ae5-3440-a1c1-7ec7d508dbcc | -9.09125 | -59.41526 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 42a973d5-08e4-3abd-8672-70d28b7d3571 | -12.46489 | -58.49611 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2f70b622-5c1b-3623-8970-52de4c909b7a | -12.17531 | -57.15519 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2f0dadd-40c2-3bf3-bb9e-a877a5e4caf0 | -12.61137 | -57.88346 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9deccb2a-de4c-3324-8a0c-3c8187cb9138 | -11.90583 | -57.12949 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aee5c41b-9ff3-3f37-b43e-0c058dadc291 | -12.60779 | -57.89177 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b08997cd-1c56-30ac-b6ed-899be10c28da | -13.88711 | -47.17508 | 2026-06-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592425a2-d5dd-3412-9a52-c88cfe76023e | -12.27691 | -50.1004 | 2026-06-28 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47444e6a-7a82-3e01-9bea-68b1ea20185a | -11.34813 | -55.26804 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93a31c66-925d-33c6-b3f6-e6eb0c2dad84 | -10.3043 | -57.14226 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4045c12b-c167-3b34-b398-87ac72392052 | -10.93191 | -56.8514 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e17ba41-6019-3b7e-8bc5-066343c592c1 | -12.43111 | -58.41384 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be16fc18-fef5-3b2b-8c2d-f26c04e05694 | -17.31179 | -42.65409 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9cef322-d7cc-3b68-aae6-2e0f6945758f | -12.60277 | -57.87886 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bcc88bf0-a4ae-3571-a181-3cd79a50864f | -9.49052 | -57.32569 | 2026-06-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3a8a2fc-4e9b-3919-b1d7-2858b8f779a2 | -12.19149 | -52.88163 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4377c4be-2cd7-3e92-892c-7a11080c1ab7 | -11.3201 | -53.94818 | 2026-06-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a4c8a63-b222-3d8e-b1cc-90988b5afd83 | -12.19713 | -52.87734 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad1b8e13-07b5-3f05-9ae6-9fc2735de358 | -12.19072 | -52.8723 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ebc8dc97-b599-3a22-9cce-88ef2f8d287b | -12.46202 | -58.49132 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 29cedd8b-e7a3-3e30-b3ad-3f72c8f28f8c | -10.54057 | -53.71344 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8154fe-bcea-37b1-a5d9-d6d93708336f | -11.91706 | -57.40556 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212fe461-87a4-3c50-b772-aa916bcb95d9 | -12.62458 | -57.8897 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dff68313-25c0-3f0c-878e-99121dad304b | -12.18616 | -52.90392 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 303480e7-5381-3360-9647-83c43192c19d | -12.19655 | -52.88131 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70a493dd-7542-3e22-9b7b-b9c75dc40e8f | -11.31988 | -54.46236 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a5d06fd-b821-3791-ba1e-be9dbae45ec2 | -10.05466 | -59.10925 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4075e9fb-0284-33b8-8e43-50adb9aa897b | -10.30553 | -57.13465 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 334bbcdb-6886-3446-9d68-c450be961596 | -10.53722 | -53.71292 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5944df2b-8e4f-3347-981b-62a79f086ce4 | -12.18269 | -57.15258 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1078f560-7943-3979-9238-5193440b10fd | -12.18586 | -57.16047 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8dca601-305d-3816-beab-c844d068c37d | -12.22788 | -56.54876 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58bc4734-33da-3443-8d02-06ae25cd61c6 | -12.19313 | -52.90499 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b13c666f-2087-3353-a07b-9df9a0fb4733 | -11.86384 | -57.80947 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5b518c1-4994-36bd-954f-a989ebcd0d5a | -12.17751 | -52.90368 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2891abb6-47ab-30b8-a195-aa224d5a637f | -11.92325 | -58.65474 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1f9c86b-5fab-34bc-8f7b-65de8e337bad | -12.19719 | -52.90158 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9007aaa6-33c6-3fd2-9beb-d941f0f32cb9 | -12.45636 | -58.50328 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b9243ab-40ff-3cbd-9257-df98ba4f80a7 | -14.63 | -54.45974 | 2026-06-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35d5a795-284c-3024-846a-28e3a863a19a | -9.5941 | -56.92714 | 2026-06-28 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
