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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f2f7f8d-d9d6-379a-a94a-ac882927f14e | -2.79502 | -50.28517 | 2024-10-04 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc616272-4a8c-3923-b902-5a28c9d6f955 | -5.02109 | -49.76846 | 2024-10-04 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 96f8bd0b-fa97-3313-b47b-46f479a79814 | -5.02057 | -49.77144 | 2024-10-04 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f90729e2-c2c3-3aec-a2ff-dc7f6ec401e5 | -5.01789 | -49.77003 | 2024-10-04 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30c08338-0c35-3e09-899a-651b198e5de4 | -5.01738 | -49.77306 | 2024-10-04 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edb7d72d-4a67-383b-9286-6f87d56b288a | -4.66098 | -50.88427 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3930b03-6398-3904-b567-4955b6230619 | -4.65543 | -49.53202 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 687dbd8c-d5d9-3065-a432-f4d5c24e1195 | -4.65493 | -49.53491 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2db3f193-8f1c-39d1-88ee-e7acbdabe59f | -4.45544 | -49.62127 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3b75c15-d471-39b2-88ea-43b3a257eee1 | -4.45033 | -49.6204 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cdebc76a-0093-392a-aef7-d89becea7cb1 | -4.38261 | -50.42591 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b9f8ef3-42a9-38d8-a0aa-4456cbbbc844 | -4.38202 | -50.42932 | 2024-10-04 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e61fbe0e-aee9-3282-976d-81b059d0eaf6 | -3.84503 | -49.39635 | 2024-10-04 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 014daefd-12a5-32ac-9801-316794cce3c0 | -7.8355 | -50.52615 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93a87947-06c8-32f9-8743-a7a60a0758b0 | -7.83496 | -50.52917 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ccc50f-d7b2-3a3e-8a4b-275900590f57 | -7.83441 | -50.5322 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddabbae1-31d8-33c9-8177-3cc579a0a0ff | -7.83333 | -50.53822 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9b3be1-03f4-3c9b-b03e-29c1cef08940 | -7.83095 | -50.52207 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5077d39-2ef1-39b7-b9de-0ebb51880520 | -7.8304 | -50.52509 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6e314653-42b5-37fd-8600-6d73b3b32ced | -7.82986 | -50.52809 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 46b4a64b-f8b3-3d99-9b16-7cb7b0bb043b | -7.82932 | -50.53109 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e5ae9a8e-321b-317d-ac34-392a36b02cc3 | -7.82877 | -50.5341 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 978897c5-6bdb-39b5-93d3-df35c8c745a6 | -7.82823 | -50.53711 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4878cb4-f8c7-3323-8338-3089de3f284d | -7.82257 | -50.53909 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a5d346b-4b84-3d7c-8b7c-1e7d446a7c0f | -7.82017 | -50.52309 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aea0f693-0f89-3156-8add-73c646762c71 | -7.81965 | -50.526 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17521a25-3448-31c6-bb7d-5d21f8546626 | -7.81911 | -50.52894 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61446ce0-2ee1-3d24-92b1-30d707fae58c | -7.81856 | -50.53199 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1070328-7a3d-3ea6-aceb-dc7b30789635 | -7.81454 | -50.52494 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac7608e8-1b04-3e3b-9139-081c7848dfb9 | -9.11685 | -51.52012 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2033cd13-14e4-3574-80d4-b5f76ca74d5e | -9.1121 | -51.5158 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 504a95c2-a996-30ef-823f-1be69e595a51 | -9.11152 | -51.519 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dee7f02d-0437-394d-804a-e0db825fd94d | -9.11092 | -51.52228 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c89e08-14ce-3c2e-b8f3-1e9ace7408f9 | -9.11031 | -51.52561 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c228b9ef-66c3-3f7c-9589-79890b7f9669 | -9.10914 | -51.53204 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06c28600-0573-34ad-a468-3ef558e279e4 | -9.10857 | -51.53518 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75949429-80bc-367e-b5f9-f7086c2bb4f9 | -9.10738 | -50.91514 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69412f1d-ae33-3cba-8964-8006bc6a5376 | -9.10682 | -50.9183 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e0d6176-4626-33e1-84b6-fd047c8637b7 | -9.1055 | -51.52165 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff9ad866-cb7a-36e5-a384-0411e8f42043 | -9.10491 | -51.52484 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d2619e3-4b1b-3422-a57e-3e0bcbf7e0c6 | -9.10433 | -51.52802 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 090f0fef-fe02-3d4f-970f-c86cb3decef2 | -9.10374 | -51.53124 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eabef97e-4461-36bf-bdfe-26cfaf4b3af4 | -9.10314 | -51.53452 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01731a54-e330-3f23-b322-32ec8d36d894 | -9.10279 | -50.91112 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0a27e76-10d4-39a0-ab10-4f5dca01791f | -9.10223 | -50.91424 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c698437e-d074-3f0f-9b71-df10d82ed283 | -9.09934 | -50.90083 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7998da35-2937-348f-a18c-cf9bade560a9 | -9.09878 | -50.90394 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 916eee08-3b0a-35a9-811c-3aa59b05df6f | -9.09821 | -50.90705 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 621417e9-4ccd-3fac-82cc-0456b05b84b8 | -9.09765 | -50.91018 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40ff6738-f1a0-317a-b80b-ad2cc30ead1c | -9.09708 | -50.91328 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f36262bf-9f02-3b4b-924c-55d8a8388f10 | -9.09419 | -50.89991 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8d3abbc-aff0-3ffc-8655-1e7c262b9372 | -9.09362 | -50.90303 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a563b9e4-3e69-3e6a-9e4f-7d944c8b3150 | -9.09306 | -50.90615 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e690c519-81ee-3537-9565-8e1727cd112d | -8.35252 | -50.86982 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6437944c-907a-3a5e-88c1-23fc59f2cf40 | -8.35193 | -50.87311 | 2024-10-04 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0db48b1e-3d26-3fb5-938d-1e348218f6f9 | -8.17229 | -50.49076 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4c5a519-3144-3310-acd6-d297944ec3fa | -8.16667 | -50.49282 | 2024-10-04 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 346abd8c-eb5d-342f-85e6-63282e7ee23f | -8.02203 | -50.90214 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3d76f421-6271-3644-8236-db633b979e8d | -9.32458 | -51.12385 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 267f7c1d-fb7a-34e2-928c-e8b9e5172b11 | -9.32398 | -51.12704 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70fcfe61-e93c-353e-a5b8-800b3e7c71b4 | -9.32338 | -51.13023 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2885182-8ea0-3929-8f09-31d4b30d8db8 | -9.32219 | -51.13663 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03967147-276e-3b0e-bc82-968d0308754b | -9.32158 | -51.13985 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b61b4d1d-bff7-36a1-bac8-cde7294df621 | -9.32095 | -51.13929 | 2024-10-04 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49587fd7-e79c-361f-aabc-f815875df6da | -9.36991 | -50.74806 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91c24d7b-9f59-3e9d-86d5-130bdf8f4c7b | -9.36938 | -50.75101 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50bb201f-2997-30c7-b6a2-c4f8d5c50094 | -9.36885 | -50.75398 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30976e4b-1bb4-39f7-a732-be7bc3438eca | -9.36433 | -50.74997 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbefe5dc-6544-3a0d-94a8-44cd8ed0eb44 | -9.36379 | -50.75298 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfdad0e8-9ef9-36f8-b79f-36ed8921f3d1 | -9.33521 | -50.79494 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5327b6f3-f65c-39ec-9db5-989000001fda | -9.33465 | -50.79799 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 54832d1a-67b9-32ce-917d-a9e28a2b18f3 | -9.3341 | -50.80101 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f834a2ce-bd15-34f7-baa0-699d082f3b1a | -9.33355 | -50.80404 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ca6c9283-5621-3413-89cc-e1c6f51e84ba | -9.3307 | -50.79083 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 99d351cc-cd1e-30d7-aede-6ac2e8304374 | -9.33014 | -50.7939 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c3e05060-deae-3dd2-a10d-ad962345da12 | -9.32958 | -50.79697 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 94d9de7d-084f-337b-a7a7-5c6becdaf75d | -9.32903 | -50.79998 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3ef979e9-767e-3a67-bf7a-357bc0c3e391 | -9.32849 | -50.80295 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 940f98ab-d5c0-34c0-a69b-97dc6447d409 | -9.32795 | -50.80593 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 21919b96-86a1-3266-bb12-8c4d697722bd | -9.3274 | -50.80896 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8ed0bcef-c7ee-3dc3-be57-a1bd5c7a7b6b | -9.32684 | -50.81202 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ecf21d1-7117-396b-8fd7-8c2cfc854c42 | -9.32618 | -50.78675 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cde966a8-2953-3a71-8536-0f03268438ab | -9.32563 | -50.7898 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e52d59db-0003-3934-877d-f27543660c24 | -9.32508 | -50.79279 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c2db0d5d-bfd0-32d5-9880-39b4451d6324 | -9.32455 | -50.79574 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bc3e746a-d56b-3083-aacc-f1300886175f | -9.32402 | -50.79861 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 0fdec4ac-44d5-3c94-9ba3-1b0029065fa8 | -9.3235 | -50.80145 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ece249ad-8c9d-3a15-8eb4-0531e312a676 | -9.32297 | -50.80436 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6e2b1164-b3ba-398f-9cb7-70ee2575e7e6 | -9.3224 | -50.80751 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ffbbf666-cb56-367c-87da-8349fbd5feac | -9.3218 | -50.81079 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 727d4e7b-068a-32e1-8197-c408b06fdb9a | -9.32122 | -50.81396 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff574ac7-d08f-36c5-9d46-f0e04535b45d | -9.32067 | -50.81701 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17bfa0e7-4e4c-35b9-8329-443741a43b3d | -9.32055 | -50.78883 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ea62110-0f12-358e-8b10-fca724cedcef | -9.32002 | -50.79174 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f72b2156-129f-35a6-8bc4-ba42a532a906 | -9.31948 | -50.79466 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea723435-0154-3d41-a3f0-c5b99c13c7a1 | -9.31896 | -50.7975 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ddf4301b-a895-30fc-a165-da98d0cb2d61 | -9.31845 | -50.80029 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6bf6e67d-d225-32bc-8743-3581e249f2fe | -9.31794 | -50.80313 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a19b5453-154b-34e2-9aa2-1ffa37089fc6 | -9.31737 | -50.80625 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2535103e-8922-3b11-a2cf-ca5a26f58471 | -9.31675 | -50.80963 | 2024-10-04 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README66.md)
