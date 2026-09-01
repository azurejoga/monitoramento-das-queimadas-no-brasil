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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da2aa606-bf97-3a8b-a7ca-e8b2455e099b | -16.37247 | -54.52338 | 2026-09-01 05:38:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0007cca7-6db8-30d2-872e-a2a96c778b05 | -15.48844 | -56.01346 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b6eaf57-8a6e-3786-af12-906eac98200a | -14.39724 | -52.50891 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83354ea2-a4ad-37fb-a72f-9a5588ed9181 | -15.87093 | -56.47792 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4f4c9305-81e9-3d02-abaf-a38c7f55a4aa | -15.48769 | -56.01951 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b3cef2d-f8b5-3a66-bbbd-196005682bf7 | -15.87029 | -56.48336 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e17ec6b-9caa-3f2d-b085-510c90eec2dd | -14.2577 | -52.88209 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 866d39e9-6a36-3387-a151-0f2878b5ff4f | -13.38951 | -51.75271 | 2026-09-01 05:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f6562af-8b33-336f-a809-ea5a3b6d38b4 | -14.38793 | -52.5376 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70c6791e-bf56-3800-89fe-558cef6fef6a | -14.66212 | -53.54282 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b25bcbff-6a41-37fb-ade5-8a34d03e2e43 | -15.26022 | -53.87982 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3848739-7087-327d-9cf1-c1f2b9b7298a | -10.10141 | -68.40598 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3140adb6-d4ad-3a9d-bda2-fde116d6dcac | -14.50579 | -59.83836 | 2026-09-01 05:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad551271-f2dc-3779-8e75-58f88cae556d | -14.45877 | -52.52143 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb701b30-7d0c-35e8-b3c6-a25fc735b9e5 | -14.40489 | -52.5071 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d8d6fbb-6561-36be-b621-f758c8d86928 | -11.50022 | -60.58689 | 2026-09-01 05:38:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35274f26-8c1b-3659-9809-e083f484cfc2 | -10.22052 | -69.04053 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f414e97e-0ff8-3ba1-9c86-4d374a18ae02 | -13.39018 | -51.74671 | 2026-09-01 05:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 625e5d1a-4d7c-3087-90e4-3e3b75bc7a8b | -15.76361 | -56.09341 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a91c15fa-da94-32c6-b7e4-47339214880b | -14.73381 | -53.58645 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 720d14b6-b11c-3745-aa8b-5251213abc09 | -15.00959 | -52.7664 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62228d31-c342-3c76-b2e8-c5e83b26fe54 | -14.66795 | -53.54365 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| daaeb780-fe1a-33b5-b0c2-0941fabdd3a1 | -15.48937 | -56.00456 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd8b2f26-1824-3e57-87e2-73c9c36f491d | -14.26574 | -52.86459 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c50c26e-2135-30e1-9380-b8b88b10950c | -18.2499 | -52.74272 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c456da0d-c854-3efa-ad8e-c0e373a0e88d | -11.48597 | -58.51674 | 2026-09-01 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21d0b6d4-3ed8-3c31-b991-6b0b83a84110 | -14.38194 | -52.54347 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0741292-ca5e-3978-8bca-d1d52523e1b8 | -15.76291 | -56.09916 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d2cbd3e7-0411-3fe5-9c23-5d007ef20ef7 | -16.55572 | -52.51031 | 2026-09-01 05:38:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e21a9be-2fa8-3d47-88d7-7360a586be38 | -17.22952 | -53.26676 | 2026-09-01 05:38:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c5eca78-5b5b-3d30-b933-22ff128540b5 | -16.04098 | -54.38417 | 2026-09-01 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9318c1e8-634a-3a42-aecd-55996bbf688f | -15.43387 | -52.68323 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c6df98b-0bb2-3592-b37f-912c69a80623 | -16.04569 | -54.39306 | 2026-09-01 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b62daae5-9cab-3fe1-8675-d95759387fd5 | -14.47133 | -52.52158 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10396687-967a-3b9e-a3d0-515226188fd0 | -14.66118 | -53.55116 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92e27b7c-2ba8-3ae3-aa5f-595f77037c07 | -15.25237 | -53.84554 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce0d13aa-80de-3c98-b680-f3202b828cf0 | -15.63876 | -56.38201 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8e4caa5-7d0a-362a-a98d-577ead2c510a | -15.48868 | -56.01054 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a236e38-caeb-3922-8402-18087bd5b9ed | -14.38742 | -52.54241 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbea983b-292b-33d9-9540-25c2057ef406 | -10.19278 | -69.34999 | 2026-09-01 05:38:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 034972b2-d418-378f-aaec-f5407d875e32 | -14.38228 | -52.53164 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f5616e6-caed-3faf-9626-585e4843c19a | -15.24566 | -53.85337 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a52813ee-4ed4-3b37-9c39-9f22b02cb0e0 | -14.45996 | -52.51056 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac334171-6449-3707-973e-e25889ca49de | -15.43343 | -52.68761 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e42db022-985a-3757-a0ef-be584685cd41 | -15.77291 | -56.10052 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 01a65565-1a7d-3e9d-9715-f936af9ad188 | -15.24034 | -53.84863 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58605935-99c3-31ca-a61d-fa7071ca54b0 | -14.38917 | -52.53498 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 421aa751-fa9a-3e5c-9ef8-2488081923d9 | -17.19185 | -54.31145 | 2026-09-01 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acfdf529-6bb8-3a80-bee3-281bee84abed | -10.61927 | -67.9276 | 2026-09-01 05:38:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3033d6a4-338a-3c01-bb3b-c8f74dec2228 | -18.25087 | -52.73184 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3be4358c-ea64-327b-97b7-b8ddfc4e1931 | -14.67424 | -53.54039 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce1683d7-f2a2-323c-b290-1336f4b6763b | -14.3905 | -52.51317 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 075b15d9-72b6-32a9-a40e-e3e03744b17d | -11.48547 | -58.52021 | 2026-09-01 05:38:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a659cb2e-81cf-3966-a1f6-391b4ea91bd2 | -15.75226 | -56.10313 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ffd7f844-8adc-305b-8c36-24d39d7f8dfe | -10.13629 | -68.58675 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 467fc6bc-2bc4-3c4e-8f86-6238df55808c | -13.96013 | -54.39611 | 2026-09-01 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44e0a2d3-578e-3835-acde-88eed6008046 | -14.38895 | -52.52793 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 001a0a3a-53b3-38a7-ada2-ee5baabecaa7 | -18.25151 | -52.70906 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caccfee3-f4e2-3d04-a860-94a682817ae0 | -13.62442 | -51.82846 | 2026-09-01 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cd2f1b6-c155-3f61-b68e-9f02039e6db0 | -14.40451 | -52.49965 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 611a3645-1cf8-3dc4-aacf-a5128e05b12e | -14.71553 | -53.59166 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb85b953-c6ba-34e5-b7e1-4d509a104ced | -15.48797 | -56.01658 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a13a30a-453e-372f-971e-d918dee35b3d | -15.86777 | -56.48124 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2ab2398-d71e-38c8-9e36-c7e8eb73eba4 | -14.26485 | -52.86251 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4293e60e-7c8c-37a4-a679-1bd3b861306f | -14.25563 | -52.88916 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68a8d1b7-7a9a-3c1c-a2b0-786124027a1c | -14.41121 | -52.4959 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ceac7e10-ddb3-3529-9fa2-531f61bb0998 | -14.25869 | -52.87289 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1a6c1d8-6a36-3d80-a2e5-57362ff05adb | -14.41164 | -52.50313 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67d3b86b-9d6a-362a-88ff-e3d00f7d6cc4 | -14.42888 | -52.50708 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2731267c-d13e-36df-a25d-ad8497cee69e | -10.10204 | -68.40237 | 2026-09-01 05:38:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75e8ca4f-3d79-3443-b04f-697c9fac4840 | -14.26524 | -52.86914 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b45fd95-925a-3385-86fa-0437b11a8ed1 | -15.63713 | -56.37582 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d3d1fbf8-1849-3684-802c-082cae950fa6 | -14.39513 | -52.52886 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa4912a9-6956-39f1-a9e0-96acca7cc202 | -13.62379 | -51.83401 | 2026-09-01 05:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e55e670-5e74-339e-8d84-7c7612eacfd1 | -15.29992 | -53.19021 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceba5077-e96f-34d8-924f-9d8e116098bf | -14.42833 | -52.5122 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0dd3825-6396-34e0-828e-07fd8d85fb77 | -15.4401 | -52.68387 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e03653a-e6db-3360-a47c-a7b73630d3b8 | -13.32695 | -51.7294 | 2026-09-01 05:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d14f1ec4-6c4a-32fc-bb94-07fba7b8117c | -14.44746 | -52.50983 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb138c4e-6bcf-3360-b4cb-777e45149789 | -15.25976 | -53.88397 | 2026-09-01 05:38:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52c70d6-2f9c-3317-aad8-827c89bfb204 | -18.25038 | -52.73731 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f7dda6b-aab3-31b0-b2cb-5c81c070a83f | -15.29392 | -53.18938 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad19b13f-bfbe-33df-b62e-aaf2c7fde0b0 | -14.40151 | -52.48132 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c312f001-03fa-3113-8ec5-f6f8538812ab | -14.40771 | -52.4822 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 631c565e-1c86-3d16-85c6-18553c2d0f9f | -14.59026 | -54.12126 | 2026-09-01 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| daf32e58-6ad1-3ee6-8a8d-56050ab15f0c | -14.39194 | -52.51043 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96c5eb87-bedb-34ce-afd9-44cb8f995444 | -14.25775 | -52.87082 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1cc938f4-7291-37aa-9a78-35c35b80140d | -10.4402 | -67.84502 | 2026-09-01 05:38:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ff2efa5-51cf-3b78-9531-86736f0c02ba | -15.42871 | -52.68491 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01236eba-2fd3-3177-8392-1e758716c572 | -15.75725 | -56.1039 | 2026-09-01 05:38:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a984ac49-3837-3d68-982c-05ecefb01dab | -14.72129 | -53.59293 | 2026-09-01 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28d2ffb0-3ac0-3520-bbbe-7a65efa6793b | -16.04614 | -54.38902 | 2026-09-01 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 68ea6c30-079b-3a55-832a-451f86848230 | -14.25722 | -52.8754 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52549c49-2b01-3b44-b698-30fba693254d | -15.43544 | -52.68086 | 2026-09-01 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b82e4a4-e69a-3500-b88c-db0fd7e25051 | -13.32755 | -51.72381 | 2026-09-01 05:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ab0cb17-4ba0-3a24-ae9d-378eaaaf1eb8 | -14.39871 | -52.50617 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62e8a526-c43f-363b-8cda-fd611ff366a8 | -18.25481 | -52.74205 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 232ad445-601f-35bf-8c3f-abac3ea25139 | -15.63644 | -56.3814 | 2026-09-01 05:38:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 94a5857d-feab-38e8-a1ef-b403942593fd | -14.40604 | -52.49703 | 2026-09-01 05:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b0abe44-2f33-3c67-8461-38fe226fd44c | -18.25533 | -52.73658 | 2026-09-01 05:38:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README86.md)
