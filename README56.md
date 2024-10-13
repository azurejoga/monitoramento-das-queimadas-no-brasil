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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80d34862-71fe-32a9-9b7e-b7372924ab29 | -4.12358 | -50.75496 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ceaa6d69-379a-3994-b122-170e00ae99f5 | -4.12018 | -50.75443 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81824e22-691e-3a47-b653-88c967b09640 | 1.24239 | -50.7082 | 2024-10-13 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41ffd61d-69a6-312b-970a-f211b30c1571 | 0.94925 | -50.20647 | 2024-10-13 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c694c1a-48d6-3fa6-b4b4-1939319c850b | 0.7552 | -50.86734 | 2024-10-13 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ba75b38-fb37-3235-87c6-0649a25eb8a8 | 0.75162 | -50.86787 | 2024-10-13 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 959a7cb3-dd43-3266-b973-32ec8403e1ff | -2.19407 | -50.86858 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae2e886-f731-384f-a3ca-3d33d18f1f37 | -2.19263 | -50.86493 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c21532ef-ee44-3e77-b32d-a137ab2969fb | -2.19204 | -50.86876 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609ee3ea-ce34-3ba9-9f08-5466d7b0be92 | -2.05882 | -50.70748 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb6a66a-0101-3656-8a66-07f434256109 | -2.05477 | -50.71073 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49be70b2-448c-3bec-997a-0380927d4c28 | -1.78562 | -51.01318 | 2024-10-13 04:38:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9028581a-4cde-36ec-b3a4-09320fc9e418 | -1.67502 | -51.16192 | 2024-10-13 04:38:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b29a50b-8894-3e39-aa7d-7a46d6b0ab79 | -1.59828 | -50.44495 | 2024-10-13 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87cfef9f-4eba-3316-a328-20ed2fb40418 | -1.57448 | -51.58881 | 2024-10-13 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 852c86d3-ceaf-3364-ab61-c2c07e9d165c | -1.48549 | -51.58056 | 2024-10-13 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ccf39c4-231d-3cfb-8036-f67e89ef0033 | -2.80678 | -51.02114 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3503de14-3bb1-3954-a48d-53075390dcd7 | -2.80452 | -51.01289 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35df3330-fc86-3e40-9859-663607990cb0 | -2.80391 | -51.01675 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9387edd-0ebe-3b87-affa-d42773b7d7b3 | -2.8033 | -51.0206 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7988eb86-8232-34ca-aa79-23528f518fd7 | -2.80104 | -51.01237 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9455bb5-04ee-3b68-88ab-bbb42117dbbd | -2.80043 | -51.01622 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 839bfad3-9da9-39c9-84b1-3e69932f0453 | -2.52681 | -51.2571 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1324c524-9860-34dc-9714-eb5246f400d8 | -2.25631 | -50.56865 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9d47a04-d861-3491-8127-947cfeaf4449 | -3.5859 | -51.50956 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c0af5c-a947-3ae8-907a-fb080acde5b5 | -3.58175 | -51.51297 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02a67e50-ddf2-30c0-a493-707cab7dbc90 | -3.55736 | -51.48483 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d307c89-d007-3328-8334-8d461ae46979 | -3.47162 | -52.1585 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0de6b499-434a-354f-913b-a4d558c382e1 | -3.46653 | -51.55272 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48a047b2-b58d-313b-ab58-4bd12b19751d | -3.45511 | -51.62464 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea9f6603-2a4f-3ca9-87e1-204ba8dddead | -3.44894 | -51.59491 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10ab0149-dd21-3227-a9eb-59428c0eb657 | -3.40902 | -51.57226 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7229612f-d8b7-35aa-b711-44dc27f25eb5 | -3.36838 | -52.17016 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 284c1ecc-3ba0-348c-b99d-7de229fafca0 | -3.30189 | -51.49454 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74d79198-56b7-3d9b-8ac5-84541cc4fbb6 | -3.16457 | -51.69236 | 2024-10-13 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59ff4f73-edbf-3bd9-ab79-d93bb53471ac | -3.58527 | -51.5135 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0c3ac59-d3d3-32a5-a496-5d19bc2d80a6 | -3.58237 | -51.50902 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a190be5a-9ce0-3c0e-8c35-a4ebbb22f91c | -3.53594 | -51.25037 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c453b6e0-3e5d-3ad3-8cce-6ee57582d240 | -3.51588 | -51.28684 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49b36e64-76d7-338e-9256-31a6dad85baf | -3.46299 | -51.55219 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 746c68b9-9655-3621-913c-52faa8259cfd | -3.38631 | -51.35033 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26fa5b84-987c-353c-81e6-e248d35f22b4 | -3.31531 | -51.41157 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f4adf40-5c4f-3dbf-88d6-632c79965383 | -3.28038 | -50.9526 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56686999-401f-3db4-aa4b-ac088231eff8 | -3.27043 | -50.77443 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8062ee08-f488-32fe-b098-59d94a0ef321 | -3.2679 | -50.94717 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e357216f-23ec-3a51-92f0-4bc5ce6bdf2c | -3.23052 | -50.84869 | 2024-10-13 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e5f48f8-cf51-3cd8-8cd4-da8025a41905 | -3.22311 | -51.28563 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e7a717-e29d-3029-ae91-a28217dffa5f | -3.20191 | -51.75648 | 2024-10-13 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7a741e9-1b8f-323e-85e4-fefeb4c9d800 | -4.61552 | -50.95256 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c915866-8353-3bff-a772-b396f3bcfe50 | -4.61493 | -50.95625 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aea2edb1-ae1d-3f72-abd3-73c3d7c0ab78 | -4.61211 | -50.95203 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c243fe71-0510-342c-a809-4dab2cf88ced | -4.61152 | -50.95573 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8aabffc-2031-303d-afc1-ad848bd8efdb | -4.27764 | -50.957 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ae5af2-16d0-36d6-a829-94c5a0c1118c | -4.27705 | -50.9607 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 349577e0-72d7-3027-a7f1-e6a1aba01513 | -4.27422 | -50.95647 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d6e484c-333d-32d2-b5a5-a76f8d47db77 | -4.27362 | -50.96018 | 2024-10-13 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23019630-d0a5-3178-a023-c4bc7b81b30e | -4.26395 | -50.95487 | 2024-10-13 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6af983c9-2d4b-3fe4-bbbb-da80827f098c | -3.96467 | -52.17473 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4181c80f-255a-36f8-a2de-179231f42a22 | -3.96174 | -52.16988 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01973e06-05ea-3b8b-b36a-ff04b4916218 | -3.96105 | -52.17413 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdfe261e-f316-3198-8719-b641043a4d2e | -3.91703 | -52.21113 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28174009-e18a-3d46-b94c-7c35149b39d1 | -3.91407 | -52.20635 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 207608e6-9f33-3cb7-831d-715465e7e69a | -3.9134 | -52.21056 | 2024-10-13 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0f442f3-4036-3c93-803e-d888ca86f355 | -4.12585 | -51.11365 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57fb6775-d42e-3221-b42b-24d6495cd8c4 | -4.12238 | -51.11322 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7d07714e-c63a-30ea-bb4d-0f64e30c39a8 | -4.10524 | -51.11431 | 2024-10-13 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f49a2f2f-8de7-3092-8908-61bd93a21103 | -6.39641 | -52.71098 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ac056c-29c6-3969-a4df-064b486bf720 | -6.39572 | -52.71519 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 755e326f-6665-3934-ad6e-7dbf00c45d61 | -6.3928 | -52.71038 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23872b4f-3b25-36ac-b936-8197e057f320 | -6.3921 | -52.7146 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d67ddc52-d4f0-39d3-9f8c-ae64c391ad16 | -6.24553 | -51.71996 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 918d039a-10eb-384d-997c-65a39d4cc4eb | -6.13031 | -52.65836 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ee991f3-61a7-3d2e-b215-9ba0f1644567 | -6.05404 | -52.163 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b69faac-ab9c-3ab5-ad8e-6253d0160ffb | -6.77801 | -51.62129 | 2024-10-13 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f986d3d-f45f-301d-9ebd-3b5493c6c24e | -6.73164 | -52.03758 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0480fc-6da3-38fb-a0ed-e529d478b232 | -6.72944 | -52.02906 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 712092ba-de50-3cb6-9a14-c73b9691e447 | -6.72529 | -52.03258 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f1cdb89-925b-30ac-af43-2c3ea4aeb677 | -6.70077 | -51.62092 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d660b6-7be4-352f-9bb9-46bd21099d26 | -6.69576 | -52.01597 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed362fa5-2a39-30c2-bbe5-25765acb4c98 | -9.10234 | -53.31743 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef63f40f-ee58-378f-a454-2fcb0912d158 | -9.07462 | -53.27449 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c21877d8-fe00-3012-ae36-a099f86b4278 | -9.04987 | -53.00188 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 873dfbde-ae90-371f-a708-c8bf25dddef0 | -9.04764 | -52.9933 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e33f40-44e5-3f2f-bdfa-07a17e5d396f | -9.04698 | -52.99726 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12ff5e95-d933-359f-b81c-000dc9af12c2 | -9.04408 | -52.99274 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b97e9b-05d6-343f-9f4c-ca2014e50cf8 | -9.04342 | -52.99671 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06324a7a-b02e-377a-9df7-a39d80d0aecc | -9.04189 | -52.94325 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac7df5b1-0d01-3c77-9426-646c6c96979e | -9.04158 | -52.94228 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d0159c0-45dd-3b4f-a238-a1f2b71a8ced | -9.04051 | -52.99221 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0c40915-e59e-36bb-a9f5-379123470bac | -9.03984 | -52.99621 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3632eab-fe81-3353-82f2-c371d899efff | -9.03836 | -52.94257 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b4a473c-c21a-3b06-b5c4-044984ddf931 | -9.03415 | -52.94601 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbd02ca4-e1f9-356f-a812-5991c3d3be9f | -9.02135 | -52.09118 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdee8e6-2b2c-3fad-90db-2f157242e2b4 | -8.85775 | -53.02255 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffb7f0de-b479-334c-928c-54a11dc66254 | -8.85556 | -53.01365 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673abe58-ab1e-3969-b575-89499cdeca90 | -8.85489 | -53.01772 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ccb8da1-ae86-3e37-8b39-334e80a2cd57 | -8.8542 | -53.02184 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65fce179-8d2a-3506-b486-b8191ffbd56c | -8.85199 | -53.01308 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dccbc0cc-57ca-312e-9870-7f7442d135e6 | -8.65234 | -53.05831 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37ce80db-9633-3491-8d70-92504150a7c0 | -8.65167 | -53.0624 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
