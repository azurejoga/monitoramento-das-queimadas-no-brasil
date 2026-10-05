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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82c255ab-8429-3114-9240-0cbaa78500b7 | -3.48454 | -59.7266 | 2026-10-05 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd24c450-e67a-362b-b5d0-08312fa252f9 | -2.92787 | -53.94978 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3be47a83-a30d-33ae-acc9-6c6b91b8a4b4 | -3.06399 | -54.17372 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1589f062-ba58-3a11-8891-a840c821fca4 | -6.18274 | -52.9366 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bb17469f-772c-37cb-b648-5e087c8afaff | -7.17875 | -42.00674 | 2026-10-05 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9093b477-2ac0-31b0-becb-41dc6ce0de69 | -6.89426 | -43.68247 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85f17fa3-47f1-3863-8561-96d4868f9cbf | -2.81238 | -54.10046 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a9ce2ef-aed7-3ca4-b49e-7b19124dc9b0 | -5.96186 | -55.3508 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e9f6b3-4e02-35ad-bbd3-44692c94a163 | -6.26171 | -52.86717 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57fc6995-8295-3f4b-9cba-94d1cd512a4a | -6.18329 | -52.93314 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dffb9287-3193-30f9-919b-4c20dfeb6d4d | -7.50507 | -54.99294 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 120f6d79-8c58-358f-be34-9c617e7232ad | -5.81351 | -53.50412 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e528bc-bece-3ebb-900f-149f1e294b5c | -3.00864 | -53.88308 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea0b28f5-1b45-37fa-89d8-5cf673d17ed0 | -3.84488 | -55.84597 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e044238-4873-31a1-9519-b06ea6a8248a | -2.05738 | -56.87923 | 2026-10-05 04:57:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46d947dd-016a-3e49-98d6-fab8dc087d0b | -3.42453 | -54.54914 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5572abff-620d-3b8d-ad69-9896ba62fa32 | -2.9938 | -54.23609 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4dc3620-3e30-395d-a8a7-fac8597b364a | -2.9313 | -53.95032 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58114722-b2b7-3b68-85ad-94bf61acc640 | -2.82417 | -54.13707 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef90d38-6c59-3612-b78a-a6dd2515f906 | -3.08123 | -54.17646 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e41a53f4-77e8-3918-a927-5eba8b3e38b3 | -2.97846 | -54.09529 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f53ce93e-8fb2-39e4-9b5d-3ae5a85caea2 | -6.20244 | -52.79105 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a209da6-c5b3-3c69-bcfe-e6abf9deaf36 | -3.2761 | -50.40372 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c854bc3b-664e-310e-9ab2-0e781e749865 | -2.88557 | -54.14599 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 183b1573-a27b-3b49-97d6-902f85c06b68 | -2.79678 | -54.10954 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a720b95-7905-3a82-a31b-291f77857ab3 | -3.46569 | -54.59105 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8966182e-01ef-3410-badc-438c33dbeb36 | -4.11236 | -49.08135 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c4730d4-f393-3dd5-9df9-bfa03c61b2e8 | -5.68634 | -53.49433 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6df9ec6d-9a2b-385d-bc68-d652e8b853b9 | -3.37545 | -54.11122 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597e92f5-9e24-33be-9d5b-d6ad2be888c5 | -8.67265 | -54.55908 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1e2223e1-83ab-31f1-bd59-ec7725a7e90e | -8.66652 | -54.55439 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9ffe605-07e3-334e-9dbc-adcfb790e0b8 | -2.97668 | -54.10653 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 199e4dba-34db-32ac-bb9a-396d7a467cca | -3.12737 | -50.34368 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d662088-7649-3acf-a2b2-f203bd20610a | -2.87379 | -54.11407 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a84a22f-645c-324b-8300-f77d41b1cc15 | -3.47081 | -50.09764 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fc0da07-58ea-39ac-a65d-83108ce52fd8 | -2.7836 | -54.10362 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f28abc76-0a00-36b7-ab70-b180f3c71d0f | -7.88815 | -44.19363 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9ca9343-b6ea-3be2-a9e6-d9b8cfb2d911 | -2.80185 | -54.12191 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a666b679-87f6-393d-957a-0d1d821b7cb7 | -2.97621 | -54.08726 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79e012d1-32b7-395a-865c-83c37d2b034b | -3.40574 | -51.80753 | 2026-10-05 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12ef187e-40b1-3e1d-b206-caead2784b90 | -3.63442 | -54.5068 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 267e97e8-6c48-35b1-983a-c874a896e42b | -6.24737 | -52.85074 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d95cc7fe-51d2-3269-b70c-6439243d8d5c | -3.15583 | -50.43335 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eab0950-2b6b-3746-a623-7855efe0e2c5 | -4.25906 | -50.79103 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e49141b0-8bdc-30d5-9c38-5fb28b0f76e7 | -3.22746 | -54.31142 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ed1657b-2588-3c6c-98b8-fc1d265e5ff8 | -2.79394 | -54.10524 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b57b8bf8-d15b-3fd2-bdf7-e5bafaac66b1 | -2.95304 | -54.12205 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db876e4-6d4c-3daf-a1b1-a846685d1e3d | -6.90546 | -43.68067 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76ad7718-5451-375e-97cd-03871d30c0e5 | -3.7913 | -50.86977 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8514f3da-56ab-3730-8918-2d4b83f3d57e | -3.90898 | -49.6995 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4d7c4b9-c419-33c4-bf73-af8c4fe60813 | -3.11316 | -53.71174 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b21242a-651c-3ab0-b2a6-22395c0111be | -3.93897 | -47.98038 | 2026-10-05 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05eb57a9-e2c0-3d34-8960-d1d723e8e090 | -2.80814 | -54.12678 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612bd658-2ab1-39ea-92e3-37d16500c455 | -3.12615 | -53.71754 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| edf2ebd3-4aa9-337b-ab64-eb015e2a9332 | -3.06442 | -54.38398 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f358a1-bcc6-30ae-a08f-992fc8b1116f | -7.89426 | -44.18818 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 954b1223-d37e-36cb-8369-5ca1d6a69386 | -7.23276 | -55.20042 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bb7025a-5fc2-3afb-ac3f-24fef638ce83 | -2.90079 | -54.11751 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b4514c0-6446-3afa-a785-4e422689c46a | -5.95769 | -55.35412 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14a8a4b1-c2e5-307a-b41e-69681f6816fe | -2.95633 | -54.14571 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d048c9e6-c55e-3db1-a5c6-d473f220500d | -5.99647 | -53.63747 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 384aa843-773d-395c-aba9-a2f77938242d | -2.94673 | -54.20598 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89c603e0-3ca5-3f73-8bf9-364fbea6790e | -2.95349 | -54.14139 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 71d70b90-fa6e-3103-b61e-e6414484ea6c | -2.7563 | -51.55332 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43698f2-4b57-39a2-b56b-e670c79c0765 | -6.41811 | -51.96053 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcb73dff-ea53-3fba-8f24-14845ff5b390 | -3.12454 | -50.33952 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c7165de-a9d4-3ad7-9e45-62bd017920aa | -3.06804 | -54.17051 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d5149a50-04d1-39ec-b151-48ed41e33ad3 | -3.08063 | -54.18021 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 66dbabcd-7178-33e7-94a3-b4903994cf07 | -7.88246 | -44.19603 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658d2e6f-c921-3a06-8523-2e6d2a4b943b | -3.10182 | -53.71741 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| cf14dc7e-8bc3-330c-8ac6-d4223d8e0504 | -3.28289 | -50.40476 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a53351ff-5619-3f0c-9e1b-60c5aed600af | -3.05095 | -54.39006 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 449356bf-f049-30b4-a2fc-5d4c346fda6f | -3.29673 | -49.12606 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51c66bf6-17db-3d17-878c-94ae2cb9d469 | -4.81169 | -54.73198 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d370424-f849-3ded-a9e4-5d931dd0fc1c | -2.90563 | -54.08754 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6f257b5-e9ea-3aaa-bec2-5a6ae2bf7bc1 | -5.99437 | -53.52211 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0119c1d2-ab5c-30a6-8b31-34fa16ab0c03 | -5.58714 | -49.7506 | 2026-10-05 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 424d52a0-f0dc-3358-8c69-fcb49de29ade | -1.40569 | -54.62447 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c31d843-ba3c-3021-8087-1fcc85d4d1c4 | -5.58776 | -49.74657 | 2026-10-05 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3503c2f1-43d7-3061-ad86-ec9ced1b7ec8 | -2.96934 | -54.08615 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16ac3431-f4a7-364c-a77d-24f3d1a8019f | -2.9692 | -54.10921 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73f4f1c8-ca83-33d3-a25d-626339ed58b1 | -3.12 | -50.34627 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c479386d-8a05-3ebf-970d-15f708f7a679 | -6.19828 | -53.43623 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45692eff-a199-37ea-9cdf-7689feab0fc7 | -3.18157 | -54.09625 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbedc933-19b1-3485-80ec-ce018eadef50 | -3.5166 | -54.63092 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 586177b1-6481-34eb-954b-6e6a39188de0 | -4.46154 | -54.97064 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62dc81db-afeb-3141-8a40-64f9c75187ae | -3.50798 | -54.61762 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9becbd9-3e39-370b-bc9b-77fc75e8729e | -2.85356 | -51.3028 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59f198d5-f0c4-3548-8d68-abb7010bdbac | -3.56973 | -50.29442 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22150b94-5582-3c32-9d88-62a4af1b8e8e | -3.12397 | -50.34315 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f974ec9-cd4b-3be9-b0b7-02f1b63a64a9 | -3.45871 | -54.58992 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8f1056df-5905-312f-bd43-23221f3dd611 | -3.10522 | -53.71795 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57827e52-c288-3e57-97dc-5a9a9cf41837 | -5.84574 | -53.4734 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47caa9e1-ab37-3865-a8a0-8ecbd6024864 | -4.11064 | -49.06824 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ca6b7ae-3f6c-3025-9fa8-cc0d47f7a105 | -1.76358 | -55.02954 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68909289-a457-30a7-be13-2408914635cd | -4.11426 | -49.06879 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24be6e2e-befc-30d3-a320-a9753cba0984 | -2.81745 | -54.11283 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b5345b-c89a-3d78-b510-12471265db40 | -2.48728 | -56.10961 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc87ca4d-3703-3ad6-b2fa-c270f8b8e6af | -7.8934 | -44.19449 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97d12f3f-81a8-3e5f-a583-38531028a3b1 | -2.68833 | -49.03898 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
