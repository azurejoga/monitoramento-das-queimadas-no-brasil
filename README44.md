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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96e2731c-18ea-3dca-9b26-5034c6ad162b | -9.93014 | -48.98652 | 2025-10-26 04:51:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3f3086c-9b1b-35ee-b107-c61ac810a4af | -8.15776 | -47.04 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0e4031a-eb1f-32c9-9bde-5d5c552005d3 | -8.45929 | -48.02578 | 2025-10-26 04:51:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 958ee955-bc2a-304e-a991-bac6ed7e250e | -8.49823 | -44.73322 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d34abd-0aec-3a1c-90de-c047b44a4ecb | -14.51167 | -42.9996 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| f61ccefd-338b-331e-9a84-ccf801171063 | -11.62951 | -54.55632 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48d155ac-3f0e-3ee9-ae93-ca660e4839c0 | -11.36469 | -54.31682 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b9a19ed-fda3-3f5a-950d-50208967ac1b | -8.12326 | -47.03862 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7650a017-3c76-3a8d-82e7-536951e2b7d2 | -10.64418 | -47.91877 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b5de047-a69e-3a27-b98f-1453efd3fe09 | -7.56921 | -46.26791 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cc53a401-0975-3fd6-8e1f-5d7d3cee4d72 | -13.3309 | -47.9235 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90e33d1f-c699-3210-89c2-1cc809a7742c | -7.10771 | -47.94835 | 2025-10-26 04:51:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d89ba9b6-b92e-3c79-b42a-987211ffa83c | -8.3328 | -48.18237 | 2025-10-26 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbe1af98-6738-312a-b80c-d5ffbda81395 | -11.87838 | -56.40173 | 2025-10-26 04:51:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfddd46f-9119-3027-a3c9-87b890ae6db2 | -7.84682 | -46.43305 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 526898b9-aa71-3c05-95fc-c96f8f68e6c4 | -11.49432 | -54.63576 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fee324d-7674-3a77-a0fa-92379a0520d6 | -10.80172 | -47.86858 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ffb930a-6e8a-307c-8adf-28bab0939b27 | -11.36194 | -54.31276 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48efdcc7-c13c-3862-b075-54d227e71236 | -7.56264 | -47.11928 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da0f615f-d315-355d-b415-316647a354ee | -7.80586 | -45.39757 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5e14cd4-acf8-3e85-b86c-c9c6f573cf97 | -9.86089 | -50.54332 | 2025-10-26 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b453774c-c47e-3602-b4ff-131e0cf16541 | -7.88145 | -45.71684 | 2025-10-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea59df4c-29a9-352a-baf4-5f157d544d80 | -9.93077 | -47.6436 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f18a7f4-87f8-37ac-a9f2-f97656f4a5fc | -13.88666 | -48.41947 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68817a2c-88d2-3ad5-99eb-1b62feeb1021 | -12.35234 | -54.1397 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9979bd68-486e-3109-ab12-5758ca0d78a3 | -13.91759 | -48.3798 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb1eb6c-de1d-33a7-a156-39a7fa4834ab | -8.53696 | -47.20063 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07c463cc-1f76-3ecf-9e3d-5ae999670a6d | -15.60126 | -49.29544 | 2025-10-26 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e373ac1-ce69-3042-bdef-472c3989d56b | -17.31621 | -43.63556 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c87df517-1c3d-30a6-bd7e-f0ce354170ec | -15.36558 | -42.93147 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ae17768-c423-3c4d-b16b-e26df02d2a51 | -17.32085 | -43.65083 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 254e2ebd-c61c-345b-ba45-1481375bc932 | -17.31577 | -43.64013 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cdd4dd0f-76b7-306d-8a52-ceb7e83af8fb | -17.01051 | -55.90108 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5e338516-0f8c-38e9-894b-a8b2d395e27e | -15.19042 | -47.23166 | 2025-10-26 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ea7c272-bf9e-3dc7-9df4-c37b65b4db0e | -17.3206 | -43.63538 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e98b6dd4-9be2-35b8-84bf-c5be397195a7 | -20.24705 | -44.10751 | 2025-10-26 04:53:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7e3b5e79-3ad2-39cf-82a3-d0e129f4fb71 | -15.18104 | -47.23119 | 2025-10-26 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e22df4ef-0392-310f-a7b8-97086648127d | -17.39725 | -52.02424 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0280c29b-aa74-3d85-bf9f-0290d7ac0f68 | -15.18574 | -47.23138 | 2025-10-26 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 141b824f-14ef-32a2-91ae-cc1afbf3586e | -17.32686 | -43.65178 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a080b7a-e68f-3aa5-b2ed-132f415fd8f3 | -17.31912 | -43.6498 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1060d2e8-3ca5-3bd0-b7ac-977cc7c4de74 | -15.36179 | -49.51054 | 2025-10-26 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3270ad25-7f47-3641-83e2-d58a3ec83236 | -20.32497 | -46.54039 | 2025-10-26 04:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85e041d5-472f-3cf1-8866-4911f6fcbf34 | -17.33865 | -55.01517 | 2025-10-26 04:53:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 481a3f0e-9d9a-3cdb-a4e2-825983848fd2 | -15.35995 | -42.92823 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 60534d9a-7719-3a4d-83ac-698c6769df2e | -17.32268 | -43.63183 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f62d795b-932a-376f-ac77-9bc11fa938e4 | -15.30511 | -53.01889 | 2025-10-26 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf60003a-3798-348e-bb53-022fd0f7023c | -17.32226 | -43.63618 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2eca254-fa7b-364d-9dbc-565ac2f69b98 | -17.42897 | -46.88215 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7f3f478-2d53-3af9-9ece-0746fa080d80 | -15.58564 | -43.21239 | 2025-10-26 04:53:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e96993ee-5249-3bc5-9785-703c2149f6bf | -17.3329 | -43.65249 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02ae41ca-7426-397c-a3de-c2432ec6fd89 | -15.35991 | -42.92566 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f8f65879-9a4f-39be-944a-593cbf3021fb | -15.36579 | -49.51113 | 2025-10-26 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b43afa0a-bb97-3dd1-bf8c-af23e5ddb32a | -17.05608 | -51.52081 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f9123d0-6c43-3b8f-9633-ce82a3092f99 | -13.48386 | -56.55789 | 2025-10-26 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc267c74-2977-3bbb-8c3d-442b613c2b3a | -17.32461 | -43.65574 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33c1b860-2480-365f-b149-d9616132bc28 | -17.01598 | -55.90952 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 84cf315a-f4ed-3f4d-bfbd-361dce42691b | -17.32665 | -43.63605 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f932e7c-71a6-3cc8-bb79-870274af626f | -17.3271 | -43.63167 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fb7b0d2-7976-34d5-bf10-451bc9ec87c6 | -15.83 | -49.07592 | 2025-10-26 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f30711de-3bbe-390b-bc68-061c156a2103 | -18.48016 | -44.42949 | 2025-10-26 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13f5060a-05c0-3a1f-bd12-4aaf60039f9c | -17.01384 | -55.90166 | 2025-10-26 04:53:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2b9070f1-4a97-30d2-9f4f-25a96031c5d5 | -16.28787 | -52.9353 | 2025-10-26 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 248209e9-d8d6-34c4-8afb-a5bfa65ad713 | -14.42964 | -49.42989 | 2025-10-26 04:53:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba0573db-01cd-3e60-a89e-98a344ea76e2 | -17.32132 | -43.64591 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86816617-ed95-37e8-a053-c7962d41ab43 | -15.29525 | -50.75802 | 2025-10-26 04:53:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8c57407-67f8-3b98-a779-882c62f87273 | -14.76937 | -46.62019 | 2025-10-26 04:53:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05e6946a-00d3-341f-9f0e-04caab201a33 | -16.44369 | -53.962 | 2025-10-26 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd699f0-6123-33a7-99fb-014ba6c995f5 | -14.46065 | -51.51411 | 2025-10-26 04:53:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ca73cf0-1961-3bf1-aa0c-81824a95a465 | -15.9407 | -51.05939 | 2025-10-26 04:53:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e171d59-bd11-3fb2-b9b7-480f2450d040 | -17.32873 | -43.63248 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 535d07fa-4e57-3a13-ba8d-daa0f1e2b7d5 | -15.27157 | -43.17944 | 2025-10-26 04:53:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8f4c4a5b-ed33-3a5c-976d-7dc6783a09c0 | -18.47973 | -44.43378 | 2025-10-26 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b8a6e08-5ff5-34ba-ba46-4a4a85c705a4 | -14.9764 | -54.82753 | 2025-10-26 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9e4efe5-18ba-31ed-a1ed-e6c251b7ac5e | -14.83906 | -52.45049 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3036a3c-3e9a-3b54-844f-e82f1518df69 | -15.6905 | -49.40842 | 2025-10-26 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01d05f3c-5ed2-30c8-ba84-515e54576303 | -15.1192 | -43.2548 | 2025-10-26 04:53:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38bc49b0-387a-31bf-9a1e-f67dc0a214dc | -19.40472 | -45.87228 | 2025-10-26 04:53:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08b9281b-aa9c-35e3-b34c-3cc7985ba5a8 | -15.60653 | -46.78508 | 2025-10-26 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b2c8bc-e78c-3e7c-ad5f-ce1737ad21d1 | -17.41132 | -46.72722 | 2025-10-26 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe2212ab-9789-306a-bcde-a32671f979c1 | -14.43885 | -49.95532 | 2025-10-26 04:53:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0fd523c8-24c3-31cc-b010-c8618a627cdf | -13.48733 | -56.55847 | 2025-10-26 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cabed0c-5d89-3a75-87e7-f2d7adb0d494 | -17.0555 | -51.49808 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dbd9c8c-0c68-3d6c-8128-d9a24ab6dff3 | -17.3218 | -43.64093 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30b0dd52-b5b2-3532-82eb-a1789b82f72a | -17.15762 | -50.86125 | 2025-10-26 04:53:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e389fa9d-673c-3b08-8b79-817cf5277fbf | -17.32512 | -43.65077 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5f33123-cddf-3ef3-bc00-413ad1cd2afb | -14.73839 | -49.69114 | 2025-10-26 04:53:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb14e52b-4e73-36d9-8adf-f909e0158a8f | -16.20342 | -52.62829 | 2025-10-26 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9fdc620-825d-30ad-92eb-a66254129b73 | -17.21368 | -47.6539 | 2025-10-26 04:53:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 681dd5a5-d4ba-3b48-9878-78ad87f9e780 | -15.18626 | -47.22726 | 2025-10-26 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cef4390-f998-39c8-b8bf-9f38910a6ad5 | -16.62591 | -46.28965 | 2025-10-26 04:53:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7514247-d508-3df6-9554-e77c743e3126 | -15.3661 | -42.92916 | 2025-10-26 04:53:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3fc65dae-ce0f-3bd0-b067-18a6cef331e5 | -15.26799 | -56.65585 | 2025-10-26 04:53:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ed19ac-4c6c-3592-8f63-464d3be71862 | -20.24745 | -44.10305 | 2025-10-26 04:53:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 55630987-f961-360c-aefd-54e9ae16c5e6 | -14.98647 | -47.88079 | 2025-10-26 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5328c96b-3740-31d9-9ce5-a92c98fd45d6 | -16.92239 | -55.53927 | 2025-10-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ccbf09c0-1d7e-3bd7-b5dc-d1c6ba22c60d | -17.31361 | -43.64394 | 2025-10-26 04:53:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c643f300-3217-38eb-b620-31ca8e54c0f8 | -17.05183 | -51.52462 | 2025-10-26 04:53:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad88d82e-2300-3251-a642-9bea8c782148 | -14.83618 | -52.44622 | 2025-10-26 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a27ace3-bae5-3b11-96de-2467707025ec | -15.12523 | -43.25544 | 2025-10-26 04:53:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README45.md)
