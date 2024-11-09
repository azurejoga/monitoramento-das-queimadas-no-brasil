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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17417995-7e8f-3c69-a1bb-37518d713aef | -2.41508 | -48.52071 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44267571-30ea-3019-8791-05c8177e7716 | -1.31867 | -55.88438 | 2024-11-09 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1be5b0d-6f53-3cd1-8821-e66f61c5bdf3 | -1.15822 | -51.99697 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 837acb97-df44-3430-910f-1ac4d88724b8 | -2.58074 | -51.92304 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3518406-8e02-35fc-bd57-64812976df9d | -2.81141 | -51.81125 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 437b5ce1-e85a-3e5d-bdc9-a56d9252dd9b | -2.21336 | -50.77616 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25a4cd1a-843e-3d20-8e13-200ad7486bd3 | -4.37987 | -48.57886 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8979da6-7f27-3b35-a5e1-bb816465d137 | -2.68107 | -51.82101 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a071192c-876a-3569-9229-86ef6a27b808 | -3.24362 | -46.49249 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 474f5dce-1c80-3d40-86c7-8610787eb2d8 | -4.06049 | -48.30672 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1905b9e4-0766-3368-97bf-a7058f6c530d | -2.84093 | -49.43628 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6e07af5-c4e9-3273-b21e-8e7aeca67b3d | -2.57858 | -49.13948 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 416c6051-24fa-32be-b61a-aeac8d6ab761 | -2.86954 | -49.37317 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55087ed2-21d5-3d18-a959-09b59d5a0044 | -5.17449 | -44.00138 | 2024-11-09 04:55:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb917730-3398-37e5-953e-e8c9b707adb4 | -3.29177 | -50.08221 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cad3888a-bf3f-3a04-84a5-29702010bbf8 | -3.69524 | -54.61532 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2e9e553-d0bc-3b65-8292-8507fab91043 | -3.71522 | -53.40023 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d59fd1c-5acd-3d17-bf25-e2bf19f8a006 | -1.52344 | -52.18951 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 61e2f25a-4745-3ed2-aa9b-cb93341e8756 | -3.24194 | -50.4482 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90ef59a8-a405-3b15-a44d-8ed2a1b02093 | -3.71854 | -53.40074 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df429d0-fc63-3bd4-b3d7-3fb39a698f41 | -4.6277 | -48.72364 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01525483-1857-3fc6-99cc-b3f2421e66c8 | -3.32861 | -49.91079 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c8d133a-d5a3-312f-b049-18d085f92165 | -2.28688 | -50.67553 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e503909f-42b1-3e37-8010-44a6fc21a083 | -2.31281 | -50.64762 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc673ab9-0f94-3675-bb3d-de7a867b0c7c | -3.5014 | -51.02717 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbc0c5d5-38f1-3c9a-adb7-4e9ba1c80799 | -2.77935 | -49.38507 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c616907a-e7d9-34b5-a1b9-7fd4410efc74 | -2.94065 | -54.12655 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 120c48d5-7837-3679-8b73-ec204b0ccbeb | -2.77268 | -54.03559 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a54c82f-44cc-3e74-b43b-8ba9ab73c39c | -2.72516 | -51.71712 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49f3e93f-38e6-3597-925f-deb89991281f | -2.57842 | -51.33532 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38113423-ef74-3a2e-8a97-d96afb32593a | -1.15601 | -52.01096 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbb6ca86-1d4e-3731-8d3b-96e8d3cc2a14 | -2.23429 | -53.77678 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ed3f3ba0-c4d0-3aa0-a01d-4960052de6ce | -2.86683 | -50.3276 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f5a80a2-2c40-361d-9b95-508c68f28200 | -1.11531 | -53.6013 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7b458f3-9a47-3182-95b4-4344ea4173b1 | -2.74556 | -54.12081 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ffd780c-08b1-35dd-8c6c-db5375bb239e | -1.56508 | -51.29943 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a222b592-50ef-39ce-b295-1869149223a6 | -2.35962 | -54.74882 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3cadcd0-fcd9-3de0-ac29-efd6560ef6d1 | -2.27575 | -50.67779 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5b5c869-290a-3ff8-9122-72654399a4be | -1.77552 | -52.34653 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fb9ec11-02c0-3866-9fc2-54adfc73e19c | -2.36522 | -46.85896 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84d7a691-335a-3f62-bf58-05629546b39e | -2.94116 | -52.70547 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01d3c3e8-c193-349b-9abd-54032fa1c401 | -2.37726 | -46.78089 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca677050-85ef-3fd7-b65d-02fe73edaecf | -2.74501 | -54.1243 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c694ebae-2c86-3399-a808-bdad72b0b300 | -2.61178 | -51.748 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a6f83b-aeff-34f3-874b-207b2c241246 | -3.25559 | -48.74578 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69732c57-d342-30ef-bbe8-738ad42d7005 | -3.0214 | -48.08279 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febbce0a-097e-3f7b-88db-d6a4b5ebb870 | -3.58792 | -50.23973 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08340c64-5732-3318-b81d-31f528fb067a | -1.15153 | -51.99593 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 519bbfce-2be4-38a7-8e2c-57e24a38a6e2 | 0.62105 | -60.09307 | 2024-11-09 04:55:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 164ccac5-8f69-3635-ba3a-4ba6adf37fd0 | -3.23246 | -50.4384 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e05300ed-af65-3f1e-99b3-123866b74d83 | -2.72499 | -54.14268 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99759939-8272-3410-a74e-0bd5f7404028 | -2.082 | -54.69499 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bac5844-8cc2-339b-9421-10a8b83c9517 | -4.21482 | -48.68625 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8f33270-8899-30c2-be62-aa97331782bd | -2.77541 | -51.9962 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6c27063-18a3-3c52-b4e7-cb57f2f401aa | -2.40525 | -50.56451 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086e4e0c-f7c3-3174-a965-75a47ef87baa | -3.24131 | -50.45222 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1e2359f-a0de-38fd-ad3a-4c70a24a6677 | -5.14027 | -47.7068 | 2024-11-09 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 650284f1-b87f-3397-aa16-737478e589c2 | -2.86382 | -54.09968 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bb8f32e-3654-39ae-8082-00e851ac9991 | -1.24272 | -51.77552 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 632c5430-5308-3bd1-be36-9d8fcaadb3b3 | -2.50588 | -47.62027 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9375284b-fda0-312b-862f-c10f49e0a70f | -2.58811 | -48.20559 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b491f5-50f9-39bb-b41b-65aae1899761 | -3.74344 | -52.0376 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 616dc7d6-644e-314a-8da6-5013eea8b7d7 | -2.40833 | -50.30754 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bb1c2a7-18d2-3def-9e31-d3f1e1f925f8 | -3.12454 | -51.10582 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58b225bf-8b0b-35ee-ae2c-6203cd099126 | -3.54583 | -43.56031 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4fd85785-5274-34e4-b96e-204d36cf4b42 | -4.29158 | -48.58706 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c600954-deb7-3b98-bcef-e23ed76cc0bd | -2.37031 | -46.85534 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c48448a5-ff9a-3f77-9d37-c06f2f6c4676 | -3.03869 | -50.36502 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df38796c-ad50-36a3-9a87-edb807b6b830 | -4.25444 | -50.98049 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71686ee4-3c3c-36d1-9756-7c5cf16849da | -4.09804 | -55.06661 | 2024-11-09 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8039e6f-4700-3407-9fd0-79b0fc8e12e0 | -5.44627 | -44.81847 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 642d36ef-d91e-3554-937e-e1851eb9c9c6 | -3.30117 | -50.14255 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0037301-96cf-390b-9ab9-5a0fb2801418 | -4.20772 | -46.69453 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d844385d-2896-397b-ac97-51f88ef95535 | -0.91218 | -52.71816 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79a3c290-8371-3eeb-b5f1-1e09e8356b87 | -1.82523 | -52.02821 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fd0c59f-0b74-3547-8b50-cbb22d614fb1 | -2.86991 | -49.22488 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d9e943f-8a4c-3cbd-be11-0741c2980ad2 | -3.54728 | -43.57355 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac678acc-93fc-3cb4-b04b-3299d6b0e50d | -3.88999 | -50.23722 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa891bee-15dc-392f-8888-247e890092b9 | -2.8359 | -52.90196 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dba4a07c-aa9f-34ae-84e0-a3e92acf2f3f | -2.13583 | -52.44837 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefeaac2-74ed-3b6a-8e3d-040ed15353e7 | -2.85573 | -49.8648 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6274c504-af1f-3966-bed8-058642f4caf5 | -3.12742 | -51.11017 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f267cc8a-cc39-3e8c-833f-c016678eac76 | -3.11282 | -51.29359 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a250f49e-4afb-3078-bc96-d025c3a1e586 | -5.67221 | -47.99389 | 2024-11-09 04:55:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61c9384-59a8-3cce-baf6-61511ea51ad2 | -2.87651 | -51.30771 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b21fd257-1f7a-3da8-a202-4b155d4a7f13 | -2.99849 | -49.23454 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27de10fb-5c28-3eab-a5f2-51d2dbd01472 | -0.40615 | -51.47614 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7130493-5643-3288-86df-8209ca7875df | -2.08257 | -54.69137 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac8e8d1f-1ea3-3941-b7af-bd8a7df91e25 | -0.91226 | -52.56647 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c57b6b9-e75f-32fa-b977-efadadbe71e1 | -3.22975 | -54.86086 | 2024-11-09 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a16ac651-795f-3b93-9c24-d3f7313025ba | -1.3791 | -51.44164 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019f22a2-e546-3d56-ae38-fb5cc2842015 | -2.28478 | -53.78111 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2609647d-9e17-3f9f-9ece-819d2bec319c | -3.9587 | -48.12512 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4029162-dac5-3c3a-b6c9-1ee9f8f6633c | -3.67266 | -50.22065 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4fb957c-8653-3261-84f0-838cba90a68c | -3.15845 | -54.48814 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05161063-5150-3181-84be-0ad5675a67de | -2.23423 | -48.4264 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9630302-e153-32dc-bbd1-3119e68164e5 | -3.27017 | -52.74236 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e690fd-6ed9-3260-8ee1-595df3ce8d15 | -2.87937 | -50.41275 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60031f71-c776-3b40-a149-f8b83dd303c5 | -2.81119 | -48.45713 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c116b480-bcba-3da9-aace-b5eb7b912034 | -1.12881 | -53.72495 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README80.md)
