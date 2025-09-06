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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aad0c037-6a1b-34b1-a532-21fe24b1b29d | -6.15535 | -43.16375 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a44594b-d2bc-3d04-a362-0d8a9536a157 | -6.8389 | -52.80819 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f010e70b-cc24-3fdf-92b7-c5d3156f85c7 | -5.73187 | -49.2912 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efeba14b-c229-3f17-969a-208c1e358bb3 | -8.88497 | -47.25293 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 242a118a-6e32-3b30-8bfd-7515e22e0e22 | -5.68378 | -46.34278 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12b7d6de-097a-3932-9aca-89cde0856e73 | -5.95619 | -53.79776 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81d98e6e-2e63-35d1-aa9c-f95151c2eb61 | -6.60539 | -43.97851 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c4b77cc-11fc-32f9-a42d-ea2210b9c093 | -6.4386 | -58.14675 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9deb963f-9ff4-3d2b-b7a0-0eb3921537cf | -7.69363 | -50.28807 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5cc1403-2548-3b5d-be5a-97979d5c24cc | -6.7832 | -52.80744 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e610c2e8-c515-3d3e-89ac-a4d090fc5a40 | -6.60285 | -43.96693 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a024364-06fa-357c-985d-60c6e1adcca3 | -6.27453 | -55.95584 | 2025-09-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6a5f16-5ffb-3b9f-80f0-a3a67328fe1a | -5.94558 | -46.1694 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bec3824c-683b-3ad6-b0fd-3b1c4bf67067 | -8.86553 | -47.91481 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f437cba7-a05b-3782-b214-234b0964ab21 | -5.94477 | -45.66523 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa1be5f0-7495-3e74-b9a7-e6e0a9c1ae20 | -5.20092 | -43.69366 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 949c73e4-5ba6-3d0d-9176-cc353c5ceba0 | -4.45335 | -44.13824 | 2025-09-06 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cddaa011-5387-33d1-980d-112d2e00e3d6 | -8.41918 | -47.32434 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 098a541c-8613-3f61-a5a0-1b2aa67e7f30 | -2.87694 | -49.4713 | 2025-09-06 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db2023d0-8aa3-3e7d-ab09-f3583e88d005 | -8.36811 | -52.56295 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a2134ad3-693e-37c4-a7dc-c854b7418d17 | -3.47134 | -52.76707 | 2025-09-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6247f1d-bd35-39ef-8c45-f4e7c3cb1d61 | -6.80856 | -52.81168 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b8c5262-d966-38ed-acee-4ad8431bdc93 | -5.90071 | -57.7276 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a675d2b1-76c3-33a3-9d40-940258280a60 | -5.86777 | -46.04314 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fef8703c-4526-3709-a345-d688c6daabba | -7.73277 | -50.31973 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1b634afb-1e0b-38bc-af40-c1d33da0f9c0 | -5.00827 | -56.03463 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ccb683f-2129-3143-91d1-f53d5a608d39 | -5.91466 | -52.2317 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39f4e7ae-baf3-3fbf-9e94-0ffc86e0e38e | -9.08809 | -47.01051 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d282998-b687-306b-ac92-1afb6024ce52 | -5.18467 | -43.04388 | 2025-09-06 04:38:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e5f191-d058-38a8-bcd7-bea70a35409c | -5.94923 | -53.79158 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 579cad03-3e97-3d8d-9c6a-75d06065b1bf | -6.20331 | -44.19176 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f81513fe-9612-3410-afbf-21c6c6fc081f | -8.36744 | -52.56701 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 821ad6c7-451e-3290-8270-d6ba61d5bd82 | -5.86171 | -46.10668 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ef927a-dea4-3cf8-80a7-d8e16435f92d | -3.96812 | -43.24011 | 2025-09-06 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c3b45b2-8f29-3827-b512-0df54f925585 | -3.37958 | -50.84951 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 243fd242-f86f-321f-8a5f-93df37f57e79 | -8.36208 | -48.2779 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e35dbdda-600b-3524-9d5c-7b9ba545ff00 | -5.9529 | -53.79925 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d9d4ed2-bd99-33f4-9442-2740f55721f4 | -6.88775 | -45.54639 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2392794f-9432-3ce0-a77c-63f3a581fb4a | -6.23227 | -43.28496 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580ed56a-7405-332c-b1f8-21b0d9549d7f | -4.56104 | -40.34519 | 2025-09-06 04:38:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2c8d0ec-4a52-36a8-8fb5-d660b5bece1b | -3.31618 | -48.71291 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7592519b-3379-344d-a4a6-a056733b22e5 | -5.98416 | -44.7273 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1e863854-ce69-385b-9005-c31352407629 | -6.98686 | -45.42508 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66972d49-1f05-3a63-a2e3-79be3252cd8a | -7.05608 | -50.85789 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6974b398-bf25-34e3-9875-52c54e0a6e9f | -7.23193 | -43.85864 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1144d8b1-fa51-39ed-ab7a-eb517b1f91a0 | -2.85477 | -49.50353 | 2025-09-06 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b825f102-5177-303d-b68b-4dd9672509d4 | -6.18286 | -51.49228 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92343393-48d9-34ab-88ae-4e75ed1cdf97 | -6.59158 | -44.54658 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9243eb3a-742c-3436-8e16-5a079a795df6 | -9.07831 | -50.42458 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19853f68-bd24-3ff7-94fb-6ccb44c35f6b | -3.36769 | -49.16157 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59a16dfb-ffa3-3d62-9744-807b69a1870e | -6.26843 | -53.44804 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69fde5b-41ae-39d8-9bf0-169dac900f2d | -4.99154 | -56.22057 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53bceb7d-9cdb-35eb-882e-db59808a103c | -6.26388 | -53.45202 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e27106-103e-3f91-831e-b9add04eccde | -7.33201 | -43.94153 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 307d95a3-3c5a-36d1-a8a5-594b418bbca4 | -8.07508 | -45.48661 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a6c7b69-dfda-3b98-b24c-e0f2307420a3 | -6.0334 | -43.70121 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 721b2432-896d-3fed-b718-1a5bf6f13eae | -6.27071 | -53.43429 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 968affef-aa08-3adf-870f-b33867bea918 | -6.27902 | -53.43097 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 050f2821-af68-381e-b198-86b685ebb486 | -5.37956 | -45.96206 | 2025-09-06 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1632fea-b47c-327f-b007-5e9b899042f0 | -7.41482 | -44.93806 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f5cefb6-feaa-3ed6-a8e1-b13427d329f2 | -6.53655 | -49.50704 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06274e45-a98e-3099-96f7-36ba04911414 | -7.42669 | -44.93989 | 2025-09-06 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4f263be-3694-37ed-8b46-601cff425528 | -6.1467 | -43.19237 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8e915aee-4e49-3a1c-ad2f-ff4cc31034cf | -6.2472 | -43.30421 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf6423c-0da4-39d7-8b15-d0d70d404824 | -3.25661 | -51.15284 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5201acea-019d-3363-86fd-db41a5fdadca | -6.24035 | -43.29043 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ed923f7-fa91-3753-a6eb-82e6216c30c3 | -6.01052 | -46.68876 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50a54bee-7ef4-302d-8b7b-a9e1357cd425 | -4.79628 | -47.26403 | 2025-09-06 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c19ce70-18e1-379b-9045-22eda736f8ab | -6.23252 | -42.6341 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9b38ce8b-2154-39d2-b35b-386d2ae29e85 | -7.30154 | -43.72838 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37434226-f92f-33e8-bc47-05e6e873841c | -7.5873 | -49.28252 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e3b34ed-72eb-3e7c-81e1-539575a94ded | -8.06469 | -52.3814 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4a2038d-f4a0-3792-865b-24613e36fdee | -5.90895 | -51.71024 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3a5e0f-1c6d-3fa7-8195-2be5b59af241 | -6.18523 | -53.24887 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 767b97d1-fdbf-371d-94a3-6e4e3be6581a | -5.92724 | -52.0005 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e64d01b6-9d67-3671-8316-9f1d2c844543 | -5.95389 | -53.78738 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70f3b22d-f15a-3134-8b73-9153b1128e0b | -8.77117 | -49.63696 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 826f70aa-fecc-3588-bec8-d652fc2be461 | -8.67629 | -47.43837 | 2025-09-06 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe385f4c-e354-3437-9344-a68cf8ed0bab | -6.20772 | -43.36272 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e52a5c5-9847-37c4-acaa-3e5dec959441 | -6.15789 | -43.17694 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2fd22c8-b113-32b2-b930-8af1b364e616 | -6.20692 | -43.57845 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76c7b8e-b4ed-30e8-ba1d-a1ced48b3baf | -7.73058 | -50.31218 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3730b08a-2652-319f-82b6-617f5c287ae7 | -6.23719 | -43.2816 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0643037f-efad-33b2-845f-f1a17e9b5c60 | -5.72467 | -43.91858 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d31ebe7-cf4e-3c70-b1f9-ad94b4b31ae8 | -4.22304 | -47.2113 | 2025-09-06 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22c01773-0a83-3f67-9f4e-379352fd149d | -6.15415 | -43.17196 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3003904-c162-339e-9b03-a2ae5b176c34 | -8.45246 | -45.03665 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 448a1f32-3092-3deb-9c9d-01935e118648 | -6.01178 | -43.70195 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abf300d7-2fae-31e2-aa55-f879797e323e | -5.95348 | -44.74611 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f154f509-3f1e-3dde-bcd0-f18900494e1c | -3.24729 | -50.79795 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4e22ca8-5bb4-3e51-b33a-528f411b5b13 | -6.27297 | -53.44407 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a690016f-7ed9-3b9a-aac3-e07e3242f18f | -7.72781 | -50.30819 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fb4825d-5a83-3809-8ae0-91babbc9d94a | -6.1578 | -44.24679 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5830226-fedb-3179-8748-4c981e039ffc | -5.90577 | -57.7284 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ed09e96-503c-31e8-839c-54049dbb99f4 | -9.08935 | -47.0022 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66d061c0-f902-33e3-9e69-3095c96a9d32 | -5.97594 | -53.60278 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3e963d1-3486-3921-8528-3dee66755b49 | -7.3321 | -48.50463 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e45b13f-e01e-3a4c-bdb1-f11d650bc8a3 | -5.37892 | -45.9663 | 2025-09-06 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872a9d40-79ff-30c4-98af-cd3cccef215f | -7.21305 | -43.98912 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea5624a-962a-390b-b197-07b1694da128 | -9.08337 | -46.99311 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README54.md)
