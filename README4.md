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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31d1c902-4008-3449-82b1-f837e45bab9b | -4.7929 | -49.5919 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 838f9063-59ac-3776-8764-e338602e3b8d | -3.3413 | -50.188099 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc492fcb-3806-321d-8bf0-a04576b7bac0 | -3.3306 | -50.0961 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ae1f3f-146e-31df-a3af-69da1945c69a | -2.436 | -49.3377 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8f1c75-0d1d-36c7-af87-585cc28fdea0 | -3.315 | -49.1245 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4bea167-93f4-3917-a5c4-0d2ea0a5bdc5 | -3.5395 | -49.429901 | 2025-11-08 00:17:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea2c577-2f5f-37a7-ad31-725df9765b7a | -21.060801 | -47.243 | 2025-11-08 00:17:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 92688c4c-9fe9-3cf4-a202-f2fbd831cbe4 | -3.7282 | -49.6698 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba058fd-9a0a-33ce-b907-ff890316cf83 | -3.5221 | -51.075199 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8bbfece-6d1a-36cf-a399-f2e0cf3cbc9a | -3.3247 | -53.351799 | 2025-11-08 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72f81ba2-c512-3987-90e6-6606d01cabad | -3.9773 | -46.015598 | 2025-11-08 00:17:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a939134-4580-31bc-bc39-729c533472b3 | -3.0149 | -49.435299 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655f0816-4e87-3884-9364-83d7a7cafb19 | -3.5334 | -51.0798 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c8657e-e961-319d-92bc-1f792038d9c9 | -4.3779 | -49.670799 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a18906-acb1-3869-893e-f5ba0b993585 | -3.3545 | -53.2094 | 2025-11-08 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9c115a-239d-38ff-b701-8808dcb83919 | -3.8537 | -47.389301 | 2025-11-08 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed3ee7db-e13e-34f4-8778-d44d5d2775fb | -3.8402 | -49.799099 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6df1a35-ca54-3f95-bfda-69d808f94024 | -3.6338 | -45.866901 | 2025-11-08 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e76f322-f2fa-39e2-895b-d6b15b3820ce | -3.7299 | -49.676899 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54b49222-63c9-356b-ab08-a4057e383053 | -0.5196 | -51.787102 | 2025-11-08 00:17:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f7ec3521-17bd-3b7c-978d-16c41ea01675 | -2.9323 | -48.758598 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1316981b-a50d-3a87-a96a-09bb249198c4 | -3.5248 | -47.527 | 2025-11-08 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f46ef3e5-26f9-3730-877c-c0596ea4ba66 | -3.1463 | -50.282501 | 2025-11-08 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a408a69-9f5e-38bc-96ba-cd08718e3469 | -4.3861 | -49.661598 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d18660ac-cd12-3cfc-8c4f-e4e316329f7d | -20.184601 | -47.378201 | 2025-11-08 00:17:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d116f9fc-1018-3650-b8da-26481731a9c5 | -3.4519 | -48.822498 | 2025-11-08 00:17:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae4d637-1e1b-3604-9f74-d3b0241a286c | -0.531 | -51.791698 | 2025-11-08 00:17:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 74f614af-6cfe-3022-a5fe-f1964087e6e0 | -3.8242 | -45.845001 | 2025-11-08 00:17:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0ea010-0530-3acc-a83f-34fa0c9a0ae6 | -2.0967 | -48.035702 | 2025-11-08 00:17:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4d17168-be1b-3e99-a132-120c7f3158d9 | -3.2906 | -45.322899 | 2025-11-08 00:17:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a46e1f33-6d71-3570-9d94-52f09b581bd6 | -3.3508 | -45.272598 | 2025-11-08 00:17:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3070908e-420b-3098-ad8e-8eb1413fefbd | -3.6457 | -50.257401 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67f6c723-d1fb-3435-9323-e1961cb7216a | -2.7077 | -49.5345 | 2025-11-08 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892d1da3-f212-341b-a693-bfb4d8e7c661 | -2.6154 | -49.2206 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf7294e-2e38-3a5d-ab22-666f1970c196 | -20.187799 | -47.392799 | 2025-11-08 00:17:00 | METOP-B | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3cfddfcb-e4e9-338a-bb8e-7c881aaf0259 | -1.4334 | -52.590302 | 2025-11-08 00:17:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74d64ce3-82f8-3949-93c8-e4d43b15184a | -3.0797 | -45.212502 | 2025-11-08 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 260c1e97-42d5-31af-a877-03fe3efed85c | -3.3298 | -52.550201 | 2025-11-08 00:17:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86624243-adc3-3d25-a928-e531e04f528f | -3.333 | -50.197201 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931e11bd-f372-3ed2-8fd0-8dc2c6e44803 | -3.5804 | -51.2416 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88c25b4-d78d-3afb-ad6b-c15c04b2dc3e | -3.4466 | -49.836201 | 2025-11-08 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34cc3262-6d7b-31a0-93fb-b3f6beef3cc6 | -3.8218 | -45.834599 | 2025-11-08 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cdc0c804-536f-3962-8421-c50053c93136 | -3.2835 | -44.459702 | 2025-11-08 00:17:00 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 670094f2-3f3c-3a43-b1eb-2450088e4cef | -3.3535 | -45.2841 | 2025-11-08 00:17:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4834704-5c43-321d-9683-7602a46f9efe | -2.7094 | -49.541599 | 2025-11-08 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ace1b5-9a30-3821-85c6-4a28bd108ff0 | -3.5789 | -51.234798 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60f032b-e57e-35c9-a8b8-d541b19a1ba8 | -3.834 | -45.842701 | 2025-11-08 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10e02334-fa67-32b7-ac2c-36e3289b7123 | -3.8459 | -47.400101 | 2025-11-08 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b5657d-8f46-34bd-8d83-2645ed8aa637 | -2.9807 | -48.699902 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46b6bdc2-b193-3924-ac35-cf0a4225da37 | -3.4077 | -45.427502 | 2025-11-08 00:17:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0be72a15-35d8-3d20-ab51-95fd04a00f17 | -3.4338 | -50.232498 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6104e8-f316-3352-a95b-0835ce98eb6f | -3.3993 | -50.262001 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a12bb45c-b4f0-3984-8bb9-08c8da503227 | -3.0574 | -45.029301 | 2025-11-08 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac1f4031-434f-3a08-9b7b-3951f326eb34 | -4.2761 | -48.326302 | 2025-11-08 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5a25731-76da-3533-b832-5798001678f8 | -3.3314 | -50.1903 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2935eea8-29e2-33f6-81c2-d2d3856ab71e | -3.8438 | -45.8405 | 2025-11-08 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0f407c2-2ea9-3ce2-b1c8-233a842800de | -3.3133 | -49.117199 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976a8f25-8a91-3637-b87c-ad8a4b16b90c | -3.0562 | -48.714699 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ecc555d-ab1a-3e60-b247-3eb7cdf70683 | -3.3952 | -45.418499 | 2025-11-08 00:17:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 650e41d1-bcb1-35ab-989b-9930c8bcbae3 | -3.1513 | -45.474899 | 2025-11-08 00:17:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b312ebb-0e63-3fbc-a78b-f493cdfa2b0e | -4.3553 | -50.6595 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05b607b-7bf7-34fa-b931-ba4957ffb08d | -3.5819 | -51.248501 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffba69f1-23e7-3fb0-b974-13511d5290ee | -3.657 | -50.2621 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179b70c1-8d02-3f88-87bd-91dc58d6ce60 | -2.9691 | -48.694599 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1433994a-b8f3-3207-91f7-06a7a88de590 | -3.9136 | -50.030701 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c430258-4adf-3585-adfc-6e7bad3c64b5 | -3.1333 | -49.096298 | 2025-11-08 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f957a45-600c-3177-9482-aeb051aa211c | -2.5214 | -49.440399 | 2025-11-08 00:17:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122a01fd-1442-3762-9189-e61a7c43188b | -3.3558 | -50.2066 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e93fb75-7cc1-3053-aaaf-a3d4a0a687a4 | -3.8417 | -49.806099 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed18189-f916-340b-a535-3524d2a72907 | -3.3447 | -53.211601 | 2025-11-08 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f234ad81-6ba1-3b78-bb4c-358d0222709e | -3.6472 | -50.264301 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5274e866-0c49-3d00-8b5a-0abc57a720fc | -3.0602 | -45.041401 | 2025-11-08 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3d0b65-c024-3d38-9ad8-3bb0332b0c7d | -4.3877 | -49.668598 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf3755e-7852-3a38-a4ea-c5e7776ead14 | -3.346 | -50.208801 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d295020-1f4c-3b7c-b275-05c0f05a064d | -3.2848 | -52.076199 | 2025-11-08 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f649d84-33fe-39d5-9273-153e220cb2e0 | -4.3763 | -49.663799 | 2025-11-08 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd5d5c1-eb59-35c0-a250-c5a83522571f | -3.4354 | -51.511501 | 2025-11-08 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2533534-af6a-3440-a103-ed294814526f | -2.934 | -48.766201 | 2025-11-08 00:17:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0f138b-7f54-3499-916f-6c29fbfa0352 | -3.916 | -50.994499 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58f88cf5-7433-32a8-a39e-c1f1bc6b1c96 | -4.1109 | -48.0121 | 2025-11-08 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58be6ab8-2466-3fd3-8a58-a298b90f7b34 | -3.4396 | -46.182201 | 2025-11-08 00:17:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6db7fd-87e4-38c9-a539-32eb9a6e979f | -0.5325 | -51.7985 | 2025-11-08 00:17:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7b077b13-17f1-3afb-9cda-26e9cef0bee1 | -3.9785 | -49.863201 | 2025-11-08 00:17:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 425dc8ee-d8b5-39c6-8c17-d33ae7d4de95 | -3.5236 | -51.082001 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf88cd2a-e287-3ba4-9f8d-10cdc674dd7c | -3.3291 | -50.089199 | 2025-11-08 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f7ebcd-e53a-3a97-bb09-0b39352c9506 | -3.8842 | -45.573299 | 2025-11-08 00:17:00 | METOP-B | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 027efd12-841c-3a54-8a91-6911e6d55105 | -4.4635 | -43.1919 | 2025-11-08 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3328780c-e3b6-3acc-925f-875fda532d38 | -4.6835 | -46.4074 | 2025-11-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 495.6 |
| 0e8ba266-bdc7-35ed-b2df-0d0a8aafb855 | -4.3927 | -45.3503 | 2025-11-08 00:20:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a5ee935a-e8d1-34fb-a06c-12efe5508919 | -8.0188 | -38.5211 | 2025-11-08 00:20:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 225.9 |
| 9017da17-80be-30d2-a5db-1348f8012739 | -3.4058 | -45.4424 | 2025-11-08 00:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 55650823-6ee8-39e7-8270-7c49ae125e0b | -4.6837 | -46.3852 | 2025-11-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 0bae0879-2fdb-3ea0-9db3-ecb05d5efa19 | -8.0375 | -38.5442 | 2025-11-08 00:20:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 185.7 |
| caa36b44-7d3b-3259-bdd9-cc46baacc8ed | -4.482 | -43.2141 | 2025-11-08 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 2fc51615-1cb0-33e4-9e27-c8504c659c16 | -4.7023 | -46.3842 | 2025-11-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cd4d12af-74c4-30fb-ba0b-ff99997feb3a | -20.1893 | -47.3735 | 2025-11-08 00:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 166.5 |
| ddf1ddf9-72a4-3187-92b2-4018b56d456d | -20.1886 | -47.397 | 2025-11-08 00:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 5fdd276e-89ba-3a98-876d-7285957fd3e3 | -4.7021 | -46.4064 | 2025-11-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 173.7 |
| eabf7218-bc06-3f93-b0fd-fabc4857be4c | -4.4633 | -43.2152 | 2025-11-08 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 230bf3fd-77b2-3050-b099-f590d0578da7 | -3.0731 | -45.0501 | 2025-11-08 00:20:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |


[Clique aqui para ver as próximas entradas](README5.md)
