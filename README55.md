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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68d67d26-28b9-30db-abc5-450481d89b20 | -5.75528 | -43.13262 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b339e629-8e42-38f3-814a-2a1c82e0ef48 | -3.73452 | -49.05359 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ed34e1a-c3ae-3d25-b6f7-b62254d71685 | -6.80652 | -45.65224 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c97f0801-13c2-3853-b75a-29fc0d9f6706 | -5.72738 | -45.36894 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fd4ca73-60d6-3338-8cad-69ed599670bf | -6.53764 | -49.50012 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12fe7306-08ab-32de-81dc-34d941d66a8b | -6.42484 | -45.89492 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4320e1da-1eb3-31fd-93c4-fc0d6a7ff521 | -5.87045 | -52.17113 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd4b4a0-0d01-30eb-87c8-e741cf05ad9a | -6.20284 | -45.49943 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ca1c437-7661-3051-8f73-5ee151196955 | -5.71726 | -43.94003 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8095e60c-311c-3c52-bfce-4190a6ecaaae | -6.84321 | -52.80457 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ab1772-3204-3e00-a31e-92e4d359b50a | -8.4444 | -47.3241 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bca15c8a-57e6-3734-911a-e5465abae500 | -3.69404 | -49.54647 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d282b626-ca1e-3a00-b8a4-98d88e6f9499 | -7.20448 | -46.19768 | 2025-09-06 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8341150-00d5-37d4-b566-54f98e3eef77 | -6.51556 | -43.06717 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe05c6ce-e9db-3a95-a247-d2cbbcafa193 | -4.9988 | -56.25502 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d06f75d0-b1a0-3c63-ac46-7616a8c1b069 | -8.43502 | -47.31468 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb02c38d-229d-3e5c-858a-fd2da52369a5 | -4.64533 | -46.37195 | 2025-09-06 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b88cccd7-66e4-3378-89e2-9dc430b98181 | -5.90625 | -57.72557 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8cead82-7b61-3042-9033-947cfbbe04ae | -5.92355 | -47.28688 | 2025-09-06 04:38:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aa17d31-cfa3-301c-af58-ba291a3786ad | -6.53986 | -49.50756 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87bf4ca1-493e-3757-b5be-06112765fa84 | -9.82736 | -46.53038 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05cfa0fb-d31e-3d35-8905-d152e6717489 | -5.92788 | -51.99665 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8c377a2-e0a8-341e-832d-80ac152e54e0 | -2.65709 | -48.79937 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70eb329-666d-3db2-911f-b7a158ddaecb | -5.98243 | -53.60122 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a966378-2dfb-39c3-98ab-1f2724e093ed | -6.8756 | -52.78818 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d2d264d-30e4-3a25-a751-c4eb35b938c5 | -2.34149 | -47.58929 | 2025-09-06 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b22fc7a-661d-32a5-a88c-a5e8a42bb333 | -6.55487 | -42.95479 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc47d63a-8c88-3c72-ba03-28ac36390447 | -3.30241 | -48.71429 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f336cbf3-da5a-303c-8661-7456e0590b3c | -7.34355 | -43.95117 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3fabcb4a-b932-3c31-a951-f0fa820855c9 | -8.45644 | -45.0373 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e067c40f-9139-3bbb-8c68-913a502b18e1 | -5.40227 | -42.32349 | 2025-09-06 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8cdcb5d-a62e-303e-8f1b-7113e80e001b | -6.16315 | -52.44601 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4ba2a1a-cd49-35f8-af53-1403c0b6ef88 | -6.08134 | -43.30662 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ceee2ca4-8e7d-3f81-934b-a0658cc4a636 | -4.8572 | -42.73685 | 2025-09-06 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1dbfe29-d23f-3901-bc0b-b4e70ef5abef | -5.6528 | -43.61658 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71bb8962-f074-3d7d-98e2-2a0a05b914d1 | -6.28204 | -53.43616 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7acec6b1-f15a-3920-a8de-00546464ae64 | -3.35883 | -43.37418 | 2025-09-06 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23d91f2b-7407-339e-8711-f5b4b7c89ce9 | -5.92547 | -43.01492 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb8aab2c-d5d7-3472-9674-6114182467a5 | -5.20149 | -43.68982 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb688cbe-66ef-3028-82cc-fd4e888e1bef | -8.06118 | -52.38089 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5adc8b02-6fdc-321c-8694-9c4e48ee60d9 | -5.89412 | -57.73565 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d962efbe-5c6b-313e-9916-1e527438b34b | -6.91405 | -44.16636 | 2025-09-06 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd3770ae-08b3-3e97-9e82-6a5cb772ecdb | -7.25847 | -41.89268 | 2025-09-06 04:38:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 665e33b4-3ef7-355f-8d0f-e24011a6521e | -5.70472 | -53.69208 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b10d37-f0f3-3cc4-90d7-834f7f6a4734 | -6.83528 | -52.80758 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abac2936-52da-312e-925c-0ed71965d5a0 | -3.32111 | -48.70311 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d5d4a3c-e2d7-39f9-8357-40c5f4486bf4 | -8.35869 | -48.27736 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3dfc427a-9c0b-3491-9783-4ee68b610190 | -5.70993 | -45.14835 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6b4d6a2-7753-312e-9c6c-51f57641f83e | -7.7636 | -50.74182 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ca12f879-7a88-3c53-b7e1-b6100e03c5d5 | -3.32057 | -48.70655 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c68f1443-cae2-38f1-b6d2-42f9cdb8c580 | -4.79969 | -47.2646 | 2025-09-06 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7074c7bf-387d-3952-8183-21e8109a1522 | -5.95424 | -44.74108 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caea63ef-5bf9-3313-ae14-f8712cda5830 | -2.60537 | -48.13526 | 2025-09-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3212920c-0648-3074-a23e-e1cfc27a43bb | -7.29872 | -43.72926 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 262e8ef2-1386-3744-aff4-43f5719c0db8 | -5.92738 | -51.99718 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18db872c-36da-30ce-9a9e-5b7c318b0153 | -5.94984 | -53.79376 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d80c979-8d19-3e40-b24e-d444956cb380 | -6.3637 | -44.68077 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b9b72bb-6192-3702-83f6-b574789f502d | -5.99562 | -44.16327 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 432758bc-8fc3-3f90-9b3d-9615fe8feabe | -7.23618 | -43.85919 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c669eea2-bb38-3d37-8c52-920bd4935eb1 | -4.98525 | -42.06781 | 2025-09-06 04:38:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dab2e339-0bec-3ee2-97c8-03e08fc9e9ff | -5.81411 | -47.79131 | 2025-09-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e2e444d-5ff1-3ae6-be09-69030b9fcc0e | -2.5148 | -51.91629 | 2025-09-06 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88c0ae97-e2a3-3033-a0e0-32a04b7ef41a | -8.90784 | -45.81397 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72784a06-7180-362d-81d8-7a62a302f44b | -5.6576 | -43.61324 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6416191-2943-3b8f-a654-4cb63795b03a | -8.83829 | -52.00936 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6dbd774-79b8-3c4b-9914-3551bdad0f71 | -5.96696 | -44.73505 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75d4d84-c727-3768-bff7-34186fc891ad | -4.37572 | -48.06594 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a81661d-90a4-3d71-ac65-d0e9e74a6f49 | -7.04937 | -50.85688 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5b70639-f5b4-3bef-8a1f-3d907b9d1ba0 | -5.94678 | -45.66351 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74659633-60a5-32aa-b403-9ea0f0651332 | -6.55172 | -42.94523 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5469f1ee-c513-3875-a168-33b3ef00e286 | -6.60847 | -43.98642 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e0dbeed-cd22-3d98-aa95-ab9a4cc8d052 | -8.34125 | -47.47803 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6868dff-5b22-34c6-ba0c-8c47d19d2f6f | -6.26285 | -43.49581 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceec0f87-d70f-3dbd-80c0-532c308ca032 | -5.0688 | -56.06743 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21cfbf77-e2fd-3866-8b2c-1aed8b753a9e | -4.03475 | -42.52053 | 2025-09-06 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ad873451-b751-3474-83b5-331b64b9cf49 | -6.27223 | -53.42512 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc491e12-091f-35ae-8a43-bf68a640ef49 | -7.38066 | -50.91011 | 2025-09-06 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c7d7a5-09a1-3616-8ffd-7d9414e5194d | -6.73024 | -51.9642 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e19930b-eee2-3524-a393-eaae04435791 | -6.51489 | -43.07172 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58ca3d40-d213-3e4c-a124-e9b15fc5a483 | -6.22275 | -42.63743 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b3d768c0-53e7-3302-93bd-02b7a87d6660 | -3.75383 | -49.06014 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d607b3bf-646d-3b8b-8134-335d076920d3 | -6.20386 | -44.18805 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79ba959f-0986-3625-96b7-89fc39c1c043 | -5.88974 | -43.64931 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26d073f1-fd50-31bf-b45a-256ae21d7856 | -6.9135 | -44.17008 | 2025-09-06 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed19e353-c1dd-3846-bd42-b72b588083a7 | -7.78454 | -50.97457 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b934f471-2197-30fe-9047-0116be3f2896 | -6.30805 | -44.57536 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 534d2743-d3ba-3671-8c48-fbf687dd1ece | -6.87489 | -45.5547 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 94a1221b-6f34-3e81-9de3-444784112e48 | -3.37981 | -47.61301 | 2025-09-06 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d527f79-fd1b-39c1-895e-32caeb7e8348 | -7.07505 | -43.86957 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| feddb9b8-6f43-330b-948a-249441bf5168 | -6.20019 | -53.25132 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a0c5be7-7e50-3556-b1cf-5f923520a3a1 | -6.26766 | -53.45266 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba816e26-b9d5-3b86-b094-c2c880c987bf | -5.46804 | -44.13437 | 2025-09-06 04:38:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b37c5823-9b77-3f4a-a08c-5dc2c219ac24 | -3.37614 | -50.84896 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c673bdf6-287b-3845-968c-c9811e984d45 | -6.82804 | -52.80633 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6be51d0-8d95-3572-a948-96d9a4f81591 | -5.94744 | -45.65905 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f0c696-7817-32dc-bcba-3628172794c7 | -7.72503 | -50.32563 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ec3d781-dfbb-3755-8f7c-e942164b8c8d | -9.8157 | -46.50567 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df3f9307-7ef6-3e09-b99d-d79b27dd25f3 | -7.81569 | -47.50824 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e981590-3ae5-3efa-a19e-da5d380d21b8 | -7.5915 | -46.21064 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2514191-d22d-325b-8735-607db7ca485b | -8.35074 | -52.51517 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README56.md)
