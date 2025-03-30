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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e678f7e0-fc6c-362f-b54c-92c79e85d8cc | 2.7267 | -60.3916 | 2025-03-30 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| aff9c9b9-a6b1-3162-8e74-b8af96f1490f | 2.7267 | -60.3916 | 2025-03-30 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 78c68468-2de8-3adc-80c6-ffc3490096f1 | -12.38 | -38.8979 | 2025-03-30 00:20:00 | METOP-B | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f3fc5ba-a220-39ed-87da-584290615c9e | -12.375 | -38.878502 | 2025-03-30 00:20:00 | METOP-B | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2b0f8a03-210b-38e2-ae40-f3aa3f00e1cb | -18.2719 | -47.3004 | 2025-03-30 00:20:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1146034-06e6-3c26-9687-edf58acae736 | -18.2735 | -47.307701 | 2025-03-30 00:20:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3518aaf9-0f47-303a-8a3c-76431f42d3b5 | -19.9784 | -47.6552 | 2025-03-30 00:30:00 | GOES-16 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d3321100-6a37-3f67-ad43-2b99e6b32602 | 2.7267 | -60.3916 | 2025-03-30 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 795a17f3-827d-3e0e-85e5-d180c4dcb3ca | -19.979 | -47.6318 | 2025-03-30 00:30:00 | GOES-16 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 9b2fed45-0d3c-3773-be44-2a37e27a90bc | 2.7267 | -60.3916 | 2025-03-30 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| aa138c6a-f365-3e58-b31b-74e8136ee853 | -12.3897 | -38.89154 | 2025-03-30 00:41:00 | TERRA_M-M | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 1c4093ce-c9b2-3fb5-915a-6f112207f2b9 | -19.97746 | -47.65055 | 2025-03-30 00:41:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 3dcb77ff-759a-3cb3-81fc-13e6dd431ffd | -19.96803 | -47.65173 | 2025-03-30 00:41:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1366b099-b5ad-39af-956d-8f2ea06fbd8d | -19.96941 | -47.66271 | 2025-03-30 00:41:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 15e04135-849c-3531-8065-22e7f813baae | -17.16929 | -42.83747 | 2025-03-30 00:41:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 283414ca-a128-31b5-a5f1-73d63acc3363 | -19.97881 | -47.66124 | 2025-03-30 00:41:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 738580bf-c09b-3795-82cd-894e96c64ea6 | 2.73478 | -60.38987 | 2025-03-30 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ed675d6e-9b54-31a6-b993-7510a50c02e5 | 2.73716 | -60.39503 | 2025-03-30 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f7bc2b17-c9c2-3a91-a3d5-e06fff149b2a | 3.38999 | -60.03175 | 2025-03-30 00:48:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 4096d223-1371-32b0-a9bf-329acaa2e73c | 2.7267 | -60.3916 | 2025-03-30 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a9c347b4-28bb-3908-b08e-f3143a3c59f4 | -30.46242 | -55.31431 | 2025-03-30 02:17:00 | TERRA_M-M | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 48.2 |
| 11323cee-396d-3a5a-b74f-b772398f7417 | -8.38973 | -35.02635 | 2025-03-30 02:56:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d3ef272e-3067-3377-a08c-918cbf109e8d | -10.39811 | -37.48408 | 2025-03-30 02:56:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 25958f38-016a-3a15-b06b-4b3e160c3079 | -10.397 | -37.48976 | 2025-03-30 02:56:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 613b1359-a7d1-305e-8b97-ec6d9b43cb07 | -12.38072 | -38.894 | 2025-03-30 02:58:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a72da910-857d-30cc-99b6-949455f56893 | -12.37933 | -38.90052 | 2025-03-30 02:58:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 08643423-b80a-3f37-9bb6-bb3eaa97bcbc | -12.38754 | -38.89565 | 2025-03-30 02:58:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c05d3863-a477-34b0-8750-7e56fc53f0a0 | -12.38616 | -38.90211 | 2025-03-30 02:58:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 469eae5a-71ed-3514-86d1-d69950277385 | -7.47657 | -34.84235 | 2025-03-30 03:47:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8bd51de4-2c61-33c8-8a9e-4960a19a9149 | -7.22943 | -35.78313 | 2025-03-30 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61a0acff-f330-3d6b-8618-7e8f94f837ba | -7.22608 | -35.78262 | 2025-03-30 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d4242971-6896-3307-86fa-e5ba4a5043a6 | -5.79646 | -43.61872 | 2025-03-30 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26b3e8dd-247b-38c9-aa77-27aed33a4a3e | -8.07351 | -34.97667 | 2025-03-30 03:47:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c72aed33-1699-3f00-b410-aa6795568c13 | -15.56786 | -42.61553 | 2025-03-30 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4db0b81d-1671-36b2-9f9d-94e442c5ddf1 | -15.38262 | -39.21534 | 2025-03-30 03:49:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d75808f9-9921-3edc-880f-ea413f10007e | -12.38201 | -38.89592 | 2025-03-30 03:49:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 497ac485-41b4-329f-80fb-286294ba665a | -13.37775 | -41.3269 | 2025-03-30 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 023511df-8874-33bf-83a6-97fb32987c7d | -12.3881 | -38.90057 | 2025-03-30 03:49:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bf83604-7486-388d-8a28-acecff5f1089 | -9.61458 | -36.76191 | 2025-03-30 03:49:00 | NOAA-21 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5193cdc5-461e-3188-b746-9c89ec3259d6 | -14.13663 | -41.69063 | 2025-03-30 03:49:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4b16f65-9613-3c57-b787-d127076626c8 | -11.32795 | -37.52981 | 2025-03-30 03:49:00 | NOAA-21 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| bcae2576-255e-3510-b082-48d6ebc9aab7 | -15.49155 | -39.8139 | 2025-03-30 03:49:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4cb8941-23ce-3e79-ae54-d27308a666d3 | -16.32702 | -39.56576 | 2025-03-30 03:49:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 939686dc-fc24-33c7-a2be-22d2f416dd8d | -10.34844 | -38.48279 | 2025-03-30 03:49:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a80dfa5a-c57a-3eb8-9124-b4f0ae6fd87f | -13.68857 | -39.86882 | 2025-03-30 03:49:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e8be0931-4474-368f-9616-8ad2f2841ef2 | -10.35177 | -38.48331 | 2025-03-30 03:49:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ec965cf-21be-3aad-a4cf-c9bd2afc2b23 | -13.96378 | -41.49051 | 2025-03-30 03:49:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 46be7c0b-7b1d-37d6-bbe7-76e7b0e2ae1e | -10.39993 | -37.48533 | 2025-03-30 03:49:00 | NOAA-21 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2f2429e6-7cc7-3cab-aa80-343d31e9aed2 | -13.96022 | -41.48989 | 2025-03-30 03:49:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 133575ff-3090-3fb8-9fd3-a00216fb838e | -12.3859 | -38.89291 | 2025-03-30 03:49:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9b0fa107-10b2-3757-a21b-649dda2f8eab | -12.51981 | -39.39776 | 2025-03-30 03:49:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 117da0e9-94a7-30b7-a452-4a88d8a7ee45 | -12.38866 | -38.89701 | 2025-03-30 03:49:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1f2112d0-6a51-3508-a99b-8b93c04cd8c6 | -10.41856 | -37.43101 | 2025-03-30 03:49:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b4d51db-29b6-35d1-b844-760709a4f9d4 | -9.50641 | -36.99947 | 2025-03-30 03:49:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1bd7ac5-7db4-30b5-9abe-f4845d87c59d | -16.3276 | -39.56217 | 2025-03-30 03:49:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89ea1a74-189e-3fda-b2b1-6c9ea01d0eb0 | -12.51762 | -39.38996 | 2025-03-30 03:49:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ed817d5a-cfbb-3864-8ed5-360d1724e3db | -12.38534 | -38.89647 | 2025-03-30 03:49:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| a3526a0f-5daf-3971-be96-023c3945ae51 | -16.37201 | -39.26002 | 2025-03-30 03:49:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 91bb1b32-8781-3b20-b423-92dbbacb7d90 | -9.87881 | -37.35952 | 2025-03-30 03:49:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 130f2d93-4aa5-3d26-82e3-d02451168bf9 | -16.68313 | -43.8832 | 2025-03-30 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ab0a38a-ec4e-3701-894d-44bdcb08f1d5 | -17.73092 | -42.7161 | 2025-03-30 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8deb7ab-2cdc-3742-a98f-1d3c4cb92d25 | -15.56996 | -47.85669 | 2025-03-30 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ccee9e-90e4-3ae2-84ee-d909f58d9965 | -22.90815 | -42.74548 | 2025-03-30 03:51:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| febd3fc5-79d5-334a-af60-57c23402d9cf | -17.59774 | -43.19851 | 2025-03-30 03:51:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 455bab6b-c82c-34e5-9de8-71d4a6ea7e1a | -19.96937 | -44.21471 | 2025-03-30 03:51:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 040e7ece-0f43-3b83-9f87-7fd240ad80c6 | -17.4166 | -40.03094 | 2025-03-30 03:51:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc8990fb-1151-3c0c-8798-f563c0838a8b | -17.1726 | -42.8367 | 2025-03-30 03:51:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7c2107f-e586-3fc5-977d-3377daac6c5a | -22.53924 | -48.81202 | 2025-03-30 03:51:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cd52107-e056-3541-925f-78acfb6babc3 | -18.3976 | -44.19267 | 2025-03-30 03:51:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc6463cd-16f9-3e2f-86c0-7b2c35570cb9 | -22.91157 | -42.74614 | 2025-03-30 03:51:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 669262d0-bea3-366c-ae82-0e6b9844db95 | -19.66862 | -42.05457 | 2025-03-30 03:51:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b26c6cf1-1736-3db3-a129-3eac5f12865b | -20.73224 | -42.27686 | 2025-03-30 03:51:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9da8878b-8183-3127-a73f-0b8df3df60ca | -20.17291 | -49.68192 | 2025-03-30 03:51:00 | NOAA-21 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5d06c71-c15b-3b41-a462-1544f260fab4 | -17.66623 | -42.52252 | 2025-03-30 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61e26b78-1184-3fd9-b722-c5fad9560653 | -15.07798 | -48.9449 | 2025-03-30 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce035fb-e2ce-31fa-af57-e4b988595f6e | -17.77926 | -42.80875 | 2025-03-30 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 320b3407-de6a-32bf-9442-f96377414cd9 | -17.6655 | -42.52682 | 2025-03-30 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81284c35-fc0d-345f-a45d-4bab3a7c02be | -17.78288 | -42.80943 | 2025-03-30 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02394cf9-0a67-3d4c-864c-78a2808a16af | -16.68241 | -43.88529 | 2025-03-30 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 742bdba9-0d4b-37f1-a7d5-1fdef14ca558 | -20.17218 | -49.68531 | 2025-03-30 03:51:00 | NOAA-21 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0bbfd2c-251d-3d15-9141-db0fc52f06ed | -23.40416 | -46.55673 | 2025-03-30 03:53:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9bb40dd3-d223-3aeb-a3d0-361e95e0dd19 | -23.59238 | -47.43872 | 2025-03-30 03:53:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7be2dd47-a577-3fdd-a8a1-bd39e39cec46 | -23.64869 | -47.13433 | 2025-03-30 03:53:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a4c594f-5550-3968-91f1-fed1cf996a3c | -5.79441 | -43.62074 | 2025-03-30 04:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92bcb973-c1a8-3ee5-8061-fcfca66c08a4 | -11.32625 | -37.53123 | 2025-03-30 04:14:00 | NPP-375D | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 732cfa25-4919-3a51-9d2b-8ec8c687b979 | -12.37891 | -38.89614 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 225cdc6e-a0b8-31a1-a679-687224f03bd8 | -9.39229 | -40.52651 | 2025-03-30 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e780ccb8-71a0-354c-821e-ca1c1b69e02f | -12.38305 | -38.8967 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a776887a-1e94-3527-b605-a020c8918f22 | -12.38935 | -38.8967 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| bea34552-5c94-3b9c-8a7f-3b3e80f79e93 | -12.38572 | -38.89233 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 29905630-7d27-317c-9780-750e50dfe58e | -11.97481 | -41.37653 | 2025-03-30 04:14:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f894c56-99c5-3260-bed2-974f79c3ea52 | -10.34988 | -38.48261 | 2025-03-30 04:14:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b4af6587-133e-3600-8bc4-b81d4c30e98c | -12.38358 | -38.89294 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b2936347-2fbe-30a7-8830-049aa46f5c63 | -12.38107 | -38.89552 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3a244a3a-aa14-3d58-aced-64cc9e605cee | -10.41644 | -37.42852 | 2025-03-30 04:14:00 | NPP-375D | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb577a45-2e60-3c9f-b172-b5c025442ec6 | -10.39965 | -37.48405 | 2025-03-30 04:14:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e523f3a-5e49-37e7-99fe-94775f22a237 | -12.38521 | -38.89609 | 2025-03-30 04:14:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 97327508-f763-3f29-9778-58d4867c7d1e | -14.1337 | -41.69149 | 2025-03-30 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 676199e5-2741-3d97-aba6-cadf2685594c | -23.33871 | -46.77296 | 2025-03-30 04:17:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa69b818-a941-39d9-93f6-9e37522df708 | -17.11476 | -49.14307 | 2025-03-30 04:17:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
