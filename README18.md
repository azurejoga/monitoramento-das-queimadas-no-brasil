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
| a57e6eb3-9f98-3332-b08b-b3f32031979a | -21.63429 | -49.84193 | 2025-08-01 04:19:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d27827d-6607-34e9-98bf-59a89666330b | -29.77873 | -51.17839 | 2025-08-01 04:19:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 2513b73c-759d-3a39-87c0-06134d34a7cb | -19.45804 | -56.88896 | 2025-08-01 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 002baa29-c9ae-3154-9cbe-2497c454ed94 | -28.88779 | -50.62926 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1878ef91-e4a5-367f-913c-80f5284a6f5c | -29.20365 | -50.7761 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54496414-4231-33bd-92d1-f6c03fe4e4cc | -23.51763 | -47.83624 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| ef5bf89f-d765-31b2-a3f8-96597c0f8f95 | -28.36738 | -50.03227 | 2025-08-01 04:19:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f38c28e2-478b-3b0a-ac62-c607646fb880 | -22.08621 | -46.97022 | 2025-08-01 04:19:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f6a78c6-1e1a-3031-9ebf-a3055592d385 | -23.51431 | -47.83562 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| d396b687-527a-3d8e-bb5d-3067121e3935 | -21.24399 | -48.56714 | 2025-08-01 04:19:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45a6f1e7-5acf-326e-84e7-8efce3f2ea9c | -28.15927 | -49.71626 | 2025-08-01 04:19:00 | NOAA-20 | URUBICI | SANTA CATARINA | Brasil | 4218905 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd8b9d8a-4f0e-3abf-b678-bd4d2a2c91ca | -22.84564 | -43.38259 | 2025-08-01 04:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bc4088c2-6cd9-35ca-9e2b-4de7d4c2bfcc | -29.20362 | -50.77843 | 2025-08-01 04:19:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2aaf7b4f-57e5-3719-85e3-d86a07c761a5 | -28.58765 | -51.23338 | 2025-08-01 04:19:00 | NOAA-20 | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 66498bf4-6bde-373f-9e6b-9df26e023ef1 | -22.701 | -48.04715 | 2025-08-01 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b549b3e4-3cb0-3da3-8f2a-e379edddac21 | -21.44526 | -57.14598 | 2025-08-01 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05122c07-3d9e-3094-a91c-c90f2cf8e233 | -22.62762 | -47.19649 | 2025-08-01 04:19:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74e310e5-7846-34c9-a1e0-0b77830eff42 | -23.51824 | -47.83246 | 2025-08-01 04:19:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 37b94fba-f4ef-383a-bad5-9d00f1034452 | -29.07159 | -50.9276 | 2025-08-01 04:19:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4dce388c-50ad-3461-8940-135f5819166e | -6.7294 | -59.1723 | 2025-08-01 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 232.4 |
| 2d87d85d-564a-33be-82c7-734510ac51cb | -6.7295 | -59.153 | 2025-08-01 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4cfaae58-e4cc-3f52-bae3-05b0a8ad8cea | -8.051 | -43.1237 | 2025-08-01 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| eea034fb-88bc-3e63-a0b0-2a607624d964 | -6.748 | -59.1523 | 2025-08-01 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ead892d0-6c29-385f-b177-c5ee6c841a84 | -8.0513 | -43.1001 | 2025-08-01 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 3cd88ebb-3ab1-3715-bd0e-a12291832319 | -23.5234 | -47.835 | 2025-08-01 04:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 049ddb43-738a-3e4c-842b-3b3b03169337 | -6.7293 | -59.1916 | 2025-08-01 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| c5f502e0-4da3-3920-8689-36ef43696009 | -6.7478 | -59.1716 | 2025-08-01 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 6b601f6b-5007-3633-8b97-c056fd740fb3 | -8.0324 | -43.1022 | 2025-08-01 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 8a09abf8-ad02-3b00-a92b-dbad249978cb | -6.748 | -59.1523 | 2025-08-01 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2992e0f8-0320-39d3-a1f8-dc476bbafd13 | -6.7293 | -59.1916 | 2025-08-01 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 04633fa3-9cac-3bce-bf35-3720deb40655 | -6.6143 | -59.9848 | 2025-08-01 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 02f1f36b-08db-3489-abf6-65952ccc8c8a | -23.5234 | -47.835 | 2025-08-01 04:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| dfea0951-4c3f-38f8-9052-6bcd7ae72d81 | -6.7478 | -59.1716 | 2025-08-01 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 1cea4839-be03-3f19-88c5-5597c9c1a1a6 | -6.7295 | -59.153 | 2025-08-01 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ef4ccb92-5048-3eea-97fd-363651a224da | -6.7294 | -59.1723 | 2025-08-01 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 279.2 |
| 4777e509-1fdd-3d97-9ecf-73674178650e | -8.0321 | -43.1257 | 2025-08-01 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| ca0beebf-0c6e-3bd7-944f-c6e160e3439d | -8.051 | -43.1237 | 2025-08-01 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| af8cd57f-6706-30c0-8e3d-38b06268ad39 | -23.5234 | -47.835 | 2025-08-01 04:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| 8bfba0a3-5271-3b79-9e64-6235d39eb983 | -6.7294 | -59.1723 | 2025-08-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 252.0 |
| 07538d87-7359-3daf-8a67-c55a9f9907c6 | -6.748 | -59.1523 | 2025-08-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4864d94f-88a0-397f-8ec6-5651195b7f11 | -6.7478 | -59.1716 | 2025-08-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| ee7c2798-ad28-371f-a6e9-2943dd5fea0e | -8.0513 | -43.1001 | 2025-08-01 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 623bfc22-98c0-3e3d-a2ae-acc55670fb26 | -6.7293 | -59.1916 | 2025-08-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ec0dfff2-2799-3708-aef6-9d9765394799 | -8.0321 | -43.1257 | 2025-08-01 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| a039786d-8ade-3b41-9232-0fb5c47a83a1 | -6.7295 | -59.153 | 2025-08-01 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 63f1eedc-3b2d-38e9-a196-bb7ccb655c49 | -8.0324 | -43.1022 | 2025-08-01 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| c4aff0d0-767f-3691-9d50-273309531a54 | -8.051 | -43.1237 | 2025-08-01 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 621d5cc1-f5c4-3d61-b9d0-bf8208ec1bde | -23.5234 | -47.835 | 2025-08-01 04:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.9 |
| e5d8828e-0072-37b3-a1d5-43b49ee72fbc | -6.7294 | -59.1723 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.0 |
| d51b864e-db40-3338-92e1-200a8cdb415b | -8.0513 | -43.1001 | 2025-08-01 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 971595ba-ba4f-3ec5-8988-a6d13ea5c540 | -6.7295 | -59.153 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 348644ec-aca0-3fa1-9b82-fc6138f813fd | -8.051 | -43.1237 | 2025-08-01 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| dc6c2175-90aa-332c-9d44-a6bb77a4e1cf | -6.7478 | -59.1716 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 5f171a9b-7ef5-3983-b36a-7ad4f7cbffec | -6.7293 | -59.1916 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fdfb9001-838f-3df7-8d0d-541c94351332 | -8.0324 | -43.1022 | 2025-08-01 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 5e63182d-b018-306c-9e30-201dee987b4c | -6.7477 | -59.1909 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2a522dc7-1273-3f25-9b04-85a42d8ed022 | -7.7253 | -45.1008 | 2025-08-01 04:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| f1041eb6-8f70-3410-8774-06c5b3ab4584 | -7.7255 | -45.078 | 2025-08-01 04:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ca6d437c-0543-33e1-b5c9-7b934025a74d | -8.0321 | -43.1257 | 2025-08-01 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| 8bea0a4d-f49d-375a-8a56-45e71c9722b0 | -6.748 | -59.1523 | 2025-08-01 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 51ae73ca-eeb9-3153-89f6-4bebb7112bb0 | -8.0321 | -43.1257 | 2025-08-01 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 8773dea7-ff89-3784-b8a3-12bbc6181248 | -8.0513 | -43.1001 | 2025-08-01 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 8f948a02-3d5c-3658-b516-ea6834824c09 | -8.051 | -43.1237 | 2025-08-01 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 6c19a7e3-f3f1-3b3e-912e-c0d6258cea1e | -23.5234 | -47.835 | 2025-08-01 05:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| 58061b2b-f8a9-3074-b248-43b91f3f47b1 | -8.0324 | -43.1022 | 2025-08-01 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 5d7f1a03-3f74-3cff-8183-6b0b7d7dde47 | -6.7293 | -59.1916 | 2025-08-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| bc545c19-2dc4-3b91-bb9c-b9d7448f5277 | -6.7478 | -59.1716 | 2025-08-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 5856f7da-5e50-304d-84b8-802e2fa844e3 | -6.7294 | -59.1723 | 2025-08-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 245.8 |
| 7fedeb9d-e0e8-36b6-9d64-fb592a913c46 | -6.7295 | -59.153 | 2025-08-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a567a969-38f8-3113-aa8f-9746109f58c0 | -10.0815 | -46.7441 | 2025-08-01 05:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e1569a48-edeb-35db-8ec3-f3b2304f9d5f | -6.748 | -59.1523 | 2025-08-01 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4d78db93-fbd4-344c-b9fa-38ba9b58f3ad | -6.54468 | -56.20208 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93518e38-bebb-3dfc-b2f6-e0506df3a291 | -6.8335 | -59.26787 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b2bb63de-396f-32f9-8ffb-60593568c6fa | -8.0359 | -43.12174 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 95c8d99b-96bc-37f7-b6b8-109ea39a5342 | -6.7391 | -59.15607 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9f2bd12-1495-32ac-b2d7-695467548173 | -6.51275 | -56.21125 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b812c6-d4f3-37af-87c1-082256545550 | -6.52652 | -56.20986 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c809f8f4-105b-3b4d-9bb8-cbf70c4f0e98 | -6.51991 | -56.20882 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d704d009-0f57-3b0f-b33e-1e9edd8bf88a | -8.04277 | -43.12276 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 551bf6be-7f85-32bf-9c86-cf1ca9fce198 | -6.73483 | -59.15963 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| df3b3993-d271-3ec2-a281-b418c72cd67e | -6.62411 | -59.97623 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 65412ffc-0235-3060-8b78-cb3d7e18702f | -6.66852 | -56.40924 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c88d66f-b753-33a0-a42f-dd8c2fa4be43 | -7.17818 | -56.71505 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c2bb6c5-2bc4-3253-bb23-291068bfa8c5 | -6.6663 | -56.40181 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca2dd46-1fea-3e07-9ed8-ef1cb4fd30de | -6.67292 | -56.40283 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e88a3734-3e29-3a87-80f5-89713c2c9b2f | -6.73572 | -59.17682 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c0bb2244-68be-3d5a-a507-e1ad918462ed | -6.73144 | -59.18039 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 94aa705a-818e-3aaa-9f24-fe9941833e4e | -6.51053 | -56.20382 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456505a0-9e5a-3364-a1ab-2aa03bc7277a | -6.81542 | -59.265 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 90ce61bd-23cb-31ff-9300-5e84a7e91eb2 | -6.68231 | -58.8587 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0a4392e-694d-3e52-9cc3-62f1491100c8 | -6.51162 | -56.19691 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c6e84df-cca3-33fa-980f-ad0ad01f537d | -4.07064 | -47.97095 | 2025-08-01 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780ff4cd-0491-3fc8-a03e-ac1ea7499f08 | -6.66907 | -56.40578 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2547b02-7661-3220-8bc3-fa4c79e0533f | -6.56391 | -56.18738 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc7d5952-426e-311b-8dd6-58d538d8fbd9 | -6.51937 | -56.21228 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2038d34-a2f5-3c48-bb44-9423179a5166 | -6.55622 | -56.19326 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8e2d1eb-f39a-3b42-8411-4f06a513b67c | -6.73707 | -59.16851 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 206288ec-1f13-37a7-bede-0388774da7a8 | -7.0716 | -60.04195 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ae25d9e-a17c-3646-a170-f295f9db21c1 | -6.8292 | -59.27146 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2dc60b55-4d6d-38d1-8a59-fb93a70c5efb | -6.74563 | -59.1613 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README19.md)
