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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09bce4c5-8a1c-3c4a-b472-f442aeeeb6e8 | -4.36628 | -48.63046 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28405693-6719-377e-8381-740ecc594235 | -4.36529 | -48.22182 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570548a4-457f-391d-ace4-6cb2660de39f | -4.36152 | -48.22116 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5103331c-db47-37d2-b17a-71304846898b | -4.35699 | -48.15412 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40666e80-4081-3138-9f02-a0b579bf15f4 | -4.23038 | -48.04467 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 636efde2-ba8f-34d3-bb41-e64ff6354e9f | -4.13063 | -48.13631 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0cce393d-5973-3d91-93c0-ead78280b876 | -4.10404 | -48.51428 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9e421d4-7a38-3051-8cd2-a912ae0e2464 | -4.10019 | -48.51363 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ca859aa-50de-3ce1-b497-3b7d98c4da95 | -4.09425 | -48.84774 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33b1065b-e002-3fb0-acb5-1ac8ed95f5e8 | -4.08625 | -48.31075 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fdf98d2-a10e-353c-a956-637baa20286e | -4.08244 | -48.31008 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954e3e86-f9bf-32d6-a59b-e9326196b1e9 | -3.98861 | -48.9716 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6785044-b62f-3cd0-bc88-f1209a3f19c4 | -3.98802 | -48.9751 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31254afe-1785-3e93-8cd1-a770923e5da6 | -3.96295 | -48.9384 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 442fe801-5fb2-37fb-a4a5-6bfe9174801e | -3.94823 | -48.13479 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0f25491c-867b-3a0e-8dea-e9a1888440ce | -3.93931 | -48.35964 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0df1d399-090f-3c38-923c-5c4ec2a6abfa | -3.93625 | -48.35418 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9976e98-e934-3335-a563-e41d471cc964 | -3.93319 | -48.34876 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b78e191-3ae8-357c-8997-287d3894a754 | -3.93242 | -48.35355 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0117e801-e40b-30bb-93f0-69a370a67b67 | -3.91949 | -49.08067 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7261c70a-7b4d-30ca-b528-e45720de9950 | -3.90627 | -48.3691 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d0d7a63-b3be-372e-a0f0-c0e05c3652a9 | -3.90343 | -49.07802 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dcfe4623-6416-380d-9823-97c5eccd0358 | -3.90286 | -49.08152 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f90ad232-13ff-3cf0-817b-4cd2b8dce0c7 | -3.89884 | -49.08092 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2e7dfaf-708c-3d3e-9fd8-97e22eca031b | -3.76074 | -47.73766 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff1d178-4807-3dc2-8fb9-19844e286b97 | -4.90934 | -48.64429 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d44b3d80-52a5-3837-b2db-be0d85d28505 | -4.90685 | -48.64644 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd22094-aeb9-39db-8f56-44b3e1d1ab8d | -4.88992 | -48.66581 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 915a4188-6021-3a7d-bbe5-f8b19f1ac69c | -4.88688 | -48.59878 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9868ef45-4071-33f1-a2b4-a65fd31bc4cd | -4.87234 | -48.567 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ea3f573-3bc2-35b9-bb25-826bd303fe85 | -4.8565 | -48.73769 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6f470c9-d321-3142-872c-4d3c0e7fa708 | -4.85262 | -48.73705 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 261dea37-54a9-3968-8aa9-0e0adf05fbc9 | -4.8189 | -48.15564 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa4f4de3-cac9-3432-afc5-9506535c9a79 | -4.79555 | -48.57878 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db0cdb4-22df-3687-98b2-fde6068ba8f4 | -4.79313 | -48.57988 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 458605e8-70cb-32ac-8711-673993a52c95 | -4.72737 | -48.47684 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 529c54c5-fcfb-34c6-b90f-1c6eef4f89f6 | -4.59561 | -48.07291 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb320853-934c-326c-99f9-d6a095f31a13 | -4.59189 | -48.07224 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 771b54e5-1c5b-3982-a02f-b1cfcebedb2b | -4.59116 | -48.07665 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6caab25e-0634-3026-93f1-c46a8e7548c6 | -4.57261 | -48.01559 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5634df7-5fe2-330e-9423-2cdbb5c40e1c | -4.57093 | -48.01347 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df441531-7409-306c-9bb5-36d105ab3d83 | -4.4864 | -48.1221 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7a04ea-d1be-3830-845c-bb336d776d7a | -4.36775 | -48.62904 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb68dcc9-1c0d-3388-babe-3cf4bd305399 | -4.29635 | -48.64434 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7461531c-0246-3071-b5e7-6846ecb0b258 | -4.22591 | -48.04856 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4584cea2-97ed-3a6f-909b-bc1ec7bf00a0 | -4.1466 | -48.39782 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba04b38c-4549-3385-add7-c51c7f5faecd | -4.13138 | -48.13178 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab27d5b6-5add-3958-acad-99222ce56d78 | -4.11473 | -47.96768 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96d56283-6b3b-3eaa-a577-449abcdc22f4 | -4.10484 | -48.50939 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af0998bc-fe1c-316a-9c79-ad110d8b0ca8 | -4.09633 | -48.51298 | 2024-10-30 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5863057-c5bc-3d9b-b043-feb840cd5a69 | -4.08306 | -48.31181 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaf812bc-f18f-357a-b793-488824054cc2 | -4.06239 | -48.29421 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7592261a-e708-3ef2-886b-c94a77b264d8 | -4.06163 | -48.29893 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3276ed67-7bbf-3ace-9bba-327757e2c435 | -4.02653 | -48.29808 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ce9296-e529-32f2-88cd-c4759f6aa7ff | -3.96694 | -48.93901 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b66708c5-6748-35eb-bac7-bb6874fb5669 | -3.9635 | -48.93499 | 2024-10-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3edcf890-e666-381d-b855-0832d3b8b514 | -3.95653 | -48.13147 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b8767350-a06c-3ca1-9dab-7db9bef7ea0f | -3.95348 | -48.12632 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6704a848-f74b-3085-845e-3adfc9f0ee16 | -3.95274 | -48.13089 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a1576863-bf8c-3e08-8a16-6ee189c0ab45 | -3.95201 | -48.1354 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| cf7bf1ef-e816-3f3b-aa16-3657a68bb0f2 | -3.9497 | -48.12574 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f96a446a-8a59-3bc8-be0d-7c0a10592b74 | -3.94896 | -48.13031 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1e9ca697-d749-3524-8021-30e3a1887ede | -3.94517 | -48.12973 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 31f2203e-8f59-33c0-b9a0-fdd876693534 | -3.93702 | -48.34941 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cb332e5-66ad-3236-aa0b-f0ac2c3403ac | -3.93547 | -48.35901 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a349f43-81a5-3799-9798-12748c3569e7 | -3.92936 | -48.34811 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0650839-ed6b-30a1-95cd-9f73b90bb2b9 | -3.92629 | -48.34276 | 2024-10-30 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cebe16e-3f9d-3d26-9bba-d2c053848210 | -3.91261 | -47.94381 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96755ace-07b7-31a4-a003-a550c443e111 | -5.99255 | -49.59061 | 2024-10-30 04:19:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd8806ee-7bc2-33d5-832d-e03533bba78f | -5.8473 | -48.15694 | 2024-10-30 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afc1847f-a9f2-37e8-81b6-9fa9db3f16c7 | -5.84638 | -48.15572 | 2024-10-30 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be8611ac-8816-3ac4-a947-293009ffb2e4 | -5.84564 | -48.16015 | 2024-10-30 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f40b50cb-1e2e-3ac4-9e87-db65fdf735d3 | -5.70828 | -49.31434 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60f33951-20b3-332f-a44c-f82bb77f0fb6 | -5.51628 | -49.20989 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729d550e-68e0-3028-9084-bbcbf730c21d | -5.51233 | -49.20925 | 2024-10-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa27c0f2-34cc-3876-a875-e6e7b7c62107 | -5.23173 | -47.94951 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 03cd81a9-5060-3945-83b7-e36f246dc1c5 | -5.23123 | -47.94844 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d1264468-11ef-342c-8472-5ebedf123e30 | -5.22805 | -47.94888 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 703f3dcc-709d-3ba0-9d1a-fc96edf008b1 | -5.22755 | -47.94781 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d6be3f80-41ae-37ab-b374-2ce8f7d84007 | -5.22682 | -47.9522 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e1c45b42-69c9-33dc-8c29-85065c5f05ee | -5.22437 | -47.94827 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 062dc4b6-5b0f-3e2f-ba53-1c2f45a5b54d | -5.22367 | -47.95265 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f6d2a645-a0cb-37d5-9e08-fab361749921 | -5.21906 | -48.11346 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb24d8f4-5d09-367a-aa97-7c5b8ff262af | -5.21534 | -48.11286 | 2024-10-30 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b133c2d-a4ae-3194-b730-991da1443fdd | -4.96708 | -49.36932 | 2024-10-30 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8718521e-6bbe-33a7-9022-a2fdfd637585 | -4.96651 | -49.37286 | 2024-10-30 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deef26aa-8e77-3694-8f47-04c905310b25 | -4.96248 | -49.37222 | 2024-10-30 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1492415-44be-394a-8974-ffd419540058 | -7.17682 | -48.77929 | 2024-10-30 04:19:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1402c48a-06a0-3a49-87bd-685f236a13a6 | 0.08629 | -49.8713 | 2024-10-30 04:19:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c486af9-db0a-31a0-8c1e-fcef5b53b3e1 | 0.08178 | -49.87204 | 2024-10-30 04:19:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bc5df53-fe7f-3b4f-8d9c-6b07f61db244 | -2.129 | -49.07063 | 2024-10-30 04:19:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d67db60-0f50-3089-b01e-a7ba07b24b48 | -2.09762 | -49.50197 | 2024-10-30 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb65abbb-0ce2-3ca7-9e6d-5acc53b99768 | -2.09697 | -49.50596 | 2024-10-30 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7f01a96-b64a-3ca4-8afd-96c9cd263953 | -2.09337 | -49.50131 | 2024-10-30 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc7d318d-76c3-3ef6-8894-776bd736cfa3 | -2.09272 | -49.50531 | 2024-10-30 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 370d59d7-0ad4-3888-9c9e-cd55aef106e3 | -1.67924 | -48.8074 | 2024-10-30 04:19:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1dbe6b7-0fd7-359d-8abf-fe48aa8b3f4e | -1.4235 | -49.2142 | 2024-10-30 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3aa8757-6644-3315-81e9-1f67469bfeab | -1.42289 | -49.21809 | 2024-10-30 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b544a904-de59-3843-8d83-64a3e33a5da5 | -2.05535 | -48.8825 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17520899-25dc-34ba-a36a-00b4d7389fde | -1.67515 | -48.80677 | 2024-10-30 04:19:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
