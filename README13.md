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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b08cb6-f617-3f23-9b30-f5e71639289f | -12.0004 | -49.2683 | 2025-11-16 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 3572c8bc-c93c-38f4-ba2f-77064ed432b0 | -2.5238 | -47.8332 | 2025-11-16 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1326b625-1d68-38ff-8a24-35c64fb9c9f4 | -2.5238 | -47.8115 | 2025-11-16 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| d5a1ddbb-3597-3d09-ab5d-dcde48af59ab | -4.4246 | -43.4038 | 2025-11-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cae564b4-6ddc-3012-bd4d-d74e9efaa5f6 | -7.0554 | -39.6227 | 2025-11-16 03:10:00 | GOES-19 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| a3a731d4-2fa8-3353-a7d4-a90282b6da35 | -12.0 | -49.2901 | 2025-11-16 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cb173eaf-209e-38a1-bf0a-70520d036d38 | -12.0004 | -49.2683 | 2025-11-16 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 45b22001-4c1a-3fdf-be38-fc4792c73862 | -13.81526 | -42.54664 | 2025-11-16 03:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4e3f6e73-7ba2-3f67-9d5b-eb0c96a2d66c | -5.71762 | -41.40166 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| dbf4e274-8837-3106-8097-c7d31b39eb86 | -6.86296 | -38.35599 | 2025-11-16 03:17:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ca289a73-944b-3d94-a406-01067bf567cb | -3.59512 | -41.66256 | 2025-11-16 03:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 521874d0-774c-3997-b55e-f820a934164d | -11.79148 | -44.1702 | 2025-11-16 03:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7b15df2-a3a9-3aae-bd44-e625554c4ca2 | -6.06617 | -41.54873 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 876e0a1a-2e84-3f43-9090-9dfd0310f73b | -6.9511 | -38.40416 | 2025-11-16 03:17:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98aeb5d3-df9e-3a56-b674-d4d5d1d5f3a6 | -6.71126 | -42.13273 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 3c6b90c3-b2f1-3a68-85cd-c0928a408371 | -11.41776 | -43.33023 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c6b621c1-c9c7-340c-937b-ce93ebe7035e | -6.6773 | -42.04681 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f0eb5953-da31-3fa0-af3a-05d7660a8eff | -4.26568 | -38.08395 | 2025-11-16 03:17:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1b93f4d-dcc9-371b-aa90-b24c37f47851 | -8.41073 | -40.45757 | 2025-11-16 03:17:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6cf7de80-337e-3474-8e02-45343f2a047e | -7.53495 | -38.73077 | 2025-11-16 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b28f11b4-1fcf-3cfd-b150-a21bc861d455 | -6.90448 | -38.88297 | 2025-11-16 03:17:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d4f20263-9d86-3f86-943a-a7490b17ff4c | -5.47332 | -40.96815 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4837e1a7-baae-31d1-a9dd-9f186c69c4ef | -6.36144 | -39.62598 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e87af169-f59b-33e4-96c1-e6c1cb16cbde | -6.5009 | -39.51793 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8fec87c5-dafe-3401-a2a8-7c3656c0a25e | -14.05808 | -43.12622 | 2025-11-16 03:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6ce1955b-129b-3b05-a74b-1e558cea3056 | -11.71067 | -37.64665 | 2025-11-16 03:17:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64208d6b-0acb-3096-aeab-e6da415d9b9b | -7.05345 | -42.24431 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1073c112-c848-37c0-8287-0dfc6afa40b1 | -7.19176 | -39.20965 | 2025-11-16 03:17:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e202dd01-d16f-3717-8797-f476be57aedb | -4.26011 | -38.08303 | 2025-11-16 03:17:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1243802-5bb2-3a12-826e-b6fec120a57c | -6.71782 | -42.1335 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 011fac7f-7ce5-3118-9b9a-1833bddfc61b | -7.15194 | -41.76455 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6193e1cd-18c4-3dc1-9183-9f482b57ce2b | -6.85396 | -42.8427 | 2025-11-16 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b17b4ebb-8eaa-3293-b075-52b97d79629b | -3.85576 | -40.768 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 4231b7ac-3676-3f29-bb80-3a5a710e9201 | -6.36817 | -39.62273 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 21f0bfc6-5b12-3c02-bb21-943f8201d9fd | -7.15405 | -41.75346 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d45c170-99d5-3af6-b298-4083e91f5139 | -7.1967 | -39.21489 | 2025-11-16 03:17:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e7cd8162-b8af-3b78-a52c-9fc97b682e2d | -6.51769 | -39.52601 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ebf5c39-9bcb-34e5-b391-46fb906d9313 | -11.41317 | -43.32318 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adf988bd-7163-36db-8cdf-f8eaac322330 | -3.85131 | -40.76886 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 5c52b165-954d-3b68-a8f6-c156f5cacdda | -7.04534 | -42.24939 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b5dc01f8-c49f-3b5d-9fbe-bf0c680eb5ea | -6.696 | -40.80048 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b7708b9-adf4-3e1a-8b7d-e696f4448eb6 | -5.98949 | -41.91323 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 85d2cef2-8c7c-3790-82a8-0de560559057 | -6.67589 | -40.80259 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a76a2d7a-0ec2-38c5-b977-2df761a2e8bb | -11.41095 | -43.3288 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c653e718-307d-3904-943a-443895a29f0c | -3.85793 | -40.77007 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0bff97d0-9b79-34d6-97a7-e26c36fdd662 | -3.58986 | -41.66147 | 2025-11-16 03:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4bc5dc72-c0a9-3662-84e5-d68dcea0d1eb | -7.53432 | -38.7343 | 2025-11-16 03:17:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b6e0c6a-83b8-302a-9e1a-c5cc339b24a3 | -7.0535 | -42.24375 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 92f2d87c-2d70-3bdb-ae7c-f4fbe2d971ac | -14.20522 | -41.84303 | 2025-11-16 03:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 888c3166-f3d6-326d-b82f-c2e88711c91b | -4.9517 | -37.39233 | 2025-11-16 03:17:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cc4a433-94a1-3fcf-9f44-1378bebf4b2b | -14.20201 | -41.84623 | 2025-11-16 03:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b2cfe7e-2911-356d-ab85-0811782b7a8d | -5.99716 | -41.91254 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 77411e67-2396-3b0e-983c-98be869d99c5 | -6.39587 | -42.29108 | 2025-11-16 03:17:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ea3dac9a-97b6-3152-8e56-ca4f949d966e | -7.04641 | -42.2439 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cb585e8f-f97b-36b7-9e64-5f748b10c23a | -6.67163 | -42.03937 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b66d8b00-d172-3503-ae06-8ebdbf4a19db | -6.16755 | -39.92255 | 2025-11-16 03:17:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df77af53-3fab-3169-bd23-ef702d28c6fb | -7.19247 | -39.20574 | 2025-11-16 03:17:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae12ce1b-a5ce-3420-ab59-7294aebef2c6 | -5.7216 | -41.39741 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f4d03d12-6149-30cc-b8e6-d13284c811e1 | -8.41159 | -40.45294 | 2025-11-16 03:17:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 056c4a19-34bf-375f-919e-8ef602fb9378 | -7.28137 | -38.90887 | 2025-11-16 03:17:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45b9c581-1cee-36dc-b0ea-dc52ca18573e | -8.33645 | -41.25003 | 2025-11-16 03:17:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3c96e743-283f-3de5-ac55-3d1595fd0155 | -13.71472 | -43.66388 | 2025-11-16 03:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e6e3db1-6148-3ef2-b3ab-50a72c6b05fb | -3.58812 | -41.66128 | 2025-11-16 03:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f9b6bf3f-77cd-3ece-95bc-6206331f74db | -13.8276 | -43.19215 | 2025-11-16 03:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| af0ec0ca-bc10-3377-8152-f406748869e5 | -13.38769 | -40.65629 | 2025-11-16 03:17:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a473dfab-c09e-30c2-be92-f267e45249c3 | -5.99632 | -41.91464 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9279515-9093-3a49-b3b7-9e407fee4fbb | -5.71385 | -41.40199 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bb802739-e776-3ffb-ae04-cf77c7ac8323 | -6.95656 | -38.40501 | 2025-11-16 03:17:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c524080-50a9-3a2a-89a5-330853b9f6bf | -5.47276 | -40.96651 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ce1091a8-eeb9-35e0-8e00-7246218edd87 | -5.4723 | -40.97399 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ff36fc7e-a9fd-35ca-8f48-aec9271ce608 | -6.69055 | -39.09815 | 2025-11-16 03:17:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dffce22f-9dab-3489-8d0e-bf0a77ccdb3f | -6.67964 | -40.80679 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 82bdf506-7c13-3089-b821-a6ae25da0b99 | -6.67044 | -42.04204 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 12844914-36f1-3554-9067-66d175047582 | -7.76421 | -38.94375 | 2025-11-16 03:17:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| e830771c-0c34-3c96-90ef-641dcf9538dd | -5.53057 | -41.77767 | 2025-11-16 03:17:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5fc4a3a-8c3a-3d16-ad3f-1ada6e7f3400 | -7.19811 | -39.20718 | 2025-11-16 03:17:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 11d3696a-44a9-3f87-b1f6-f99fc6e05b3f | -6.86131 | -42.84293 | 2025-11-16 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 111ba927-51b9-31ab-bfd8-aa8a9cfbdaac | -13.82181 | -43.18941 | 2025-11-16 03:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c87f34f2-130e-355a-a540-9507c6a4af96 | -6.39734 | -42.29076 | 2025-11-16 03:17:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6c5f1cac-b3ef-345f-8625-c2a0993381c8 | -6.90125 | -38.88089 | 2025-11-16 03:17:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4dc5d720-d119-353a-9019-a896f03b1bba | -5.9975 | -41.90818 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 597a97e9-af40-3207-aecd-4334951f4430 | -14.05795 | -43.12469 | 2025-11-16 03:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 58df6d41-5cd0-3581-b5a9-716b72c54bb4 | -6.90686 | -38.882 | 2025-11-16 03:17:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c3b50fd-e0d2-3552-b846-117d6dcf677f | -7.14996 | -41.75729 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 36f83d0e-c343-35a0-af3a-eed9b82af68e | -7.14897 | -41.76272 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0aec8481-08e5-3e76-8ceb-7e0e10639fce | -5.47169 | -40.97235 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 454c6871-0208-3e9b-9b6b-77c692271eac | -6.70136 | -40.80704 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 736ffe23-08d3-34a5-91dd-136dcc58d4d0 | -6.6769 | -40.7972 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8144011e-683a-38c1-997d-f5d2e99765e2 | -6.95172 | -38.40066 | 2025-11-16 03:17:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e50a2bfa-19d6-3013-a1f2-ca390345e2f2 | -6.00435 | -41.90949 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a88489e-69ee-31ca-bc5d-01f168b446b2 | -7.1479 | -41.76854 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 05d12875-7758-3aec-a58c-8650aec4bdea | -6.68418 | -42.04789 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80c5e3fb-fed2-3826-9702-23e564fd69d1 | -6.86234 | -38.35951 | 2025-11-16 03:17:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 602c9a00-790e-3625-a3be-169ca0a56b36 | -7.0495 | -39.62973 | 2025-11-16 03:17:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| c29066e9-2e03-3b7f-848a-b9609ccf533d | -7.41198 | -40.0721 | 2025-11-16 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 519597be-a18d-394e-90d5-1a8ac136c29e | -7.75866 | -38.9427 | 2025-11-16 03:17:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 1c989f34-7376-34fc-bb20-343546df7605 | -11.78892 | -44.16568 | 2025-11-16 03:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23052843-2174-3c90-8d7f-80bff65514fd | -6.93029 | -39.62593 | 2025-11-16 03:17:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4282058f-e064-31c0-8fcc-9b506ba97581 | -6.67328 | -40.80561 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| afa76db4-a166-37cc-989e-1b5d92090f26 | -11.41646 | -43.33661 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README14.md)
