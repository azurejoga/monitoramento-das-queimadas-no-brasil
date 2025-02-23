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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edc42061-74af-35c1-89c1-36e340793943 | -10.48247 | -42.42004 | 2025-02-23 03:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9e2b990-08d8-3f0a-a2a0-0b014f38c088 | -10.47918 | -42.41993 | 2025-02-23 03:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07015bb0-444b-3847-961f-517ee0a65467 | -16.34746 | -43.69567 | 2025-02-23 03:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f915f484-1ec7-3e7a-8699-c3e1f7db595a | -12.84818 | -43.82891 | 2025-02-23 03:32:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55d12d15-e645-3b3c-afc9-27aff0cef568 | -15.04258 | -45.62105 | 2025-02-23 03:32:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7115713c-8e20-3a08-9fd5-065a7f82f45e | -11.89157 | -38.2313 | 2025-02-23 03:32:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cd215a76-9396-3de9-bb26-ddcdab5af1fe | -11.88966 | -38.22834 | 2025-02-23 03:32:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef984116-7bac-3de1-9b72-0844aeb7778b | -15.03749 | -45.61528 | 2025-02-23 03:32:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aac1cb73-6a16-3e0c-aa30-248ad50170ce | -10.47984 | -42.41651 | 2025-02-23 03:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac571bef-5f22-3cd6-864d-253ebdd10326 | -15.04357 | -45.61641 | 2025-02-23 03:32:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18d19197-6dfd-3d23-9e2c-182426cab10f | -10.69509 | -37.05069 | 2025-02-23 03:32:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f9bc08f7-b641-34df-8055-45230546b50c | -13.62604 | -44.4315 | 2025-02-23 03:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef733389-4341-3d02-ae21-ace10ffdc612 | -10.4831 | -42.41661 | 2025-02-23 03:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d1af77a1-55ba-3336-bc19-afe361fb6747 | -12.84254 | -43.82775 | 2025-02-23 03:32:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06be36d8-d671-30bf-9847-ea15eab51010 | -16.68272 | -43.88119 | 2025-02-23 03:34:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4feb07d-c67c-35a6-9519-32916c610055 | -20.06787 | -40.75238 | 2025-02-23 03:34:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36f03f32-4edf-31d0-a30d-55be28f7e803 | -16.64714 | -49.36452 | 2025-02-23 03:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9de5a8a9-77e4-39d8-86e2-578f59060338 | -20.06715 | -40.75619 | 2025-02-23 03:34:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 137ea8bd-4c99-3a0d-ba90-c356b21b35dc | -20.3164 | -46.48645 | 2025-02-23 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe8d0b20-0b79-39a2-ace8-355929dc6f7c | -18.04058 | -39.92466 | 2025-02-23 03:34:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 799b4082-3100-3b85-b8e8-e1c6a2f93654 | -17.77875 | -42.81039 | 2025-02-23 03:34:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba20696f-8c82-3144-8a6d-7b5227eb0b56 | -22.75383 | -43.26844 | 2025-02-23 03:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 023aa94e-9ffb-3dc3-990a-115daed93bbb | -19.82246 | -40.0996 | 2025-02-23 03:34:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a0aa039c-294e-3736-a20b-26744ea5522c | -16.64539 | -49.37185 | 2025-02-23 03:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0d9b113-ae31-3b4f-9f4d-90570c7ec279 | -20.31551 | -46.49034 | 2025-02-23 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00a744dc-022a-322c-9958-43ab4781c60a | -16.65341 | -49.36949 | 2025-02-23 03:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b57486d-a936-3be6-b41e-8c4666e34d5a | -20.31459 | -46.49433 | 2025-02-23 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b51fb240-7e16-3430-a0b1-0205cd27d829 | -16.64633 | -49.36713 | 2025-02-23 03:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9132ad96-219a-3715-a75d-ee9cd1da58bc | -20.31698 | -46.4877 | 2025-02-23 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c4845f-a708-3b13-bb17-b2645455ad89 | -20.3161 | -46.49163 | 2025-02-23 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfc776d9-f6c5-37d2-90ce-de1a09eafb0d | -22.8362 | -42.53925 | 2025-02-23 03:34:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cdbff6dc-1b3c-3878-98e9-c05ecbae3509 | -22.67633 | -42.85857 | 2025-02-23 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fe42e8a-b5cb-3591-8913-adfec739027a | -20.89006 | -46.1615 | 2025-02-23 03:34:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a61e663-ef74-3bcd-b098-25bfaae29e8b | -22.75367 | -43.2698 | 2025-02-23 03:34:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 715efd67-9792-326c-ab3d-70220ffeeca4 | -20.89592 | -46.16156 | 2025-02-23 03:34:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c2e52f20-1099-3b4e-be01-70e5e9654aa9 | -17.67793 | -42.74552 | 2025-02-23 03:34:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70fcdab7-5ea0-3ae0-b0fa-5305d3bc8ebb | -11.89128 | -38.22884 | 2025-02-23 03:53:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9abe55c8-96f4-3f12-bfe9-9b55091f6c26 | -12.8467 | -43.82486 | 2025-02-23 03:53:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ce385d9-6d20-3bbe-abed-ee1537415168 | -12.84591 | -43.82947 | 2025-02-23 03:53:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 795a02ba-4b5e-383f-9647-676398c2c27b | -11.88792 | -38.22829 | 2025-02-23 03:53:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18e37bd7-74f1-39a9-a815-3fc3c412615a | -4.16741 | -42.02859 | 2025-02-23 03:53:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0d57b931-ab23-3015-b28b-67ad5dc5fb67 | -6.95381 | -43.0046 | 2025-02-23 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d46f5e9c-78c2-38ef-a00b-293978082133 | -4.16811 | -42.03131 | 2025-02-23 03:53:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 379a42cc-a2b3-3967-85cd-c4faaa0ae14e | -11.36145 | -40.05898 | 2025-02-23 03:53:00 | NOAA-20 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cdc6809b-811f-3e56-8992-bc3f5cc1b7ca | -10.60538 | -45.10842 | 2025-02-23 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9b23e185-6d6b-3a08-b7fb-b8f7ae66d7f9 | -11.84522 | -44.7244 | 2025-02-23 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89756f7c-f0e1-32bc-ad1a-4cb0cef2d2d6 | -6.06821 | -44.4523 | 2025-02-23 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86a1e00d-be55-304f-be05-37ab17a03696 | -6.9577 | -43.00523 | 2025-02-23 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 492100b7-a96b-32a9-a8f5-8751627f9e3b | -10.6941 | -37.05047 | 2025-02-23 03:53:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cda4a1e2-5973-3aa3-b248-baed0450307b | -4.17122 | -42.02922 | 2025-02-23 03:53:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 95f74c87-1ca5-3593-ac48-f94baac592af | -5.19845 | -39.12963 | 2025-02-23 03:53:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30c86ccf-2057-329d-bf02-2f3244e57a02 | -12.01875 | -40.62101 | 2025-02-23 03:53:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ea97cc4-f6f1-33f1-9738-154ece5e4bb1 | -12.55583 | -44.73222 | 2025-02-23 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ede08818-b510-3d11-8757-2b6232ed9979 | -12.51066 | -45.49814 | 2025-02-23 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceca7751-4826-3417-9a09-cc02931c7080 | -10.60573 | -45.10747 | 2025-02-23 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 85075a24-ecff-337b-9874-8cf93269ff04 | -10.60993 | -45.10828 | 2025-02-23 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4925758e-3460-383d-9ef7-11c30bdfa3ff | -10.60643 | -45.1036 | 2025-02-23 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 014ea3ec-2268-335c-a68d-91d9d171b57e | -11.89073 | -38.23249 | 2025-02-23 03:53:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea54aad2-d38c-32da-99e7-4b84830464bf | -12.85045 | -43.82553 | 2025-02-23 03:53:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e5a09be-995e-36be-ae69-0ae9bac9801e | -12.86089 | -38.36649 | 2025-02-23 03:53:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b4a1018-75a3-3496-a4db-c42cac04eaa3 | -12.56254 | -44.74065 | 2025-02-23 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04401132-00f7-38f1-9785-931532c64700 | -10.48028 | -42.42183 | 2025-02-23 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d3fd407f-5d23-30aa-89c8-85216731c263 | -12.84216 | -43.8288 | 2025-02-23 03:53:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b871483-c593-3ba2-a210-d29f02951167 | -12.01817 | -40.62459 | 2025-02-23 03:53:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 779881bb-380f-33dc-8a61-c22f3e0bfb2c | -12.50159 | -45.50055 | 2025-02-23 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0efdb0a-72cf-3a1c-9b90-ca2d1a9b5058 | -6.94992 | -43.00397 | 2025-02-23 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc56e3bc-f659-3c7d-bca0-62b20b47ca1e | -11.89409 | -38.23306 | 2025-02-23 03:53:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 830323f9-946e-3511-aa4e-e3b167533928 | -10.60605 | -45.10453 | 2025-02-23 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f0e54bc2-9e94-3379-b8ca-9f8ec1aa656f | -6.07254 | -44.45308 | 2025-02-23 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ae90180-98d6-350d-8256-3fb8258d22d3 | -10.48098 | -42.41765 | 2025-02-23 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 74fc0634-22a2-346e-bb4f-8152a0dfdd5f | -17.09314 | -43.80498 | 2025-02-23 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26dbc61-635d-3957-be80-9f4ef4cd6be7 | -20.04921 | -41.23005 | 2025-02-23 03:55:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a964ebe-e6eb-3db1-ac19-f26b40097f84 | -17.77843 | -42.80726 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2143e221-0d90-3c5b-a589-dec728c5fcff | -15.04696 | -45.62052 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ef77c66-7f46-3413-a009-d614913c46db | -19.9678 | -44.21592 | 2025-02-23 03:55:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca7b6184-d3f2-366c-8d6e-b66a08a372a0 | -8.2028 | -39.36462 | 2025-02-23 03:55:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bad2237a-b898-3ef7-9e7d-c0efa469cbe2 | -7.86793 | -44.18474 | 2025-02-23 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72c7eebf-117c-3fea-a335-91eae8dedfe3 | -20.31062 | -46.48137 | 2025-02-23 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b461269-c7d9-3a9a-81a5-94859f2eae56 | -19.30068 | -44.50488 | 2025-02-23 03:55:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| beef95ad-8ea5-354b-9162-892e2ca19074 | -20.06821 | -40.75347 | 2025-02-23 03:55:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 153ad462-f729-3e52-8313-019950a52e0c | -16.64616 | -49.36804 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5511481b-7c49-3e5a-aa60-6019774f8b06 | -17.67633 | -42.74626 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b827dccf-c4a9-3513-aec8-1fda96b6994b | -15.03549 | -45.61472 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| debe6a91-f50a-31e5-8c10-09f1c0183e9a | -13.62024 | -44.43126 | 2025-02-23 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46864036-17ad-3eb4-a36a-054af570f46f | -16.65111 | -49.3693 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7b928d9-8fe1-3b35-8fe7-926cde2962cd | -15.19094 | -47.59167 | 2025-02-23 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d022a7a-202c-38b6-a635-c4dc69e6d647 | -15.04631 | -45.62415 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9c5dab3-0f3a-36b6-a82c-48d8a9dfb977 | -16.34892 | -43.69813 | 2025-02-23 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1d8d325-cbec-3afa-bef9-39e3b18d45cb | -15.03888 | -45.61909 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3935e07-8525-3105-bc1b-6e53d44ab442 | -16.64676 | -49.36512 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c293309-3818-36c3-b4c9-5558b83d9917 | -17.77779 | -42.8111 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b949b01-9823-32c2-b2a4-49a99fa346ef | -15.04423 | -45.61251 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3eb4531-151a-33ef-938a-9034193d5a9d | -16.64679 | -49.36647 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5c121a9-f56d-354c-b1de-38981bb986fa | -17.08101 | -39.43625 | 2025-02-23 03:55:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc8693a7-3459-3f27-9670-6deb8ee4629b | -20.45261 | -40.364 | 2025-02-23 03:55:00 | NOAA-20 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a5e317ca-7f75-3054-9839-ee1456403a9b | -20.06489 | -40.7529 | 2025-02-23 03:55:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 264a0557-f971-3b47-9d06-ccd1b7f813b0 | -20.58235 | -46.38757 | 2025-02-23 03:55:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9601eebb-ad2a-34e8-8316-008ba12e51d0 | -15.04292 | -45.6198 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 187ab070-1497-3429-b2b1-4caf024757c7 | -15.92831 | -47.45446 | 2025-02-23 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d37b1ef-fbab-3e86-8b22-18fa0fb486e3 | -16.6517 | -49.3664 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
