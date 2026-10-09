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

## Dados Diários - Página 252

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aee4c16b-cba7-3abe-a1dd-64fee2fa5c24 | -5.70022 | -41.74655 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5bdd6e37-2a38-30cb-8f7b-9da1e9ec51ab | -5.95022 | -40.94438 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| b12bc3c3-fdd1-346d-9673-2f0e994c63f5 | -6.01339 | -40.97354 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 803583ee-d941-3d37-ab00-6c9e4e9128b9 | -5.48244 | -41.21465 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 045ad080-bc76-3863-9723-a30fd787a2ae | -5.99716 | -40.9517 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| c139ec3c-3f7a-3d83-b4ae-ae229bdf5ded | -7.12985 | -41.81351 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 9b4377b5-6910-3dce-90c0-a0c01775f75c | -7.0685 | -41.60313 | 2026-10-09 15:24:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 72c92e4e-1d95-3492-9652-22c7a5b48e8e | -4.36826 | -41.81257 | 2026-10-09 15:24:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b9063d5b-1dde-3d55-9249-8ff4d22f91a3 | -5.5299 | -39.85343 | 2026-10-09 15:24:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7f73feea-6f6a-323d-9242-9dabfa18e037 | -5.98417 | -41.39413 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 53d7ff3d-4ee5-3008-a097-e93253d003e5 | -7.07535 | -41.60194 | 2026-10-09 15:24:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 1a409068-8de9-3ff0-974e-35e896b454f6 | -6.0131 | -40.96535 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| bfe77960-943d-3fd7-be73-8fe4c72a07dd | -4.31303 | -41.23775 | 2026-10-09 15:24:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 17a5b14a-151f-3f07-ae01-da8565744037 | -4.579 | -40.66698 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3aa8ff96-37c0-3323-b0da-e03d97401798 | -5.99009 | -41.38733 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 69e5b485-8287-3448-b8ca-c4b3f6624cd5 | -5.96097 | -40.92576 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 30010d22-a499-3401-87df-d2fb59be87aa | -5.3166 | -37.4008 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cf5e98b2-6306-3a2d-9e8e-29ed0e8edb05 | -6.41678 | -38.42846 | 2026-10-09 15:24:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 6965f5e8-7799-365a-857f-0863ff669229 | -5.96026 | -40.92062 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| bd0f59c3-455a-3580-846f-c627b5d74dca | -6.01549 | -40.98237 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| cba034d1-c05d-331e-871c-c8522f99ddb9 | -3.19105 | -42.95971 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bb4e9453-fa81-39cf-be58-2667e5b7a3a8 | -6.55386 | -38.07409 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9179e6a5-8f8a-3bfe-b0e9-8c107c70ec8d | -3.91072 | -42.113 | 2026-10-09 15:24:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 9a7f1f3f-67c3-3d49-978a-ae191370b9f2 | -5.23881 | -40.5937 | 2026-10-09 15:24:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b46e608c-706e-313a-8dc7-5a5a5412d074 | -7.13102 | -41.81234 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 97bb9dd1-6ff3-3101-b1a5-30dd16200eb9 | -5.98755 | -41.36847 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 60f0a557-360c-3dee-ae6e-c35a11a89c5e | -6.8073 | -39.34139 | 2026-10-09 15:24:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c500c883-b0c9-3a16-ab0c-be9136cd6a90 | -4.61824 | -38.53127 | 2026-10-09 15:24:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0c93be08-f7b3-34ac-a487-30c205ed51e3 | -5.15198 | -39.50547 | 2026-10-09 15:24:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| c7f13ab7-8256-3094-ac63-cca310271d56 | -3.5047 | -42.58513 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| bd1a13d0-4296-3a89-95a4-8ecf6c3d4d99 | -6.14089 | -37.81285 | 2026-10-09 15:24:00 | NOAA-21 | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 02829a78-dc49-3326-9fb8-54d0d30eedce | -3.2134 | -42.96386 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6eeb3b0c-1e23-3cc1-bbbc-62ac622a6a5e | -6.58297 | -41.55608 | 2026-10-09 15:24:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8b7d46bf-c23d-3a9b-88ab-2c5379f01733 | -5.9967 | -40.94345 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 7072df44-dd9e-3907-833d-aef16abbbc88 | -5.98335 | -41.38802 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 8e6d2e07-bfcc-3177-bec5-c7bf4eaa7a76 | -6.48936 | -37.08222 | 2026-10-09 15:24:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 874eff07-2dfb-355e-8baa-42e6ca8a40f1 | -6.80012 | -39.33337 | 2026-10-09 15:24:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 886b2e13-fc01-3890-a36d-600c7df3f305 | -3.21441 | -42.97094 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 39b638e0-38f8-3e2b-a0eb-f98e86029301 | -5.17409 | -37.44935 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4472cb47-1757-3622-b0d7-7394472b2038 | -5.06707 | -36.97462 | 2026-10-09 15:24:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4d0366de-85d1-369c-8556-50ae4321d843 | -5.96528 | -40.91176 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| cd58312a-37eb-3651-b010-d9844a60dd41 | -4.57547 | -40.66684 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 69f9e8ff-4fab-3ab4-b1a4-afe781abd7a9 | -3.19436 | -42.96223 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 89f9687b-1129-3b7e-8739-45cb4b4cd8d1 | -5.9884 | -41.37481 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| d083754e-8dde-3345-824f-3327ce03bd4b | -6.55294 | -35.51239 | 2026-10-09 15:24:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1f122adc-38b8-31d5-af77-d99cad1fa3f2 | -6.00646 | -40.96558 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| c58af4a7-c3f7-3bbf-8539-002ab3895802 | -4.73345 | -39.39166 | 2026-10-09 15:24:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| b573a0c4-14d2-34d2-b1e9-0bb86b2a3514 | -6.4112 | -38.42942 | 2026-10-09 15:24:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 12.4 |
| a4f4c595-3355-3eb1-9561-84cc0e5ae54d | -6.00524 | -40.96243 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| b4503215-0ca2-3935-8e8f-d1d089a1503d | -7.06472 | -40.95131 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 82e333ae-aee6-36da-9f06-9b63ea617410 | -6.37181 | -38.26107 | 2026-10-09 15:24:00 | NOAA-21 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1861afa0-75c0-3de8-8a31-9bbc12426a7c | -6.55494 | -38.07593 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4c422e93-31ed-3ada-a0f2-734bb15559c9 | -4.54886 | -40.70571 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19bbb6e6-f043-32ab-88e4-d574bc7d135f | -6.01471 | -40.97679 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 5fba31d5-8fb3-3238-ba76-f765b300ff17 | -6.89092 | -41.47759 | 2026-10-09 15:24:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 93d6c398-73d7-3fc7-bee1-c3ab0ce4109b | -7.1301 | -41.80532 | 2026-10-09 15:24:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b5a943f5-0838-33cb-ae03-832d6ea4a41e | -6.5733 | -38.84221 | 2026-10-09 15:24:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 5306b8b2-67a9-3722-a6b5-63b26617a398 | -5.17203 | -37.45052 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 267ad4e6-8fca-3d09-84c5-b00f718c05e4 | -3.19205 | -42.9667 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 99d55772-0e17-321a-8d06-9a60a3258cd4 | -6.86248 | -41.75096 | 2026-10-09 15:24:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| faf72eac-27a2-39d0-8538-6577639ecd97 | -6.85667 | -41.75873 | 2026-10-09 15:24:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| f5fd86bd-467c-37f3-9ea8-b5c293792e48 | -6.68797 | -41.76044 | 2026-10-09 15:24:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 761010a8-ff62-3f97-8cbc-45caea86ddc4 | -6.00676 | -40.97384 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 6cdc3155-8887-393d-95de-b4dc1b762fb6 | -6.8067 | -39.33699 | 2026-10-09 15:24:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8b7c8d44-eee4-3477-8cab-bedb2cb78192 | -6.006 | -40.96812 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 3f18e32d-bb48-3721-9f74-b7a21f988a63 | -6.04801 | -35.24639 | 2026-10-09 15:24:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 74fb07a3-3420-3935-bb4d-b836f73dd6fb | -5.49639 | -40.54555 | 2026-10-09 15:24:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 3659a9dd-c478-3822-9441-2ff11729b5dc | -5.70893 | -41.65668 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e67c9ebb-fcaf-39d0-adbb-b9b02d13fef3 | -3.22055 | -42.96315 | 2026-10-09 15:24:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| f713aaaa-c37e-3a14-b83b-472c9204d6e9 | -5.16721 | -37.32377 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bf2a7c50-b943-3b68-b87b-a334eaf70789 | -7.19275 | -42.00962 | 2026-10-09 15:24:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7fa33ef1-d16e-30a9-8f77-5e216aad5b9c | -5.9964 | -40.94601 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| de9ea35e-23c5-3f83-83f2-be1842daa089 | -6.41734 | -38.4326 | 2026-10-09 15:24:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1930620e-7cb8-3b64-82f9-5c5a06100e38 | -7.07473 | -41.5971 | 2026-10-09 15:24:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a3286508-48cc-3fe4-a068-ffd27c0cd873 | -6.76647 | -38.26645 | 2026-10-09 15:24:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8ff28407-e77d-32d9-adf4-9c4f11a1cdb1 | -7.06899 | -40.95 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bb80e65b-94fe-31fd-89d2-9a8d5e6c9975 | -6.21228 | -37.87318 | 2026-10-09 15:24:00 | NOAA-21 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a4277c9c-7413-30bc-bfc9-ddd24c1ce5d3 | -4.54255 | -40.70667 | 2026-10-09 15:24:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3a316b3e-230f-3344-9494-28347ac896c1 | -7.53897 | -42.09911 | 2026-10-09 15:24:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 2978eeb2-a358-3d07-84a8-f72e96437624 | -5.49003 | -40.54627 | 2026-10-09 15:24:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 86503e50-696e-3300-8f14-6528a045e77f | -6.00409 | -40.94862 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| b75677f1-9215-3a3b-8163-a7fe7e4d0c78 | -5.97661 | -41.3888 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 315809a5-732d-3b90-b0cf-424840afc810 | -6.37709 | -38.26046 | 2026-10-09 15:24:00 | NOAA-21 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4b8c5002-0cbd-3a81-82e5-7987cecb5598 | -6.85638 | -41.75838 | 2026-10-09 15:24:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 934ddaf3-95d7-36e9-86ce-eef29d9ec973 | -4.3122 | -41.23199 | 2026-10-09 15:24:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 673cc5dc-80cd-3497-bd01-ac04a5e329ba | -5.53099 | -39.85115 | 2026-10-09 15:24:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f307471a-f5ab-35dc-a541-073999ce67b7 | -6.49407 | -38.95797 | 2026-10-09 15:24:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3e8c15c1-65bc-362b-b770-39b963ab9dac | -5.16643 | -37.4482 | 2026-10-09 15:24:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 22341769-5995-32b0-aebb-ecc6394a8871 | -6.00374 | -40.95112 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| e27d0988-649c-3cc2-bccd-a9d9717d6c29 | -7.07202 | -40.95537 | 2026-10-09 15:24:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2db81dd6-cdc8-3350-9030-d971e3a59222 | -6.19599 | -40.80262 | 2026-10-09 15:24:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c1770ee4-c1e3-300c-8249-8840e100154a | -5.15141 | -39.50127 | 2026-10-09 15:24:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f5489930-8467-3840-98d2-33783b65efe6 | -6.1964 | -40.80576 | 2026-10-09 15:24:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e938c221-58b7-3b74-8527-06f333976b30 | -6.0139 | -40.97105 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| dc0717eb-0725-39d5-bd9f-ec6dc056b025 | -5.97634 | -35.57601 | 2026-10-09 15:24:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b7c089df-ba1b-33c6-9c68-ae9ad598dc63 | -6.90084 | -38.54966 | 2026-10-09 15:24:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d67b01df-6034-3795-af68-3aafc3473511 | -5.75485 | -41.68825 | 2026-10-09 15:24:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 18ef04bb-d612-3f26-b075-b0f6f847127d | -5.96596 | -40.91694 | 2026-10-09 15:24:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b555af59-4770-3de4-bfd3-55c06c9fefb6 | -4.30741 | -38.1089 | 2026-10-09 15:24:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 5c8a0148-eb69-3709-8547-4f886619993b | -6.15785 | -39.44567 | 2026-10-09 15:24:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |


[Clique aqui para ver as próximas entradas](README253.md)
