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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97de64b0-f77d-372c-96aa-b4bdc2b68b6d | -11.73216 | -41.27342 | 2024-11-29 04:06:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dbb41ef6-8cb0-307c-b92e-017f155e9dc6 | -7.28282 | -39.10106 | 2024-11-29 04:06:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 047259e8-af43-3ab5-b112-256f5d4cd454 | -8.12547 | -47.98607 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 169648a8-02aa-35f2-b6a7-279807e80b18 | -10.20124 | -42.47993 | 2024-11-29 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b7234ce-a8d3-3c49-a8c0-887f7f616f24 | -8.12473 | -47.99024 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d3fde8e-a514-3567-9e1a-8b2c9d5eb271 | -7.01935 | -39.37116 | 2024-11-29 04:06:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a24d3ec-056e-300e-9448-8fc7a5db93f7 | -12.16563 | -39.85649 | 2024-11-29 04:06:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d4afedd-4b1c-345d-a6c6-2f9df2ab6d3e | -7.0155 | -49.84468 | 2024-11-29 04:06:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e015e15-4339-370a-a936-82d7ac5f3baa | -8.28292 | -48.03848 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d1994f1-d60b-3c75-9690-2c68ebc22b54 | -6.93587 | -43.51661 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3760237b-7e1f-3112-bf3d-bf715dfad3a5 | -7.3969 | -42.76724 | 2024-11-29 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8370e864-5942-3694-82b0-9a9c3e102f25 | -7.71859 | -35.15612 | 2024-11-29 04:06:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| c25d560a-4a9d-3ad5-af04-f1e325bece5c | -6.8246 | -46.77127 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b54cb19-590e-3458-b2cd-9d2a4876fccc | -5.87591 | -47.31955 | 2024-11-29 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 445d2eb7-046c-3e6a-a7a6-33a18e1ce01a | -6.4761 | -42.81458 | 2024-11-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 47263db3-de01-3f9e-a839-4549167c5650 | -9.72644 | -37.06086 | 2024-11-29 04:06:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31428fef-0446-3a0a-829b-b304a46474b4 | -6.1937 | -44.42517 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0373db6-cf2b-310b-9bb2-62534b477e88 | -6.93025 | -43.50801 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594f8891-89b1-38ce-b8d8-88ba598a6366 | -6.9399 | -43.51343 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fb856c0-61cc-3844-9a7a-4dd1541c1283 | -6.75009 | -46.52324 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e58c5e44-b6eb-3168-af58-ec6fbecb8b12 | -10.41864 | -40.46757 | 2024-11-29 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0f328b11-3267-342c-afb7-14915ec3005c | -7.22052 | -39.05586 | 2024-11-29 04:06:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4747124e-97cc-3784-83f9-162c564d2c4f | -12.05059 | -39.06947 | 2024-11-29 04:06:00 | NOAA-20 | TANQUINHO | BAHIA | Brasil | 2931103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e4dc615-b897-3dea-ba7e-81245bc8f532 | -6.93709 | -43.50916 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1deef9ca-de04-3911-ac19-665b0ee5ee48 | -9.45332 | -47.32611 | 2024-11-29 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79a76ba-9039-3d29-9dd6-098d1b3ac1ec | -8.12382 | -47.98736 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8b4ac50-9e27-3d44-a970-67a65bce8974 | -6.7541 | -46.52392 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68b0827e-a5dd-3eac-939e-897b43df00ec | -12.12164 | -39.40917 | 2024-11-29 04:06:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67160da9-27e2-361b-b3b8-3a7831f95db0 | -11.40469 | -45.09104 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb1d9fa5-eac0-3539-a916-ab1ee32a6b5f | -8.12833 | -47.99516 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d1cc029a-0998-3390-8db1-b95a281ba914 | -9.55976 | -35.84161 | 2024-11-29 04:06:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 54136104-cc60-34e7-a184-c188174c61f3 | -7.44773 | -39.84098 | 2024-11-29 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a6f447c-55c8-360b-9057-0a9665058a47 | -7.82711 | -48.19289 | 2024-11-29 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17ae2b9-9bbe-3dd0-8300-d9c5482fecfd | -7.83153 | -48.19361 | 2024-11-29 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 966d899b-9f2f-3fb9-b24c-95daf43f63e4 | -8.1298 | -47.98681 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c9c3461-b2b1-377f-b32c-78a8fd7ea54a | -9.1102 | -43.10386 | 2024-11-29 04:06:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 821abf68-98ae-325e-a190-fa3da0cc6eb3 | -7.21994 | -39.05969 | 2024-11-29 04:06:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5fa79667-8805-3c32-8f97-057ba88d40ca | -9.81435 | -48.17051 | 2024-11-29 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0835a30b-0d8a-3aac-a097-2290f1dc6bfc | -6.19728 | -44.42581 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcdbaf23-aab1-3565-a125-c49947e032dd | -8.12884 | -47.98396 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1a53438-f905-3f28-bd0b-006baa6eeb67 | -11.39421 | -45.08923 | 2024-11-29 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de28f009-82c3-3179-867d-488381c8d941 | -9.90808 | -48.10363 | 2024-11-29 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d0e070e-91ee-3e05-9152-48ad04cd60d8 | -6.48802 | -42.81663 | 2024-11-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 39c801c6-dce6-3a94-9128-488568bd0ab9 | -6.83868 | -40.5112 | 2024-11-29 04:06:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4eb2ee83-f7d5-3990-9b0d-68a8ed18a330 | -10.09761 | -44.35272 | 2024-11-29 04:06:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c00d5066-4db1-3bc6-a153-a79cadb09acf | -7.68988 | -42.97403 | 2024-11-29 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49d23fd0-155d-3080-920c-d1dd47ac4030 | -6.2583 | -43.89055 | 2024-11-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b552abdd-5d79-35a6-8aaa-ce8c5825b0b0 | -5.98774 | -45.74334 | 2024-11-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbf566df-270c-3eda-bed2-6a156090b884 | -9.10353 | -43.10273 | 2024-11-29 04:06:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5a1e1dc-4786-3ba0-a247-bc9f2d2b9de5 | -10.66011 | -36.81851 | 2024-11-29 04:06:00 | NOAA-20 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c6ca518c-6e68-38c1-9702-d547eb24bac5 | -6.11359 | -44.92053 | 2024-11-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6d19f19-36d0-3e45-9944-121bea35be13 | -8.13266 | -47.9959 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 825f89cf-a459-3639-bff5-c4352ec9591c | -6.1406 | -44.73067 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd93ffbc-e215-329b-9ec4-f5a791f7ca83 | -8.12906 | -47.99098 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34dab3b7-77d1-3a97-a31f-acb76269e42d | -7.49111 | -41.65863 | 2024-11-29 04:06:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7d6caf5-0bc7-3ed9-b923-6fb463c9071f | -7.71922 | -35.1517 | 2024-11-29 04:06:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| 7ad3fd69-ba06-3ebe-8ad8-efb487d65b6d | -10.18525 | -42.47378 | 2024-11-29 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 65ce5f6e-d401-3481-a4aa-df45e7480ac3 | -8.28436 | -48.03012 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0828570-10e4-31e3-a685-310635f61ff2 | -6.80022 | -46.47047 | 2024-11-29 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac4ced5e-79bd-3fdd-b46f-bb9dcbb846eb | -6.99993 | -39.31345 | 2024-11-29 04:06:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b78bdbb4-0662-3028-ac4f-330a73b7e929 | -6.51842 | -46.85584 | 2024-11-29 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25e7dcb1-25f0-3210-9caf-a207c59a6dbc | -7.44714 | -39.84481 | 2024-11-29 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3fc11b2a-2a64-3606-b79a-d0fa55a3c88d | -11.40403 | -45.09499 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 103293c0-d767-3579-a6c6-98b1e5922328 | -12.67246 | -42.33376 | 2024-11-29 04:06:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f1d1a14-fa20-3c98-9ee2-515da73be849 | -6.13695 | -44.73009 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3086df8-47e5-3be6-b159-23938bdde50c | -6.47273 | -42.81406 | 2024-11-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1a6532e-085c-36d7-83fa-50781c473146 | -9.90453 | -48.09898 | 2024-11-29 04:06:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1074a64a-32de-37b0-85fc-397e16470323 | -7.69266 | -42.97813 | 2024-11-29 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f5c4ed0-8905-3bdb-a92f-a688386e0abb | -6.92682 | -43.50745 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f974e544-7efb-39fb-9490-f10ce741df41 | -8.37175 | -47.99725 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6856163-c85d-3f9c-a167-b747c10aa0c9 | -11.39705 | -45.09378 | 2024-11-29 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e86b36c-3fdd-36b6-a9f0-a41b0891ee14 | -6.00085 | -45.76051 | 2024-11-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9689774c-319c-31a6-b70a-193d050522c0 | -6.18946 | -44.42865 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2913361-7f49-36b7-9624-e43fd4c9a968 | -9.55537 | -35.84101 | 2024-11-29 04:06:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 903e7f2e-5d11-36ed-bc08-4ab19a4f9cb6 | -8.27931 | -48.03353 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14d30a7d-2aef-3256-b0fb-df9dc276eca1 | -10.09074 | -44.35157 | 2024-11-29 04:06:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cc6833e-25b4-3cb9-87f2-5d2b57ec318a | -7.07281 | -40.22658 | 2024-11-29 04:06:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5abcd856-3480-334b-8f9b-7cd2eb663ee3 | -6.19304 | -44.42928 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8a374a3-2221-3809-8648-b23e375d53d0 | -9.55157 | -35.83623 | 2024-11-29 04:06:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a264149-f9af-3e91-82f8-b9855e48e47f | -6.60584 | -42.35911 | 2024-11-29 04:06:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 701c67cd-c103-3034-9813-9a8ec3c62593 | -9.10686 | -43.10329 | 2024-11-29 04:06:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 979e63e6-eacb-321a-b32b-906f727c9a31 | -8.12452 | -47.98321 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd473da6-b350-33e1-8649-e3550aa97d81 | -7.58038 | -47.11876 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3a53d53-8be2-3910-80b6-40b0ea2c6adf | -10.19106 | -36.34161 | 2024-11-29 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 019e6c9e-0e6e-373e-9673-cb275a10d712 | -7.02188 | -39.37132 | 2024-11-29 04:06:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3c0e46c-a9d5-3e38-a30a-22ae4dcbff2d | -8.28364 | -48.03429 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b48fcf43-4d8f-30de-a586-ebc049e2817f | -7.32937 | -39.10124 | 2024-11-29 04:06:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 327988cf-5b33-33e0-ba16-374f5e841530 | -6.99934 | -39.31725 | 2024-11-29 04:06:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 63a9e1f3-e13b-30f9-a4b9-b4f3911fb75e | -6.92401 | -43.50319 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd68611f-ccaf-3a1d-9ffb-5dd9b4474595 | -11.3977 | -45.08984 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d11bd21-c9b0-3738-9258-465e489f4cc7 | -17.76026 | -42.223 | 2024-11-29 04:08:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7dcc203b-05ee-32bb-90d8-414e89e33513 | -19.7605 | -43.65177 | 2024-11-29 04:08:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aa39ec3-8ed4-3451-96c4-c923b8f219e4 | -17.58366 | -42.75519 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6807e864-c709-3292-bb8e-7443d6726d5f | -19.6689 | -45.88395 | 2024-11-29 04:08:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf0d9044-845c-39dc-8122-bd2b2eedb4db | -15.34147 | -42.8286 | 2024-11-29 04:08:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bc60e1c-7bdc-3138-b2df-f507d2af4ce7 | -17.62563 | -42.75068 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d9d1c6-2501-3071-b61e-372b1c5401c5 | -18.67333 | -47.17007 | 2024-11-29 04:08:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfe92891-abb1-3ef4-bb7a-9846559cdf3b | -19.96905 | -44.21574 | 2024-11-29 04:08:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0effc4a5-bf56-331c-9552-e5180da6c7fa | -16.92094 | -43.60719 | 2024-11-29 04:08:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450bf27c-039c-33b9-93e8-c9eefbecbb02 | -17.58311 | -42.75891 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |


[Clique aqui para ver as próximas entradas](README37.md)
