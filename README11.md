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
| 8239de79-dbc0-3e14-ad6e-02f02daaac1b | -7.73048 | -46.16162 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3d85a4fd-672e-327d-aadf-7e12c73bf7e7 | -7.72924 | -46.15274 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9c0bce08-d930-3af5-8f77-b7db35b9dd7c | -7.72164 | -46.16289 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e85dbe0f-b17c-3f2b-bd07-9040e7e53cfd | -7.58586 | -46.04402 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e0a61a8-ec24-3a4b-b459-ffc6be8d66a1 | -7.58463 | -46.03516 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9dfcc684-ec2d-3ab5-a007-4fb3665fb320 | -6.93425 | -45.60993 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33baf021-ab84-3e38-a1fb-4f57b2a6b329 | -6.933 | -45.60099 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 96b667f1-8d24-3b63-a0bf-e4c6a3610edb | -8.81501 | -46.81098 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4cd9b422-1e43-3093-96a0-da2883b5ea93 | -8.78037 | -46.82523 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f22b56b3-9b22-3348-b2ee-14206bb536ee | -8.77038 | -46.82327 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d3e08383-890e-323f-a34d-3a90e9c3b26d | -8.74909 | -47.13822 | 2024-10-01 00:50:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c3503ad0-80d4-3833-9ce5-58926efeed48 | -8.74783 | -47.12886 | 2024-10-01 00:50:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 2029bc09-e03f-3d6a-b724-e1a03a8d3179 | -8.6216 | -46.54475 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01472f64-34f1-351c-aef7-10ea506b8b12 | -8.45374 | -46.45507 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c86f199b-16ce-3b6e-a144-e870e657fdcf | -8.45251 | -46.44613 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 210821f0-4638-3eb9-a643-6819d9361cb7 | -8.44417 | -46.46273 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5699b02d-f48b-3da3-9800-0118fa5705b1 | -8.42679 | -46.33736 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56069fb3-102d-313e-ba1e-c941c8702f08 | -8.39625 | -46.37815 | 2024-10-01 00:50:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f7102624-373e-33d0-8bbd-566aed77c0f3 | -4.77273 | -46.69424 | 2024-10-01 00:50:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3c12afb8-e67f-3356-9d8d-add94c205558 | -4.1621 | -47.20102 | 2024-10-01 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94568cad-6cee-3804-8245-3643feb84a3a | -6.13913 | -46.90556 | 2024-10-01 00:50:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4e7e7416-6ed2-30a7-bb23-e46bb93bd813 | -6.13676 | -47.49269 | 2024-10-01 00:50:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6968f25c-705e-35e3-93e2-a8feece791fa | -6.1355 | -47.48352 | 2024-10-01 00:50:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5021c11c-fe58-3f42-83a7-4e1fe87bde15 | -6.02949 | -47.44827 | 2024-10-01 00:50:00 | TERRA_M-M | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 839d825b-9574-3d08-85f9-4df0f9113f7e | -6.02824 | -47.43913 | 2024-10-01 00:50:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 437e259a-c588-3285-a782-905adb0160aa | -5.3836 | -47.70905 | 2024-10-01 00:50:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e877f49f-e3c4-3245-a5ce-92eab1f19c61 | -5.37586 | -47.71952 | 2024-10-01 00:50:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b362aa97-1dc3-344b-ad56-a064b3593ec0 | -5.37459 | -47.71031 | 2024-10-01 00:50:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8711b221-b245-3c2b-b7ef-477152e04655 | -5.37331 | -47.70111 | 2024-10-01 00:50:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a5003f8-4491-36f6-ae32-2eae2749bc66 | -7.68815 | -47.25586 | 2024-10-01 00:50:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 640f494a-b493-3624-886a-0287a3d0a42a | -7.06425 | -46.86898 | 2024-10-01 00:50:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| e5e59f25-f98f-3fb9-b60e-e1b5e66bad46 | -7.05535 | -46.87024 | 2024-10-01 00:50:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d6f6ab44-a902-343c-8e0c-dfe4da1e2ab0 | -7.05411 | -46.86127 | 2024-10-01 00:50:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33064d3c-8672-38fe-9d78-eff53d8456b6 | -6.97525 | -47.63276 | 2024-10-01 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db0245a7-0ffe-3dfc-9143-da9d6c7011ff | -6.97397 | -47.62332 | 2024-10-01 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 1c0d2380-478e-38d6-8a46-8992ed95acc7 | -6.97269 | -47.61388 | 2024-10-01 00:50:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1c3d005b-4874-32c6-b735-1cb36eeafbb4 | -9.20771 | -48.66805 | 2024-10-01 00:50:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 92b23ec0-1f5e-3750-a13e-0d0efd908500 | -9.20625 | -48.65668 | 2024-10-01 00:50:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 8eecccf4-b01f-331a-97d3-715e5999660b | -9.20541 | -48.66259 | 2024-10-01 00:50:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 2f19edce-fe89-3a40-9ec1-ff2d2fdd5a0f | -9.20393 | -48.65155 | 2024-10-01 00:50:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f22f2f02-1fad-33c2-80a4-99fce4987161 | -8.43648 | -47.13985 | 2024-10-01 00:50:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cb822eab-2784-3bbb-81c2-b747c60487e5 | -8.0178 | -48.32975 | 2024-10-01 00:50:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6198d72a-2e68-3a84-b2a2-295b0cede75a | -8.01642 | -48.31945 | 2024-10-01 00:50:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d4876b78-7327-3831-8067-1bced0434aab | -9.63715 | -48.52936 | 2024-10-01 00:50:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9b4c9b4e-f413-3d03-b0e5-eb4f3ca14a99 | -5.43721 | -48.90355 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bb2dd39a-4780-3f0c-8b7a-5c0a6fe6d9fe | -5.43579 | -48.89322 | 2024-10-01 00:50:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72450256-eb20-3286-8a60-e033829b8791 | -7.27453 | -49.49173 | 2024-10-01 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8a94bed1-2354-3cf6-a529-e229aa1dbf8b | -9.14437 | -48.96788 | 2024-10-01 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 877caf71-1a7f-35d1-8e82-bdf417d61f21 | -8.80527 | -48.94976 | 2024-10-01 00:50:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4a92b6d6-0fc9-32dc-933c-19d565fc5e43 | -8.666 | -49.43466 | 2024-10-01 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0f33981f-1145-3269-aa2e-e0a4bed71589 | -8.66436 | -49.42242 | 2024-10-01 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bf78e013-6d9b-3937-90c9-3e914bade330 | -8.66272 | -49.4287 | 2024-10-01 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dac3ea1b-af66-3ad0-a25e-7e90f7d58db1 | -3.13358 | -53.74965 | 2024-10-01 00:50:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 90bf9d12-d887-3476-b499-b4579abc39f7 | -3.11421 | -49.41459 | 2024-10-01 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c4b3ec5-e78d-35ec-b974-89e6a7f8945d | -3.11278 | -49.40424 | 2024-10-01 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c0de679f-9975-3eb1-b0f7-ab571fd18eaf | -3.11135 | -49.3939 | 2024-10-01 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c786371c-22f9-3f66-b5a4-8b21250c9bf7 | -3.08816 | -50.48116 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 52887320-ee5d-34d7-8c60-5504656a939e | -3.07944 | -53.06505 | 2024-10-01 00:50:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| cda0d199-828b-392d-a1db-6d45c8cae2e9 | -2.95644 | -49.35859 | 2024-10-01 00:50:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 19ffee83-ef9f-3026-b7b4-ea3b57038ddc | -2.91656 | -49.52823 | 2024-10-01 00:50:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 77bd95e0-3a91-3b1f-bfd6-1f592142b644 | -2.91205 | -50.76666 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0936f733-165f-3e5a-a30b-31cf995e5a1e | -2.91035 | -50.7542 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 345.8 |
| 0216cb67-fd55-3005-a835-63261367bd98 | -2.90865 | -50.74175 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 684.4 |
| b8f7077c-80c9-3a4c-9e6d-d3615c58e131 | -2.90695 | -50.72936 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 10c97edb-8665-3422-86cb-9a18965d8a58 | -2.90526 | -50.71699 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 567a7ce6-4e35-3282-8ec1-3394234c7084 | -2.90165 | -50.76811 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 142f7e2f-09f9-3abc-bf97-9e690a76d483 | -2.89995 | -50.75563 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1356.9 |
| 365b8910-71a3-31a1-b128-db038a073092 | -2.89826 | -50.74319 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1009.9 |
| a79ccd6a-8d98-37d2-b3ba-62ad066323e6 | -2.89658 | -50.7308 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 5f4122d3-7b6c-3cf7-9cc5-23bcd191bb56 | -2.8949 | -50.71843 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d0cee5a9-0618-3acb-af32-e6c0f24c5431 | -2.89124 | -50.76953 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 12ca5e45-50e7-3019-b43d-335a15858e64 | -2.88956 | -50.75707 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 567.4 |
| d5f9e832-dbf7-37aa-aad6-d1b2bb34e307 | -2.88788 | -50.74464 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 564.2 |
| d6291e76-f30b-347a-a95f-c6714a184664 | -2.8862 | -50.73225 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 357.6 |
| 00d45c48-77e2-3ff2-95a6-274e65eff8ee | -2.88453 | -50.71988 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 712.7 |
| 258ec311-1ca1-35be-8955-3a9964b64144 | -2.88286 | -50.70751 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 884c05b9-7131-3b62-9530-9d3a9e604f82 | -2.87916 | -50.75852 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3107970f-d6e6-30cb-9e2e-cb2db4b5491b | -2.87749 | -50.74608 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 4ddfe61a-a7eb-3139-a1a4-7921b8d3db1a | -2.87583 | -50.73369 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 9f3c5a6d-ab06-3ccb-b946-e87d15ef22c7 | -2.87416 | -50.72131 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6f9b6ab7-166c-3f04-b033-0eb50600e28f | -2.87124 | -50.75283 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 6371631a-54df-3a30-bfb0-304d2feec993 | -2.8695 | -50.74043 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 9d20f908-811c-3582-a67c-031772c22739 | -2.86877 | -50.75998 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 0a0dbd86-cb61-3700-bb77-a96987d0c408 | -2.86776 | -50.72807 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0a16bddf-55c4-3459-b3d2-31a41f4ed920 | -2.86711 | -50.74753 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6c0d9268-2d00-329e-8a71-eceb1fbe6d6d | -2.86545 | -50.73513 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 298.1 |
| 9b8c2a42-0cde-3640-9855-6a8536255e5a | -2.8638 | -50.72274 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 306.7 |
| bc8799ec-2241-3dc8-91dd-0e2623e96b92 | -2.86086 | -50.75427 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 71e0e1c9-7213-3b82-bbbe-8681376e64f1 | -2.85912 | -50.74186 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.8 |
| 63e5f959-7681-3f1c-86a8-8ce854bc662d | -2.85739 | -50.72951 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1590.7 |
| bb13e846-f6ec-3ac5-8378-d9f75912081f | -2.85566 | -50.71716 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 434.6 |
| fb95b947-559e-37cf-90a0-766951ceba2b | -2.85413 | -53.32726 | 2024-10-01 00:50:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 22f76d1f-23ed-3c29-a957-48cda4d24c2a | -2.8538 | -53.32194 | 2024-10-01 00:50:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8f95be52-74e7-3048-aa84-7eed2ae45f78 | -2.85047 | -50.7557 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 24c1c27a-89bc-32d6-9a95-95fe5d827754 | -2.84874 | -50.74331 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f8214580-704d-3961-8794-6791206bf197 | -2.84702 | -50.73095 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 26351fac-0326-31fa-abaf-41446b5139ad | -2.8453 | -50.71859 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 83c8f8a3-7c5a-36d1-a970-2d2a375fa2a5 | -2.72224 | -46.72411 | 2024-10-01 00:50:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 82ff6c19-3f9a-381c-899a-29814e898500 | -2.49367 | -49.33979 | 2024-10-01 00:50:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b1d32301-960f-306e-a837-2c37cf368918 | -2.40447 | -50.34311 | 2024-10-01 00:50:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |


[Clique aqui para ver as próximas entradas](README12.md)
