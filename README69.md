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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e05c73-eeb9-3750-bda2-951cf5c3c243 | -4.96645 | -56.26864 | 2025-10-27 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5a114eb-03ab-3353-9d97-5f06b3128b68 | -8.09663 | -47.06341 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d8b1b3b-66d8-3e05-a0fc-85cccc3020ec | -13.28428 | -54.39468 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c712590-da5c-36fe-823e-d7dada2578c8 | -3.14437 | -50.45036 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d1eb691-8a75-3be1-8369-b54f202bf073 | -13.30536 | -54.38169 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3bb6540-a4ae-3986-8f03-3a6ee4eb90c6 | -3.47066 | -49.96598 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 791406ca-709e-3208-ba36-374745d0eab5 | -11.97641 | -58.06103 | 2025-10-27 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb11f790-8b98-3759-afcf-7870854289fd | -2.97085 | -51.03349 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68ce15a6-f46d-3c9f-8909-70afab6f59a6 | -8.12519 | -47.03806 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4d616a0-b8c9-3bdd-9d9f-4980f740be32 | -9.04118 | -47.62754 | 2025-10-27 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90c725a0-2932-3d71-829d-ead0fdbed58b | -10.68331 | -47.83947 | 2025-10-27 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d2d2c5f-b411-35b8-acda-ba98a0f1d2c3 | -13.3156 | -54.37765 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5e334a9-68a0-3c8f-8b39-e8ab9fd6c46b | -3.10059 | -49.45323 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf218cfe-a54c-37c7-ab01-82ea3e8431ce | -13.25828 | -54.37022 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 09833a6c-e36f-3425-9919-708f893b7b24 | -3.72819 | -58.59479 | 2025-10-27 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12465976-ae23-3038-bf88-ad553272c171 | -14.37598 | -51.53438 | 2025-10-27 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67a737f1-4ac6-3333-a1ec-5e4f48808269 | -5.77431 | -51.86046 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c165aa1-5d84-38c2-ad3a-42dfa5bcea21 | -13.30336 | -54.39712 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 407476b0-1b6e-3b8d-ae11-8915fca2692e | -7.05869 | -46.75916 | 2025-10-27 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed22eccd-ca6f-335b-ab46-1372ed6d5855 | -13.31969 | -54.38489 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bbaea13-afae-32f0-92fd-ae26453ebbd0 | -13.31216 | -54.3667 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d9b62d4d-12a4-3267-b0b6-9fb4804f8ed3 | -14.2527 | -48.13449 | 2025-10-27 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57209b86-cf14-3bb1-a0c9-9620985ff258 | -3.72477 | -49.68945 | 2025-10-27 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30518e0b-c684-345d-beb0-71d48783ba1a | -13.2598 | -47.97262 | 2025-10-27 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a12c9815-5fe7-3903-abac-86f9c73662a1 | -3.09942 | -49.46121 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfb001cd-29b5-3c66-9c9c-2a0d53651ca9 | -13.30192 | -54.37074 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e6fa4d6f-2162-3c39-a796-2efe6d8b8db8 | -2.86895 | -54.20557 | 2025-10-27 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f7cd47f-d8ce-3453-96fe-8ceef61ffa34 | -3.97854 | -55.74741 | 2025-10-27 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c70ca6d7-cfe8-3a94-aeb4-7ed66645056b | -13.31904 | -54.38855 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a02ca79c-377c-3f69-8f4a-e8122576773d | -9.0409 | -47.6205 | 2025-10-27 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb773300-442f-3d5b-aaac-8dfeb455dd06 | -8.09769 | -47.05519 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf2f96a-7d9e-37f7-8fd4-811950a8db5a | -7.9295 | -55.01818 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c01bed91-68b7-3b61-863c-6bfb98b7ca47 | -3.10918 | -51.21231 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f1b4f70-9903-33c9-a1a8-05d2bfed947d | -13.27952 | -54.39397 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74fec896-defe-3e34-8401-f6eaf4360bff | -5.71589 | -49.31223 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ea76af-8d8a-3c7f-a91d-3ee4e5f4a113 | -3.1379 | -53.0031 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1625b8ad-48a7-3ad3-ba36-8b96b3662f7d | -3.09486 | -49.45222 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc3f60a-8dfd-36d0-954e-3b740ba868fd | -4.62733 | -50.41615 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a05bdf9-c2af-3011-965b-dcee6978740c | -3.23772 | -50.64801 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88ce4e1a-b457-3b43-9cf1-b219d97dadc6 | -4.1587 | -51.08793 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef72905c-14e5-33b6-8942-8a45cecc3d2a | -13.31905 | -54.39008 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c659a7e7-542f-3f60-a12f-5f6ee24c0cad | -10.20532 | -52.66344 | 2025-10-27 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 930b9116-ee98-3024-90d4-e4d0f276b0b2 | -3.23671 | -50.65455 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d7b03d11-93bc-3b63-9ea7-1f7e6d6043e0 | -13.25959 | -54.35977 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5313f18f-9199-33e0-a149-c156aa1dd6dd | -14.25693 | -48.13533 | 2025-10-27 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23a4042c-4782-3c17-bdb6-d4e2a4fdfe16 | -3.80015 | -49.29338 | 2025-10-27 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6930df2-1f05-338f-ad43-366c1495bc16 | -7.93372 | -55.01882 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5768a704-f318-3c2e-a1a0-b13677eac94c | -2.7965 | -54.86035 | 2025-10-27 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8b3925a-8839-3a88-b899-c51e264d2fae | -13.29514 | -54.3857 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b60124d-b725-32a9-b3bb-d467839522bf | -3.10004 | -49.45039 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cd2fac5-27b6-3f34-8123-6da9713253e8 | -7.06268 | -46.76019 | 2025-10-27 05:23:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e21308-6453-3316-9865-9a4888a30f79 | -4.09975 | -51.05148 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d37be1d9-d53b-3e56-8893-bf013950667f | -13.30125 | -54.37592 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24290014-51b3-3a2b-9ee1-1bede0da8d56 | -9.60372 | -50.79037 | 2025-10-27 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 538d4906-7d6a-333e-9740-0d7d315e4331 | -8.12267 | -47.03017 | 2025-10-27 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7bab166-2093-3b02-90f0-e9b46c885890 | -9.28769 | -57.53815 | 2025-10-27 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2fc0bef-1168-33f2-b35b-653e859a671c | -3.83641 | -50.20208 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 870ae89b-c4c6-3170-b47a-af47f6b933b7 | -13.25893 | -54.36502 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| aac69dd2-8507-3689-877a-75b8b6dd7e2c | -3.10964 | -51.2093 | 2025-10-27 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe81d4a-8681-3ae3-9cbb-b372cab3602a | -7.22229 | -46.87069 | 2025-10-27 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 933fd785-63c2-393a-96ec-3ef588b39654 | -13.31149 | -54.3719 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fef9c8ef-ef71-3998-a6e7-910eba6e36d5 | -4.26415 | -50.51157 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ddcc254-5089-3789-a0de-216382b4d9b2 | -13.2637 | -54.36569 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 867976dd-281f-33f5-a35c-10fc36217df3 | -4.35231 | -50.33164 | 2025-10-27 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c623685a-b7d0-35ea-bb4a-986036539511 | -3.46905 | -49.97701 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8a8ecaf-65a8-3732-969e-8b38852320c9 | -5.77283 | -51.56376 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee457d33-c5a5-309b-977e-59c847baa780 | -13.31081 | -54.3771 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55aeaaf1-4339-3394-b948-2038b71d9ed9 | -3.42391 | -52.43675 | 2025-10-27 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4dd23674-ebcf-348e-9080-88b5bec1ad42 | -3.09677 | -54.62141 | 2025-10-27 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0230cba6-eb45-3d56-9b41-f8a9618bb230 | -3.55806 | -53.01616 | 2025-10-27 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 950546b4-6c55-36a8-a1fd-0d712cb09e0a | -5.72129 | -49.31752 | 2025-10-27 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daea4054-e823-375a-8bc1-e81f454cc782 | -3.97943 | -49.29123 | 2025-10-27 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe065c33-8367-362c-b619-a2e7bdcd194d | -10.19387 | -48.06967 | 2025-10-27 05:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48f26f4d-410a-3534-b77b-28c907418b16 | -13.30394 | -54.3551 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d9edd2dd-5996-30df-861c-480e699419b6 | -13.29581 | -54.38049 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 159355b0-0a3d-39d9-8a58-dd3833c78741 | -13.29925 | -54.39144 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b1ebd56-7ea3-30ca-8ce5-d40c4935e5e9 | -3.09545 | -49.44817 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddefa1d8-912d-3c4a-ab60-5f75e0fdec68 | -3.23531 | -50.65549 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d52a87b8-8982-33de-ae6f-80d8a538c55f | -8.06419 | -54.92345 | 2025-10-27 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f03d7942-0f13-364e-8dfe-cff7273da473 | -13.2897 | -54.39021 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 672bbdaa-6815-3d70-96e4-9b8a1f261320 | -10.20491 | -52.66656 | 2025-10-27 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc56c360-5579-36f2-b133-8a8d58a6eaec | -3.86549 | -50.89311 | 2025-10-27 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16d4743e-8184-3b9c-b6de-62fc3045209b | -2.78622 | -54.41813 | 2025-10-27 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab51946b-5206-36e8-9d81-4104a059ff87 | -5.61652 | -51.79095 | 2025-10-27 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c473058-afef-33d2-a4b7-40b150d95df3 | -3.09881 | -49.4584 | 2025-10-27 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c68e6d94-f16b-3b97-bc9d-418777b1d918 | -2.9458 | -51.76147 | 2025-10-27 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09181faf-e655-350a-9c05-8f2562771e66 | -8.69672 | -50.81039 | 2025-10-27 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a59d25d7-b7ad-37a7-a88c-7a16bfa1ae3a | -13.26848 | -54.36634 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5762d46f-0e3f-3415-87a7-e6ebe18722d0 | -3.24253 | -50.6521 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4fb8b67a-8248-3c9d-bda9-066c84db73ee | -13.28494 | -54.38951 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f7193ca-6fe8-3988-a9ec-18e0088c7584 | -13.31971 | -54.38337 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08c94a4e-a006-30e0-a16e-a5c67f18912e | -13.31284 | -54.3615 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc877bbb-1136-3323-8da2-14a76cd50d19 | -3.57157 | -49.02268 | 2025-10-27 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a852f232-d45b-36f8-b2c1-aa646a69b8c8 | -8.06745 | -46.95194 | 2025-10-27 05:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1317cf64-ee13-37ec-99fd-45b6fea0a826 | -13.3067 | -54.37135 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7e9e87f6-e36b-3693-8c7e-45022785fcd8 | -13.28771 | -54.40571 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e624fe12-d824-38e6-8c11-e6a8a59c8b08 | -3.23626 | -50.64893 | 2025-10-27 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b62bc569-c43a-3ffc-a534-110020e64226 | -13.28761 | -54.36868 | 2025-10-27 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d28ba780-f35a-3542-82a3-2a3be5c96499 | -9.45021 | -56.64446 | 2025-10-27 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c07b2c16-325b-3e64-9180-e11842e3f481 | -2.7957 | -54.86549 | 2025-10-27 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README70.md)
