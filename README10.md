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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9f80de1-9044-3dd8-9f9f-ca769fb7e383 | -5.3646 | -56.0249 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4298bb5f-df96-37c4-bad7-90cf8fade3d3 | -5.9197 | -47.8927 | 2026-09-05 03:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4770536d-1304-32aa-971d-339f4539be1d | -5.346 | -56.0454 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5216217c-4a7b-3abc-8e6f-008c5da43ea0 | -4.6669 | -55.635 | 2026-09-05 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f80b4a94-dd0f-30d8-806f-7ff8df6a6d45 | -5.3277 | -56.0263 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e7b782d1-913d-3c25-910e-2e4aeea7505f | -17.1074 | -56.851 | 2026-09-05 03:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 5c608999-eeeb-33c5-a6cc-87f28cc42885 | -6.6515 | -59.9258 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 972e62af-badc-37f8-b37d-73e06f499f59 | -5.6566 | -60.2284 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ff6889dc-aa3d-3fa4-a373-2ecb2d3714e2 | -17.1078 | -56.8304 | 2026-09-05 03:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 30c876ca-4371-3e00-b578-57974f36d833 | -5.3462 | -56.0256 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 61bcf5f7-abdd-360f-b3cc-d3b7820cac52 | -5.3463 | -56.0059 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a6dbca2b-191a-3b37-a7df-0c92cd7764e4 | -6.6697 | -59.9635 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 3764f591-b87f-3c53-9eab-2691a1999ca9 | -3.71975 | -39.62658 | 2026-09-05 03:21:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 12de731f-82d0-3050-a636-0538858d98c5 | -3.71962 | -39.62663 | 2026-09-05 03:21:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9db16308-e44d-308b-a637-2e5a6a60a01a | -3.05049 | -39.93206 | 2026-09-05 03:21:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 74f59742-daa1-3928-9a0d-d83f4187c218 | -4.1782 | -42.44922 | 2026-09-05 03:23:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9e459398-ea71-314b-a790-672e7a87a129 | -5.41825 | -43.26064 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 4918ef12-a220-3702-a4ed-fbe272a18d10 | -7.20426 | -43.60235 | 2026-09-05 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3a5ca125-c894-30e4-8fcf-2df0c8fc58e1 | -4.53889 | -38.45111 | 2026-09-05 03:23:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b25f570-ddea-3011-af5e-f7790955f4d4 | -4.1792 | -42.44368 | 2026-09-05 03:23:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24a22006-1eef-34da-a31f-f93188b16354 | -10.15999 | -36.21873 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 1ca4588e-5e40-346d-8bff-59cfedc8549e | -5.41153 | -43.25939 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9ceadf86-3624-3333-9d3e-63634d1a9d53 | -10.15604 | -36.21804 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| cf105310-d826-36c2-850d-de6ad3bd1fe9 | -6.36998 | -43.596 | 2026-09-05 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12d97a6f-8b8f-3311-a62f-057cb93df774 | -10.15666 | -36.22028 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2d58a14c-d3d8-3bd8-88d8-0bcb54bfa471 | -4.18008 | -42.4424 | 2026-09-05 03:23:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7645305a-f65a-37b7-89d2-c7c0fc8b87ef | -3.44193 | -43.26532 | 2026-09-05 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e45a44e4-24c7-3f18-8ebe-df4fdf53f175 | -4.26706 | -38.01311 | 2026-09-05 03:23:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 2828be98-85cc-3de1-b0b2-c0e58712fb54 | -5.41381 | -43.26125 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 3026bdb3-3fc4-31c2-814d-8478423beb60 | -7.2052 | -36.6208 | 2026-09-05 03:23:00 | NOAA-21 | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e96facd-28df-347c-8664-d9d253aa6656 | -6.12683 | -43.74979 | 2026-09-05 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f2fbe1b-5ba7-303c-960d-69f810894eb8 | -5.42207 | -36.76406 | 2026-09-05 03:23:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f893bbf9-189a-3f6a-9883-c98a6515c117 | -8.64197 | -38.14774 | 2026-09-05 03:23:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d7644434-c9e9-3cdd-ab93-c23533e02855 | -5.41713 | -43.2669 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ada583ef-d4e5-3cdc-b39a-a43b4d3e6a64 | -4.26615 | -38.0186 | 2026-09-05 03:23:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 05cd3e37-f508-3852-82d7-7a59546fe264 | -6.12568 | -43.75621 | 2026-09-05 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce153048-65ff-3683-a856-66f19215d707 | -10.15752 | -36.21515 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| bd4f45d0-c81e-302f-8b68-1918ec70971c | -5.20849 | -39.41132 | 2026-09-05 03:23:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca9ce6b2-4b4c-385f-bed8-1a7f8b3084d1 | -3.44027 | -43.27162 | 2026-09-05 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0929788f-f956-3105-9d4d-a74009183f5e | -7.20932 | -43.59286 | 2026-09-05 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5bffb9c6-04e1-37a5-ad73-602225b3dcd2 | -5.41491 | -43.25529 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6cedd558-7a7d-317b-aa58-fe56c1eae744 | -7.20822 | -43.59888 | 2026-09-05 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 382b6fc7-46b1-3e90-b42f-c6c35dbace09 | -10.15693 | -36.21292 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 54b954fa-0560-3ae7-89dc-1b8338c5e3f6 | -3.44083 | -43.27185 | 2026-09-05 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2f1c91f-06c3-3f86-973a-9c3194fc5f96 | -5.4205 | -43.26265 | 2026-09-05 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 85992fda-59c6-3c65-b05a-f4b2eca879b5 | -7.3983 | -36.99997 | 2026-09-05 03:23:00 | NOAA-21 | LIVRAMENTO | PARAÍBA | Brasil | 2508505 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea4abcfa-a25d-3ee4-bcaa-7237e9a81db8 | -3.44141 | -43.26512 | 2026-09-05 03:23:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 191a5977-e4d7-3a9b-a078-d7f8d754f9ff | -10.16088 | -36.21363 | 2026-09-05 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 202aac93-0224-38c6-9443-c3c2b9f562b9 | -5.42134 | -36.76843 | 2026-09-05 03:23:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec64b1fa-3550-3245-9636-658050fa5d09 | -6.12678 | -43.75378 | 2026-09-05 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 076486df-874b-368e-8d3f-8308a6a2f33e | -8.31599 | -37.26945 | 2026-09-05 03:23:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 53ce6ec6-7271-3ccb-a381-2969dc084642 | -4.17913 | -42.44794 | 2026-09-05 03:23:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 502525a5-68bc-3468-b14f-3a2da209591d | -8.64656 | -38.14856 | 2026-09-05 03:23:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eeee21fd-9ee5-319b-80e1-ef23285cdf2a | -7.20541 | -43.59631 | 2026-09-05 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f69008ee-6161-3808-819d-38dff873b382 | -13.754 | -42.09572 | 2026-09-05 03:25:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b18dadd-0864-348f-995c-a11dab0717d7 | -12.92647 | -42.43331 | 2026-09-05 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 258c3805-5354-3d39-a0f3-7c6fd3325cad | -12.92162 | -42.42826 | 2026-09-05 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8a45440-b480-3530-82cc-61f6aaf4bd29 | -15.37976 | -42.11782 | 2026-09-05 03:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f09cd7b4-ce51-39cf-b9ab-39e880eb8088 | -13.41748 | -41.88894 | 2026-09-05 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c51772f-653d-3aa4-8d3b-5dddf6f99db0 | -9.78961 | -42.00087 | 2026-09-05 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a83fd55-2a60-31f6-a347-5096c7cea27d | -12.92425 | -42.43156 | 2026-09-05 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b1139ac4-78cc-33bd-8eb9-8523f9cdd835 | -15.82571 | -42.03959 | 2026-09-05 03:25:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e393bb97-6dd8-3199-ac24-7b7c66f95695 | -13.4169 | -41.89192 | 2026-09-05 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ca5cd15-e440-3529-b37c-f05236584aa6 | -12.92348 | -42.4355 | 2026-09-05 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3c7967d8-3acc-3d61-9b1b-3e326b358a9c | -12.92082 | -42.43222 | 2026-09-05 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5c50a65-3a74-3589-86e7-a74e05f5dc31 | -17.7929 | -39.70538 | 2026-09-05 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 12547e47-d27d-373e-aefd-8c06be3e919f | -13.41812 | -41.88568 | 2026-09-05 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b57d325-c81b-374d-b7a4-f7ea3f892f18 | -17.79399 | -39.70528 | 2026-09-05 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 460b3fcf-d59d-3587-b29e-bcb978bfcd2b | -13.75277 | -42.09753 | 2026-09-05 03:25:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 566a1365-c12a-3818-b2c4-0bd80d35a95c | -9.78379 | -41.99984 | 2026-09-05 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 03f58157-0268-34da-8329-d2779feb1cb9 | -19.71592 | -40.07343 | 2026-09-05 03:28:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e15193ad-609e-3156-b231-317f7e281d66 | -19.23376 | -46.72858 | 2026-09-05 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5f80db3-8a0a-33a4-9f61-2c1efc2422ed | -21.46082 | -48.68161 | 2026-09-05 03:28:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f548c01-3223-31ca-89af-4d7857e13e58 | -21.53906 | -43.19645 | 2026-09-05 03:28:00 | NOAA-21 | GOIANÁ | MINAS GERAIS | Brasil | 3127388 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ea0283a-0a2f-398f-9d3b-b9cedcae4805 | -20.99186 | -45.80598 | 2026-09-05 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a43b8a01-26a7-3fe6-aac1-ccba9ab80ac0 | -17.3005 | -43.3499 | 2026-09-05 03:28:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70936019-9c34-391f-9a7c-31ca1e09f8b0 | -19.75305 | -46.6898 | 2026-09-05 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fb83acd-8783-3567-a4a4-29cc00a1f99f | -20.34049 | -47.59716 | 2026-09-05 03:28:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7ddcc73-f4d3-30ab-8558-f8b48da1771a | -21.1113 | -46.28084 | 2026-09-05 03:28:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c2730c89-010f-34fa-9342-52ea9df21986 | -21.55104 | -44.05487 | 2026-09-05 03:28:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c761ed0-2a6d-3d83-9b14-5239a1f7db0a | -19.46135 | -40.28053 | 2026-09-05 03:28:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6a6d232d-0f06-3afb-b0ff-65b0148789d1 | -19.7503 | -46.70153 | 2026-09-05 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c87f3b2-d46b-3817-bca7-ddb11aa622d9 | -19.23316 | -46.73333 | 2026-09-05 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f908773c-731c-3770-9847-d476a9238647 | -18.79191 | -41.59345 | 2026-09-05 03:28:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 82c566cc-daa5-32d5-92ba-c0b60df74a1b | -21.46255 | -48.67466 | 2026-09-05 03:28:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 803ca102-107b-3209-8ab3-ca4ca6c23d53 | -20.14663 | -46.31836 | 2026-09-05 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8c3d827-838c-3beb-9d94-3fdfd80c3751 | -17.29977 | -43.34924 | 2026-09-05 03:28:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c0587b3-2f2b-3aae-a883-53d6984b31ed | -20.25807 | -46.33639 | 2026-09-05 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83df94a7-0e6c-34eb-b028-3ae1a66d949d | -18.17114 | -42.94264 | 2026-09-05 03:28:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79891995-2eb2-3ff8-b61e-2684f42bd068 | -20.98597 | -45.80434 | 2026-09-05 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5b2a2f3-e4ed-35cf-ac23-f45423c3baae | -21.48658 | -44.15776 | 2026-09-05 03:28:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ab3a2a2f-a0e4-33c6-b686-257bb21d3794 | -18.82775 | -47.99394 | 2026-09-05 03:28:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cdcf414f-2b95-361a-acd7-12c679921999 | -20.98881 | -45.80796 | 2026-09-05 03:28:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9849ee4c-967c-32fa-96d4-8146370d315f | -17.3014 | -43.34552 | 2026-09-05 03:28:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78620bfc-08a8-30aa-a7d7-5cac06893156 | -21.39036 | -45.50675 | 2026-09-05 03:28:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c725500a-ec41-3598-a1ce-2130091ab301 | -19.23244 | -46.73414 | 2026-09-05 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9699e6c1-dbf3-3038-bfb7-a70bc47abbb3 | -19.25632 | -46.86459 | 2026-09-05 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bff792e-5f33-39e3-a158-a9264b09914d | -20.82734 | -46.31559 | 2026-09-05 03:28:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 618fb1d3-c6e0-33cd-91c5-ad27665fbd4e | -19.71675 | -40.06915 | 2026-09-05 03:28:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43214ebc-1703-3cff-8597-2a6c060a72dd | -19.75448 | -46.68369 | 2026-09-05 03:28:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
