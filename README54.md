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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d711065-fbf5-387c-9839-cc1ec7afb751 | -6.3052 | -56.0442 | 2026-09-03 08:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e7049dde-f8f7-3624-9c74-c91c957cd1a9 | -6.6883 | -59.9436 | 2026-09-03 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 458806c1-9428-3668-9ab3-f9928d90ff6e | -6.6883 | -59.9436 | 2026-09-03 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 75dfdb12-1a36-3c11-a31a-6c57beb80471 | -8.4295 | -54.7464 | 2026-09-03 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 9131a29b-7698-3650-ad87-8b282fe25b4a | -8.4293 | -54.7666 | 2026-09-03 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| e07beba7-6f28-35ee-8f95-68f4c371383e | -12.4033 | -44.8089 | 2026-09-03 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| be949288-2f93-335b-8b49-7bb85cb1851f | -12.4033 | -44.8089 | 2026-09-03 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 3fde9c45-8b8f-33d3-9027-deaab600e739 | -8.4295 | -54.7464 | 2026-09-03 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 1a5dbb2c-3dee-33ea-ba34-9fb93c9da4b9 | -8.4481 | -54.7452 | 2026-09-03 10:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| fa6bc14e-ec6d-3c51-97b5-b8eb8a3d5442 | -12.4033 | -44.8089 | 2026-09-03 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 1a55c043-f017-3642-95bd-ce0842054629 | -12.4033 | -44.8089 | 2026-09-03 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 36342343-f63b-3b7d-9483-e266762848e4 | -12.4225 | -44.8059 | 2026-09-03 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a2d5f706-908f-31d4-938e-9d015813c0da | -12.4225 | -44.8059 | 2026-09-03 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 34e093ef-a7c1-35ef-ae53-f9ef96811879 | -12.4033 | -44.8089 | 2026-09-03 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 10087931-fee4-37e1-af31-87ad5a01b03d | -12.4037 | -44.7856 | 2026-09-03 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 28d16524-7a91-347f-96ef-37b054821053 | -12.4033 | -44.8089 | 2026-09-03 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 2a6f5e06-ab1a-39af-99e2-a5183c7fcaf3 | -5.72812 | -38.57449 | 2026-09-03 10:51:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 24.9 |
| e82aabf8-671c-329d-bf7e-a3408ae73a42 | -5.73059 | -38.5583 | 2026-09-03 10:51:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| aae6dd2a-d2da-3c35-b453-572b50ed491d | -10.07051 | -39.58735 | 2026-09-03 10:51:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 2023d813-5227-3802-bd6e-efc56a68971d | -6.63052 | -41.71313 | 2026-09-03 10:51:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 4bb9c3a9-6979-33cb-8edd-0fabdce63b8f | -5.98605 | -38.16534 | 2026-09-03 10:51:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 766c997c-baf7-3397-8368-06e51bcea9b9 | -12.4033 | -44.8089 | 2026-09-03 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 5745421c-2673-3476-9496-c34ba14c80dc | -8.4295 | -54.7464 | 2026-09-03 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8d429430-08a7-3990-a79d-ed2416e0ad0b | -12.4033 | -44.8089 | 2026-09-03 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 2ed3b519-10d9-36db-ac64-7db28d660390 | -8.4481 | -54.7452 | 2026-09-03 11:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 2a5d332e-e57b-3ea5-bd52-cffedecd1e5b | -12.4225 | -44.8059 | 2026-09-03 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 57344544-3d2b-30dc-878c-9eeeba3252a2 | -12.4033 | -44.8089 | 2026-09-03 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.2 |
| a63690ac-02d0-354d-a6e7-a9724f167f09 | -8.4481 | -54.7452 | 2026-09-03 11:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| edad2dff-914d-36fa-8b37-3792d2e126c4 | -12.4225 | -44.8059 | 2026-09-03 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 58851d7c-b0c5-3009-8821-eedbf8a4d6ad | -12.4033 | -44.8089 | 2026-09-03 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 198.8 |
| 109931a0-4080-324c-9398-49d858481db9 | -8.4481 | -54.7452 | 2026-09-03 11:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| d1fc5a71-5402-30cb-b0dd-756836f7eed9 | -8.4481 | -54.7452 | 2026-09-03 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 0b6a75f2-a557-3b14-8728-2f4ce3c1fd3a | -12.4033 | -44.8089 | 2026-09-03 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f463d681-1868-3cad-a5be-768a172d6412 | -11.5634 | -50.464 | 2026-09-03 11:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| ba2bed41-f0c6-3946-8456-18c953168f27 | -8.4481 | -54.7452 | 2026-09-03 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3897a0af-e1e1-3803-9466-eefdf333b961 | -12.4033 | -44.8089 | 2026-09-03 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 6adfb917-5c0c-3ac4-bc52-4fccc51a65d9 | -10.9017 | -45.3049 | 2026-09-03 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| bd19ad11-e0f9-3d53-925a-ac2af8482c2c | -10.8822 | -45.3305 | 2026-09-03 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 43ea5016-e71b-31a7-9f83-44e50ce62399 | -14.8273 | -45.5349 | 2026-09-03 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e82bfbbc-0796-3690-b49f-df8471dc6ce9 | -11.5634 | -50.464 | 2026-09-03 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 077f38bb-c290-31da-8527-97603611e0ee | -10.8826 | -45.3075 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b21fec59-af26-32e6-98b9-7426e76c0485 | -10.1467 | -50.2525 | 2026-09-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 04651731-3619-3399-9902-807de0efdd47 | -11.3243 | -45.1317 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 1974b3a5-000f-3f54-91f8-4ff5b7fa78ac | -11.5634 | -50.464 | 2026-09-03 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d817bd18-b303-36ca-bd72-2f4409f9698e | -11.3247 | -45.1086 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7c88940f-ed57-3af3-b935-d2dd0da9af2c | -10.9013 | -45.3279 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| d0e9c49e-28d0-3975-a54b-35073fc09564 | -10.8822 | -45.3305 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 39b06a7d-b127-3c8a-b791-833611e35e1d | -10.9204 | -45.3253 | 2026-09-03 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a7d4dc7a-a944-338e-af15-0b24ec13a292 | 2.02522 | -55.87164 | 2026-09-03 12:27:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 30792d39-b59c-3e0c-9af0-754f501a76d4 | 0.17715 | -51.51243 | 2026-09-03 12:27:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 2cf68bb9-8bff-3a0e-a1a5-63894b8033f7 | 0.1749 | -51.49657 | 2026-09-03 12:27:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 28de0e88-8889-3e14-9a4d-8083ea87f2d4 | -1.78232 | -47.96969 | 2026-09-03 12:27:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| b68bbc97-5211-33ab-85ad-eb84ee5fc0d5 | -1.28085 | -47.7643 | 2026-09-03 12:27:00 | TERRA_M-T | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a4bf2a63-ce04-3543-ab77-e01ee681a526 | -1.02285 | -53.72102 | 2026-09-03 12:27:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 85ea6e5d-1a30-3527-a6d1-028cf1450bb1 | 4.34946 | -60.88899 | 2026-09-03 12:27:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 61a256ab-a93b-37c6-8463-b6d9df2271c0 | -8.43572 | -54.74417 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 55cd31f3-3e9f-31c7-be3e-0d58370d23c2 | -6.80935 | -59.09814 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0802fb8e-960c-3079-bb43-4ccbfa0726c2 | -6.67783 | -59.94474 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| daa8a139-2f78-32ff-b5a6-5300811c62e0 | -10.27741 | -50.02426 | 2026-09-03 12:29:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| fff5aafd-faa6-3629-91b0-86ab7bf8d032 | -8.78079 | -54.59476 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6ff616af-6178-35a4-9662-5025ff903f05 | -7.05063 | -59.21605 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d73e84a8-fc35-3333-9183-b238c2e49330 | -5.21318 | -60.0435 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d338b217-281b-3c2f-af22-32b6ef43b989 | -5.56349 | -60.17021 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| acb1e2d2-de64-3058-be9a-7b3c30743dc1 | -1.36236 | -54.63187 | 2026-09-03 12:29:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 093900d6-5b7d-314e-a3f2-5372055cbd20 | -1.47284 | -54.81219 | 2026-09-03 12:29:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1145a4ef-1299-3dec-ba5f-99878f6d1021 | -6.67291 | -58.76389 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 41e4f90d-bd28-3aa9-adfe-b1a4ce50f5ca | -7.62178 | -57.61428 | 2026-09-03 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 95db07c8-4187-3244-b745-af02288c5cee | -6.68704 | -59.94608 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 3aa58a5c-facc-3630-b738-25fa628f2d30 | -6.64899 | -59.44279 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6ff48892-8189-3b62-a2f8-f4c9b3ffc592 | -7.57365 | -57.69886 | 2026-09-03 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6b8abd2-1cba-377d-80dd-20882573045b | -6.68844 | -59.93641 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 30d78f13-2174-3415-8c81-e63421c4c76d | -5.94545 | -52.17071 | 2026-09-03 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 35d17903-4578-37f6-aed4-d0f58279d86d | -8.62444 | -62.55997 | 2026-09-03 12:29:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0faf2b94-e3d7-3621-9069-ed3361c28af9 | -5.57291 | -60.17154 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 445335ec-a909-317a-8603-3604b5186a12 | -6.22052 | -57.68027 | 2026-09-03 12:29:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c9782392-458f-37d2-89f1-6cc06a21f322 | -7.03817 | -62.97539 | 2026-09-03 12:29:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ba23b224-5d0c-3e72-95d8-5e61c5de6290 | -7.21688 | -56.75698 | 2026-09-03 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6cc9c77d-c1db-3342-bf81-8613ad2f0dce | -5.55444 | -60.23108 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 95b27741-b283-3b94-8e3b-dadf51a92427 | -6.11211 | -59.96512 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5bbcaf9b-283f-3bba-8c0f-a0098fde7a93 | -5.94777 | -52.15274 | 2026-09-03 12:29:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e09b0c5c-c880-3a9c-bdad-00c15122949c | -11.14262 | -51.52634 | 2026-09-03 12:29:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3853e04c-fb89-3409-95e2-7cf6dc854836 | -5.51678 | -60.18799 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 97c947ae-5417-306a-aeb6-0297177e0158 | -4.27031 | -55.15762 | 2026-09-03 12:29:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fcaa981c-ae40-3099-94bb-af3f95abd2d7 | -3.20561 | -61.2094 | 2026-09-03 12:29:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 34ba4234-dc1c-30e9-a81f-d269ae44f5e4 | -6.37325 | -58.28067 | 2026-09-03 12:29:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 19124bbc-34ae-3964-8983-34a832346d6d | -5.51826 | -60.17785 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c4089318-3b6e-34db-a912-e06f3a3b4ab4 | -3.54869 | -58.68338 | 2026-09-03 12:29:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a66ad1d5-458f-3717-8675-caa11872d39c | -8.44237 | -54.75097 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 5c9b9be8-787c-30d2-9678-ca6cc6498197 | -6.76064 | -59.4363 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| eb83e71d-bf13-3986-b35e-53bbf9560e36 | -7.60878 | -49.92737 | 2026-09-03 12:29:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 725305c6-08f4-3b9f-a6f4-7427634ba0ca | -3.49917 | -56.90435 | 2026-09-03 12:29:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e169f7c0-19d6-32be-9637-67b926123915 | -10.14491 | -50.24843 | 2026-09-03 12:29:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d22a75ab-80b2-3c18-8a17-ecc2cd101830 | -1.50777 | -54.26219 | 2026-09-03 12:29:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a5743bef-3502-3775-af93-7474ba9513c9 | -5.32845 | -60.14847 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 22f3a8da-d10c-3ee8-b97a-f9eda3f519b8 | -6.84799 | -59.34243 | 2026-09-03 12:29:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adcb6baa-48ce-3043-be25-98ca88f4af3a | -6.67642 | -59.95444 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 7437ed28-03f9-306d-8f6e-4826d520eb8a | -1.48225 | -54.8134 | 2026-09-03 12:29:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e576dee2-7c7d-3647-81ac-e58dacdcfa3b | -8.44424 | -54.68167 | 2026-09-03 12:29:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b3e10ea8-c42a-352c-b481-66455584ffc7 | -5.32994 | -60.13833 | 2026-09-03 12:29:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f4a7f268-b9a5-3b12-a440-98d88fe95dad | -3.76075 | -59.32036 | 2026-09-03 12:29:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |


[Clique aqui para ver as próximas entradas](README55.md)
