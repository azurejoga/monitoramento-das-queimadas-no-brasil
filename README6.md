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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64ad3060-8c52-3551-9550-20eaf5310b08 | -9.4383 | -40.3668 | 2025-07-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 243.3 |
| d3e4b8ff-5df7-321a-9024-5a51c97267a2 | -9.4192 | -40.3695 | 2025-07-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 71950274-a1e8-3a00-9810-9ca9a8a48795 | -13.0339 | -45.0561 | 2025-07-16 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5e6e28d6-5deb-3a94-a09b-a76288d19025 | -6.7194 | -44.3231 | 2025-07-16 02:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e8137e8d-3fb5-33d0-925f-487f7d79dd60 | -9.4574 | -40.3641 | 2025-07-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 7d28414a-3aef-364b-8b1f-7adbd525a07f | -13.0146 | -45.0593 | 2025-07-16 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 6b0fa84f-99b7-3d1f-a98a-034540566ae8 | -9.4379 | -40.3917 | 2025-07-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 36e054f3-32de-3371-8320-ac286b1f16d6 | -23.2075 | -52.1036 | 2025-07-16 02:20:00 | GOES-19 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| 2d7d4118-f368-376d-b843-fdae0e38fd12 | -13.015 | -45.036 | 2025-07-16 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 454d88b3-e698-3a6f-b26a-061ea2db7a3f | -9.4383 | -40.3668 | 2025-07-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 366.9 |
| 400aaab0-fd85-3acb-8324-495764c0fd3a | -23.1865 | -52.1082 | 2025-07-16 02:20:00 | GOES-19 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 0d9ad4d7-5656-36c4-8275-33edf1949458 | -9.4192 | -40.3695 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 503.5 |
| 34e41d15-d7f1-3d49-92b4-c24448c212bf | -9.4387 | -40.3419 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 2c77d49c-6170-30ee-8805-a4ce1349ff88 | -13.0146 | -45.0593 | 2025-07-16 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 5a800399-ea31-34e0-a4e6-efc52cb0ca8e | -9.4379 | -40.3917 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 180.9 |
| 9091c6c2-cadd-32a2-a840-bcb557c0e3f3 | -9.4574 | -40.3641 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.0 |
| c0dc57ab-7432-3440-9c2b-aa9d8ef10fa2 | -9.4383 | -40.3668 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 861.9 |
| 7c63d6e1-20c5-3503-81ac-944563fdfbba | -9.4196 | -40.3447 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.8 |
| c2e1285b-3a2e-335f-bfea-03129cfced69 | -9.4188 | -40.3944 | 2025-07-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.3 |
| e5eaab12-e46f-3cda-8f57-7dba9fd5ddeb | -13.015 | -45.036 | 2025-07-16 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 42dc72a8-841f-33f4-a4af-866adf2312c3 | -13.0339 | -45.0561 | 2025-07-16 02:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b9f9f747-bc02-3740-bc5f-7ce2afc260c0 | -9.4192 | -40.3695 | 2025-07-16 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 331ae67a-2992-385a-aeee-b171620dbe4f | -9.4383 | -40.3668 | 2025-07-16 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 2a606a86-4a73-3804-b30f-a2f1b07d52a2 | -13.0146 | -45.0593 | 2025-07-16 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 0e73f8bc-1138-32de-aaef-84a10113b9c0 | -13.0339 | -45.0561 | 2025-07-16 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 39c4dcff-dbfd-3390-acd9-349ccec42e4c | -13.0146 | -45.0593 | 2025-07-16 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 23d6e036-73cb-3884-ba99-c0acec7f6fc8 | -13.0339 | -45.0561 | 2025-07-16 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 09c1b8b5-5323-3de5-951d-dd4e20db10dd | -9.4383 | -40.3668 | 2025-07-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 4ef5779d-5447-3396-b166-d2fdffeb4dab | -9.4383 | -40.3668 | 2025-07-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 8f0b627a-28b5-3053-bedb-d7edbdde3ba5 | -13.0339 | -45.0561 | 2025-07-16 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 44f762d8-ac4e-3e74-9bf1-837d26a27a94 | -13.0146 | -45.0593 | 2025-07-16 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 29d11597-d985-36d0-984a-df3838ee62e8 | -9.4387 | -40.3419 | 2025-07-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 3a9cd601-021f-3032-acf1-e6530d402721 | -13.0146 | -45.0593 | 2025-07-16 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| aaa3cdcf-6f56-3b33-b174-1b21d4d0b67e | -9.4196 | -40.3447 | 2025-07-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 181965c1-30fd-3dc3-a402-2f69c0e8662e | -9.4192 | -40.3695 | 2025-07-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 179.1 |
| 3b59fb6f-fc0d-361e-81ed-a71c0c019d32 | -13.0339 | -45.0561 | 2025-07-16 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 33ded14c-807b-3e52-8804-00bd95ef173b | -9.4379 | -40.3917 | 2025-07-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 1e1905cd-aa20-3704-b25b-bb70f6a8977a | -9.4383 | -40.3668 | 2025-07-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 239.8 |
| 1b24e308-016d-37b5-ac56-0baf6c86b3c8 | -22.5745 | -54.9324 | 2025-07-16 03:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 9d98d57b-f1ad-32f6-8929-ae9d19e57a28 | -9.4574 | -40.3641 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 587930be-a359-351c-8a09-17a08d711d93 | -9.4383 | -40.3668 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 489.4 |
| 4cf3cb35-d614-3e80-9625-9ed951a78a1b | -9.4192 | -40.3695 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 391.2 |
| d8f71861-59c7-3544-bb7f-317b6bfd61f8 | -9.4379 | -40.3917 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.2 |
| c1b8aaea-505f-31b2-b961-7d9b0659ff45 | -13.0146 | -45.0593 | 2025-07-16 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 74940f80-e801-3934-8122-61105610989b | -9.4196 | -40.3447 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 48f7a808-a4c3-3c3f-929a-284b9d45b2d5 | -9.4387 | -40.3419 | 2025-07-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 51ca54e7-7780-3323-baf5-2bad46a82739 | -13.0339 | -45.0561 | 2025-07-16 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fb035344-44da-3c5e-8f32-a0a1d3c6dd8f | -22.5538 | -54.9361 | 2025-07-16 03:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| f3ffec3a-f016-3125-ab72-e3ec588e7b34 | -3.3172 | -40.00557 | 2025-07-16 03:21:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e358d883-51df-3ab4-9257-1b892f98bbb7 | -7.83784 | -44.201 | 2025-07-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 316ae0cc-86c0-3aeb-aecc-77d6b42d87b6 | -9.30989 | -44.84958 | 2025-07-16 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4216eae0-1fde-3c92-b0c9-6f6074003504 | -6.63461 | -44.57922 | 2025-07-16 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0f63597-eb2e-39b8-95ca-66976305dde9 | -5.35793 | -36.89354 | 2025-07-16 03:23:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d7c0eb78-bec9-34c7-b4a0-2283daf27a3b | -8.5044 | -43.3089 | 2025-07-16 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4aafb426-194d-385b-a11c-627d3b73f166 | -9.42876 | -40.35806 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 8a92e2f2-8bb1-3022-b2fe-7c99b687a5ca | -8.51083 | -43.3101 | 2025-07-16 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 37cb172c-0bb1-34a4-9764-7d50593ef489 | -9.30296 | -44.84824 | 2025-07-16 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2f7cc2-2452-32f9-b112-b41b625f7c7f | -5.96383 | -44.17141 | 2025-07-16 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e6f678e-cf78-344d-a5e0-f3ec4d7c79fc | -6.72153 | -44.33458 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eb5b5a32-bcd1-3683-9281-c59791c6dc3a | -5.8771 | -42.40646 | 2025-07-16 03:23:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5983a740-3175-3bf8-89cc-c77f6fafed73 | -9.59081 | -40.3603 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 898fed10-41a3-3f7d-9326-cb6a8d433cd3 | -9.59019 | -40.36358 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de761c6a-fd3a-34a5-8cb1-2826edf24230 | -5.87451 | -42.40691 | 2025-07-16 03:23:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 7af8e165-9900-3f56-a395-e65f26574855 | -6.63918 | -44.57367 | 2025-07-16 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c5e0d23-d54e-3898-9e9e-29f7a4c2ddb1 | -9.42636 | -40.37117 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 61bfc571-5719-3440-afe3-278d783f6095 | -6.71097 | -44.32481 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6ce1c92e-3090-398c-88c1-1af3a4bf808b | -6.7368 | -44.33049 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdbba010-27fd-34dd-9e96-e38072840080 | -5.97077 | -44.17316 | 2025-07-16 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12448d3c-9871-3107-b049-19a80e53a144 | -9.42515 | -40.37775 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13b11545-5bc0-3900-8140-71443449f9fb | -8.51182 | -43.30476 | 2025-07-16 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 29787fe1-69d5-327b-b7f7-61e70ba6c3cc | -6.70878 | -44.32536 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 2ed429fe-450b-31d2-95b8-0029cdc77668 | -6.72375 | -44.33411 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 911fcad1-a542-3f46-951d-63b9d2822ef7 | -5.96877 | -44.17248 | 2025-07-16 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 022f3983-2fcc-363f-84d3-2710aedc94cc | -9.42575 | -40.37446 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 88563104-1d2b-35d9-9f06-b389f4d18f8b | -7.19088 | -43.12746 | 2025-07-16 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f29be91d-cb22-372c-8dfd-29e3d16bb9fd | -9.43042 | -40.37868 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1764ed17-8311-3b49-bced-f438c01d9551 | -9.42169 | -40.36697 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 17142081-5817-32bb-ac10-1fe845a4e241 | -7.83105 | -44.19949 | 2025-07-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f26d00f-0326-3de5-ae8c-80a190d684b0 | -5.87615 | -42.41166 | 2025-07-16 03:23:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d5ae21c4-6b79-3d98-89d3-5deb4b54fdd7 | -6.63215 | -44.57196 | 2025-07-16 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a618b078-0fde-33cb-98a2-fa8f406efc59 | -7.83899 | -44.19505 | 2025-07-16 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c73625b-117b-3d31-a0b8-3cf6a994928a | -8.50256 | -36.58705 | 2025-07-16 03:23:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e21ab80f-d5bf-38c3-a024-01e56b4b5356 | -6.39204 | -42.45334 | 2025-07-16 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8e06f494-8fae-3ba4-9566-a17102a25c03 | -7.19943 | -43.11761 | 2025-07-16 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a342e799-b265-30f6-b056-b8b091248830 | -6.30645 | -38.9122 | 2025-07-16 03:23:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1d388ca-dbf1-3b62-9149-d47481c487e9 | -7.96221 | -37.18814 | 2025-07-16 03:23:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a44d7768-875a-3741-8209-7ebfed6cbcf6 | -6.72855 | -44.33579 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f30e60b-b640-32fa-9e73-538003dcd4ad | -9.43402 | -40.359 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| bf9e2f7d-9d43-3080-81c9-7eec2c286a15 | -6.72249 | -44.34096 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60da3caa-df7a-3a8e-901a-43c72decbce4 | -6.71451 | -44.33333 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2cd6cf1e-fae6-3eea-aa0e-aa752c58223c | -9.43808 | -40.3665 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41f5a064-c9a1-380c-b83f-bb24406be988 | -7.05849 | -38.85777 | 2025-07-16 03:23:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ff24ad5-6d50-3dff-b15d-727497ab70bf | -9.41765 | -40.35946 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb106831-3bb5-3f73-ade6-35145c498a57 | -8.33183 | -38.08846 | 2025-07-16 03:23:00 | NOAA-21 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1085f5f1-2c73-350e-b472-12462d33f1ba | -6.70749 | -44.33209 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dc37ba79-8885-3056-86b1-d93dc0cfdec2 | -9.43222 | -40.36882 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 934.0 |
| 151bd76f-9e71-3d7b-9a93-4d4061cdf713 | -9.43102 | -40.37539 | 2025-07-16 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| bd9fc7b6-0229-33f5-b0cf-5d270c9ada36 | -8.50193 | -36.59083 | 2025-07-16 03:23:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9abcbd01-107f-36ab-adf1-06112b604ab8 | -6.71674 | -44.33283 | 2025-07-16 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 729c38c2-5c00-36d2-83d7-17cb8ee91e7e | -5.36239 | -36.89425 | 2025-07-16 03:23:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README7.md)
