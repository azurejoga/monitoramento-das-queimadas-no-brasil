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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64fd519d-aae7-346b-8431-80d57890369d | -3.60384 | -48.92062 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8909537-d6cd-3351-8e5e-59f4fe8ab71d | -3.70257 | -54.39558 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a08e3992-0dc4-3118-843e-c34aa1edd880 | -3.12211 | -44.99323 | 2024-11-10 04:38:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d624d209-4f1c-3fa5-9b01-d55a1ac64d0d | -8.38033 | -44.13722 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28c9228a-1934-36bd-b2e7-88c0c70788ff | -3.66916 | -50.26373 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e29f0310-cda7-3063-ac29-29b5db637188 | -3.05327 | -48.03554 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 400a43d1-4204-3284-8047-05938a3bf839 | -7.72381 | -49.89838 | 2024-11-10 04:38:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e48d200f-0d4d-3221-946c-9dd8a2dc06c9 | -3.95905 | -46.70246 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 695142ef-bcd8-3416-b93f-d6127a4ef1d2 | -3.11698 | -54.28021 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72448fd4-1409-31bc-aa2d-f8436ebe27f5 | -2.4668 | -53.97469 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6493908-1e3c-30a2-836f-629320a1761c | -1.83017 | -55.6302 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb578fa3-b8a1-3ffd-937f-5915667bc4e2 | -4.36851 | -48.15073 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 962d4136-94af-3c29-8940-ae5313b778ae | -2.87327 | -46.66246 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cee7ebce-664c-3d58-bceb-5b47837898b0 | -4.11986 | -43.58958 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7c5a9f38-10df-37eb-bbb6-2b77252d0240 | -2.8406 | -49.23447 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 562a516d-1289-3b8b-b9c0-13ad557c608a | -3.17119 | -49.09003 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e809e35-7e4a-3e6b-b248-c72228987492 | -3.11301 | -45.96906 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a66424-b586-3b7f-8c8b-8154503346af | -4.38154 | -49.42298 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d266669-c899-39b3-bed7-e763d8c957c0 | -3.27788 | -51.09231 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 711aa62b-6080-3bd7-9c5c-693c77466a1b | -4.1654 | -48.60206 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c3a0c49-ea73-32ac-863f-f590e4f512d7 | -4.43552 | -44.6275 | 2024-11-10 04:38:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 67e3dbe8-e717-3871-ab04-b7acf38d5c13 | -3.47581 | -50.38297 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66ef6ac9-4ad2-368a-a5dd-f217b19d03e5 | -6.23723 | -44.14058 | 2024-11-10 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9d5e25b-6dbd-3a28-ae18-d6c5a8d8c2aa | -2.6827 | -51.82251 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a908d96-f86b-30fe-a5be-6b6eea7d9543 | -3.00343 | -49.03926 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 868a50ff-25b8-3e95-8a4b-d540558cae12 | -2.11205 | -51.09559 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ba5e71-4fab-3d91-a21b-8a89da341776 | -2.91471 | -49.51463 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7176f955-53f4-3e69-a89c-829883e4af27 | -4.69456 | -49.62188 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e75c786f-37cf-3879-8dbd-a7d403de7b88 | -4.10009 | -48.97385 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6aa116fc-a3e6-32a1-951d-ce8a762a8d70 | -4.707 | -46.38119 | 2024-11-10 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0115a3e4-6dbf-3f3f-93fc-b57c310c2910 | -2.46189 | -50.41222 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14be91bf-6be9-360d-a11f-6b6323bdf9a5 | -5.38348 | -42.76503 | 2024-11-10 04:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 727e0efd-8440-3e1d-a3f0-d333c4d8f592 | -3.74967 | -46.14166 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede047ed-b016-301c-b4aa-51afff9e81ed | -2.61346 | -48.2078 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e087889-3e72-35ee-ad1a-c4f481c91e07 | -3.67031 | -50.25651 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34cf3f89-a46b-301b-80ab-b1ca960a46ac | -2.84145 | -49.44581 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0438bb4-0aca-3399-b77f-2f7ea6a0a698 | -8.38874 | -44.13848 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5cbe6c1-435c-3d27-8b54-b94374672697 | -3.15431 | -45.95924 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc45ab8-f1e9-3c74-ab43-e427b74462ad | -3.96371 | -49.00216 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 574b1759-eee4-3347-9f4d-3b41714c2441 | -5.69238 | -45.1776 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d984513a-e239-3dff-9c4a-853a48fc7fe7 | -3.14432 | -45.95367 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58b5a864-9db2-3b71-88e5-025a4a4f8059 | -2.90616 | -49.24458 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fe66236-88fe-3a04-8668-1a4703c63457 | -4.82039 | -48.67667 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 495ca752-63e1-3426-b99e-dff0a3074d52 | -2.72386 | -49.84073 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1783f15-16b9-39bd-993c-db6f3b90d41d | -3.86887 | -50.26126 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f41178b2-3a91-3bc9-980b-27fbbe950a58 | -3.09717 | -49.42781 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ae319cc8-6d22-327a-82e2-dc692e21a072 | -2.41881 | -51.95596 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 82ab3725-508f-37fa-b20d-f42f7413060d | -10.00177 | -48.4903 | 2024-11-10 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cbd2d9d-9fe2-372b-a476-b5e6d188b567 | -2.30632 | -50.46472 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcd81b93-b6ba-3cd4-af19-59e88d8b3e42 | -4.7564 | -48.93224 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c0406c1-85b2-3b7e-809e-4618e29cca33 | -4.74887 | -48.80716 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4757ef7f-a102-3333-aa09-d5fcfc5871c5 | -3.1325 | -50.4357 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1114c513-e7a5-32c2-b358-9c5f3a20342b | -3.91878 | -47.95238 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c4d0acd-f5da-3b22-8d20-de03997df6d9 | -3.5101 | -54.03485 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da53991b-2464-371e-8a0e-71e5a7ba97df | -4.61069 | -48.63292 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ccef379-c3a9-3463-8501-4e79cf6ebc61 | -3.86963 | -51.97858 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a17c5735-2ed8-320e-9182-aa3119ce4084 | -3.61474 | -55.47656 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbe0342f-1e90-3823-a923-44a7044e5730 | -2.45796 | -50.39254 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333c7ab1-a0df-36f4-86f7-a3485c2f40a8 | -3.14968 | -45.94238 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf0e5c3-f179-3660-bd30-58c06ac3d6c1 | -3.0541 | -51.07062 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3089cc12-4f5f-3738-83d4-63b8acebb908 | -3.06931 | -49.53836 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e88f85d-3c33-396c-8499-cdce35203087 | -2.85192 | -48.453 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f958085-837e-3b8f-b6bc-c2c3be18ca9a | -1.46939 | -55.65312 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bb58ca0c-f4fd-3b18-bb72-084723bd4a75 | -2.0857 | -52.29922 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a668eb4-7877-37c3-8b17-1aa9f6c3992a | -2.86729 | -49.5108 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37aaf3e6-b048-3ebc-877c-f6f2b680c328 | -3.97859 | -48.12949 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd51ed2e-f940-3dc5-bee5-dccc50850998 | -4.88732 | -48.63747 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e35767d-5e6c-3d16-886f-ca3b639e1ddf | -3.07713 | -49.53233 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 452c91be-b363-365b-9dc9-2f28bd6c733d | -3.52594 | -51.65974 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14e29a77-85a5-3269-a08a-5ca3137bfa5e | -5.72253 | -42.71308 | 2024-11-10 04:38:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e09040e-14f0-3472-be8d-7dd442c1a4b8 | -3.59134 | -49.92096 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 676c4345-1827-330a-b974-fd11fd528922 | -2.4246 | -53.89025 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb5da43d-8e3e-327c-850d-415222847dc0 | -4.28716 | -48.6248 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2a10b26-f8d1-329d-aaaa-73212a1d3448 | -3.2385 | -50.2714 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce6ba4ac-f435-37bc-bbf6-8b59b81573d0 | -1.95573 | -53.06884 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d141c96-2feb-38a2-91e5-1357eb0b3a26 | -2.60831 | -47.95916 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 470669e4-65f0-394e-8b34-0e215867d278 | -3.95033 | -46.3819 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c104dadc-f774-32a9-aff5-520f2c477415 | -3.95806 | -48.12981 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 61e11e6d-d45e-3c83-ae9b-5d5d3d8838d0 | -3.01477 | -47.95493 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc5910bb-2d4a-3108-bc37-c71abc55219c | -2.41827 | -53.66856 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec8463a5-53c2-3107-9c5a-030725b4b454 | -3.95209 | -48.16806 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f4c7b9e9-a64c-3a83-85aa-eb341f56d88e | -4.06792 | -48.31772 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25a6a44a-a3ed-3e8e-a41c-bb1ef152750e | -3.68754 | -55.48871 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1abe3c16-57b3-39bb-9e16-a82630b14b9d | -3.22597 | -48.25014 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fdcbcae-c6eb-3961-920b-9b3c82a81e5a | -2.65814 | -49.39862 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2af954dd-fda0-38d0-b557-ed105840d5d1 | -2.32809 | -50.48352 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e201f1a1-7f00-35b8-a72e-de32c1f4c827 | -3.06711 | -48.03416 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 21f1f105-45c5-33e4-ba2d-1cca718d293f | -3.96323 | -48.18407 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 3271309a-3c48-30ee-a5bf-226332e2f7ff | -3.82351 | -46.52425 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9349853a-7ab6-377d-9efb-0925fe316bc2 | -5.84082 | -49.83852 | 2024-11-10 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5e5cacc-b390-3002-a9c5-78fbd3c21fe2 | -3.31274 | -51.66216 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7718e07e-b1ed-3cb7-9371-85571db789f6 | -2.53917 | -49.30127 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5dc6f99-8c22-346d-bce9-b0e137818bb4 | -3.41848 | -51.20637 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65f0050e-8884-37fa-a202-7d49ea0baba7 | -4.62733 | -49.08839 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66945d24-5351-389a-8769-e11fb7a86b2a | -3.10009 | -45.95897 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47ad012d-320c-3a81-b46a-2f039acd0084 | -2.65921 | -48.56061 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 152c4bfc-9876-39c7-b278-2b56614163df | -4.09687 | -45.69899 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a096e04-02ca-378f-a912-1084f4aad278 | -3.95915 | -48.12286 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3a2ffd1c-666c-332d-937a-5c4700453d71 | -2.33554 | -49.62341 | 2024-11-10 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 919a9dea-dc78-3645-86a0-c88b407045c3 | -2.45783 | -49.83944 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README85.md)
