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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11f113d9-d2bd-349f-92b0-1005c8b265e6 | -5.61571 | -41.12447 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| abb6d0d5-4577-39e4-828e-0148ce2c0330 | -3.25156 | -50.12825 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86af1ea6-df5b-31fb-86b6-66503e49f287 | -6.99399 | -38.0523 | 2025-10-23 04:06:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 410c61b8-b698-3a98-9df3-f952c0547f28 | -0.26446 | -48.47017 | 2025-10-23 04:06:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e19bbf5-b873-37a4-a3ab-2ca94f1cdca8 | -3.81395 | -50.76942 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aae8f30f-b7fc-3922-a441-d4041105eae6 | -6.30947 | -41.8844 | 2025-10-23 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e899d79-62a9-3f3a-aaa9-0f1b71be4c69 | -2.31127 | -46.99194 | 2025-10-23 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23c0eec3-f70b-32cf-b0fc-d96f59fac7ac | -4.7064 | -48.12737 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f92cfd14-a0b0-3371-939b-3f09a37434bd | -3.25098 | -50.13173 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3df1ce8c-9bdf-3067-97c4-e79fe3464392 | -3.84832 | -43.96066 | 2025-10-23 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6e38edd-8ce9-3cbc-b7d5-2c840e565688 | -3.48518 | -43.98285 | 2025-10-23 04:06:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14d50cdd-5690-3ed5-83d9-630afb05b54b | -4.27979 | -48.19303 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7662e842-c0db-3366-a969-59cb263d14c3 | -3.35312 | -40.42329 | 2025-10-23 04:06:00 | NOAA-21 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 127d81c1-182e-3fb9-984c-2ad2d799954b | -3.11428 | -51.20575 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57af48bd-8e6f-35eb-bab9-bf3d8decec82 | -6.32597 | -43.63255 | 2025-10-23 04:06:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19fc70d3-c50b-3347-836a-ef67b4203cd7 | -4.70612 | -48.1246 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4db19207-c000-3bf3-9172-4532d0f7b977 | -3.6765 | -47.62609 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 63cc85dc-31ec-3189-9f99-4cbed2ef26ec | -3.21385 | -46.80618 | 2025-10-23 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2bb4bc0-cb98-3435-bebb-fb40e60b25bb | -2.42754 | -49.2691 | 2025-10-23 04:06:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3eeed8d9-2d19-31c3-9f37-aa47675ac6e6 | -3.85523 | -40.73791 | 2025-10-23 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08365d62-1144-332b-8098-d03d39f920a3 | -6.32033 | -43.62377 | 2025-10-23 04:06:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 987f7af3-2ea6-3ad5-bae3-3567ea8b2488 | -4.87129 | -42.73301 | 2025-10-23 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cb703a3-536a-3663-88d0-726acd45c83c | -3.81198 | -50.77053 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb6f722e-db38-379d-8bee-2f76359bbb7e | -5.55919 | -47.01565 | 2025-10-23 04:06:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 680ee64b-ad85-328e-b735-eff8becc6612 | -3.01856 | -49.48172 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2639779c-aa2e-3c5e-b14d-80965056a269 | -2.92695 | -48.30524 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b25f7de0-f130-333e-a6ee-c2b5f3187990 | -5.6463 | -40.64167 | 2025-10-23 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd5a8f0e-d6ac-3f76-ba6e-bf22bea888d4 | -6.30287 | -41.88336 | 2025-10-23 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2d8e0b49-18f9-3bce-994a-8bdf5e65f930 | -4.94022 | -48.30348 | 2025-10-23 04:06:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ca5a4cc-355d-3595-a89b-eaea69dd6212 | -5.85321 | -43.64901 | 2025-10-23 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d34e5c0c-56c1-3108-87d1-0a3a5dcf3244 | -7.01916 | -38.83126 | 2025-10-23 04:06:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f3ba38d-6ae1-3a25-b360-16438e348898 | -6.01334 | -43.32604 | 2025-10-23 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7692ef6d-40cd-3ad0-9ba0-bdad70240491 | -4.91343 | -47.32574 | 2025-10-23 04:06:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6759ec8-2c40-3062-b17f-cc2176306b3c | -3.66946 | -39.48438 | 2025-10-23 04:06:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7678b50c-9855-38c6-95e7-5ee8c956464d | -2.25347 | -51.92393 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3770b2c8-2be7-31b1-888f-a2e490956ec4 | -3.21452 | -46.80209 | 2025-10-23 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62f266e4-2ffb-3f58-abaf-ed6b37d081af | -4.29223 | -49.27579 | 2025-10-23 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f053a8-a05f-3c1e-a65c-a4390461dd4d | -4.70902 | -47.99567 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f618622b-f2d7-383e-9d89-92e2e6941e2d | -4.11834 | -42.18102 | 2025-10-23 04:06:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01f37516-c145-3bd7-a1da-b178813f14f5 | -4.78455 | -42.97055 | 2025-10-23 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c659a33-3036-305d-9450-34429537cb12 | -4.70721 | -48.12235 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83131b7b-239b-3d1d-b035-8c2061f56a50 | -3.76369 | -48.92571 | 2025-10-23 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a1dd7f1-a456-39f6-b35e-88a1f631d678 | -2.73264 | -48.29048 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc0b4a43-96cd-3950-b109-e718edd5fb9f | -3.01859 | -49.44928 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b290ee66-5eb5-3e90-8764-7c95103b5989 | -2.80842 | -50.2728 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59817df3-92d9-3800-9319-ecabceb45095 | -2.73746 | -48.29126 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b0f7f80c-5c16-3f27-b560-429e0ec574a6 | -3.14877 | -50.16537 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0176b7ce-7b54-36b0-af23-5c65e05eef7c | -3.98861 | -39.30952 | 2025-10-23 04:06:00 | NOAA-21 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 13f4040f-19d0-333a-b757-c42b1469f802 | -4.37782 | -50.3512 | 2025-10-23 04:06:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41126e77-7115-3ee1-8b83-1ae789008fc9 | -3.70002 | -49.56528 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9273a9cd-16d8-341e-a436-b8f4860e02d2 | -2.44304 | -49.37173 | 2025-10-23 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec87c014-6b07-3422-9ef3-64ba15886ab6 | -2.73659 | -48.29649 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bf07590-c968-33cd-a332-b787328aa06e | -2.8721 | -50.71704 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 763f1607-cb13-3824-970b-4ba42b64c411 | -3.88443 | -38.43391 | 2025-10-23 04:06:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1f2bd20e-31e0-331d-9043-d4d3a7000fe1 | -2.9271 | -48.30708 | 2025-10-23 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7c6b2ef9-5662-32cf-b682-f1f101b55cbd | -3.67576 | -47.63066 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8e6442a3-db69-3b90-9e92-4b9602e86e93 | -6.32473 | -43.74947 | 2025-10-23 04:06:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ba49eb3-6480-3fc2-9892-ad882c956502 | -4.63744 | -42.52966 | 2025-10-23 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 340055fb-07b1-3c0c-b4c2-dcb329b87c85 | -3.15364 | -50.16969 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 464e929c-f1c5-3720-975a-ab404a491a7d | -4.32709 | -46.7961 | 2025-10-23 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad0afb40-4b38-394b-aa1e-9018563ab8e8 | -4.71522 | -40.58763 | 2025-10-23 04:06:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d2c96d5e-d23b-3a43-8f49-126f3989d32c | -4.77885 | -40.92599 | 2025-10-23 04:06:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96e73a1b-c9e4-304d-85d0-1ecb253e02de | -3.02377 | -49.48254 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| b12fce7f-3c84-3ef0-8873-2823428404ba | -3.79931 | -48.99427 | 2025-10-23 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1125e853-6ab5-3190-bb55-978d8a2b1c87 | -3.83308 | -51.30193 | 2025-10-23 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e25564e-9dfc-3ac2-aa4e-4613e1bb028b | -2.86002 | -50.73606 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0b2de3b-2c0f-3c7c-9a6e-11e1d31f718e | -2.44253 | -49.37491 | 2025-10-23 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2888f81-4fb9-311e-93b7-2c93c66482cb | -3.9528 | -40.93926 | 2025-10-23 04:06:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 694a543a-c4b3-36e0-b397-afcaf2238577 | -3.99631 | -43.28326 | 2025-10-23 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27346573-e73d-3cec-8201-1f3eea29f956 | -5.91403 | -43.31039 | 2025-10-23 04:06:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 738fc51f-66d0-3d9c-a735-02c03d129906 | -2.90285 | -49.40084 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11a555cf-44ca-3a94-ab01-5754b74df5ce | -5.88714 | -46.28543 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f154ba4e-c7dd-331c-bd9a-423af60a63eb | -3.70183 | -49.56496 | 2025-10-23 04:06:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 383ab848-7cf3-3bc6-a305-4556c3743e4a | -3.95049 | -46.9721 | 2025-10-23 04:06:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18984ffc-a45b-377a-ab92-9628be1db3f7 | -3.0295 | -49.48023 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 6de567d4-4a77-3995-9bc0-1f276b48a3f7 | -3.92961 | -47.69511 | 2025-10-23 04:06:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a83de01-2e99-3b1e-b34c-aa3ae565bd62 | -3.02378 | -49.45012 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f4410ec-ed23-3e71-b980-8cf9ee33b73b | -3.8113 | -50.77441 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 239357b2-79c5-32f0-b359-91bc4ee9e340 | -2.8587 | -50.74381 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f00ff4e-2d81-3233-a119-aa2a3a722b2c | -5.54429 | -41.3596 | 2025-10-23 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7f80758-e3f6-3eee-b131-bf378ced4e79 | -6.32535 | -43.74563 | 2025-10-23 04:06:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 318e3660-3b18-351b-975c-aa96e047185c | -4.81384 | -48.64505 | 2025-10-23 04:06:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6437c60c-374c-37da-b2fe-7524758ff068 | -3.25789 | -49.11956 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7380f364-3ebf-34b8-8de3-1cff6f50c75d | -4.6408 | -42.53018 | 2025-10-23 04:06:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c428cd0-f706-3341-a34b-7d9b69bee295 | -2.85368 | -50.73906 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f75bdb51-a403-36d9-9f3a-d5f711319eaf | -3.32632 | -50.22525 | 2025-10-23 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 595c547b-58d3-328b-9e8a-cee9b31ed7c3 | -4.70721 | -48.12236 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37237b1e-42ce-3aae-b4f0-04c6f0347f12 | -4.7097 | -47.99341 | 2025-10-23 04:06:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 601f485b-208f-3f2a-89d8-2e40157c1b22 | -5.69327 | -45.97728 | 2025-10-23 04:06:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 610126f4-cd0b-326e-93b8-d669e0ac9123 | -3.79714 | -40.84414 | 2025-10-23 04:06:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 061cea50-b7cb-303c-b41b-c72fdda5ea47 | -3.64776 | -48.97352 | 2025-10-23 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f857b3de-b150-39c6-bbdb-5d4de1a41161 | -3.0248 | -49.47635 | 2025-10-23 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1e5f312e-7f0d-3b12-981a-2a4fc7371d29 | -3.05201 | -48.71611 | 2025-10-23 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff6beec2-df94-3777-be93-c3f4f65d059b | -4.9394 | -48.30835 | 2025-10-23 04:06:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10b9224f-c978-3fc2-963d-f414481dd092 | -6.27846 | -39.69068 | 2025-10-23 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa733fd3-4e3a-34cf-a2db-00e2b57ce89f | -2.80346 | -51.3517 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fa5c565-2a4d-38e1-9269-0d8493acc4f0 | -2.2473 | -51.92292 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 213447d1-1db3-3999-8cbc-bd1f7ce35410 | -2.80417 | -51.34746 | 2025-10-23 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be574e61-fbf3-3edd-9cf8-738b16a4ee86 | -4.11834 | -42.18101 | 2025-10-23 04:06:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37091f29-cde4-3653-8c6b-b8987f904548 | -4.63887 | -41.12485 | 2025-10-23 04:06:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README9.md)
