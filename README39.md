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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cfe1b84-36d3-3b2c-9799-a13a2375e07e | -10.85708 | -68.55469 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd7f5c2e-a68c-3cee-9d2a-29dc94db3b2a | -9.72058 | -69.08121 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b380e617-7c28-374f-bce1-d2112c9de69e | -10.92031 | -68.59037 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 446d380d-03a0-3e48-9e82-e5a1a95a1e51 | -8.96166 | -63.62522 | 2025-09-22 05:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d11a4152-9ef7-32a1-aabc-a8b600d065ef | -8.41515 | -67.31145 | 2025-09-22 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e8c77ee-4d7f-3e5d-92c2-2e2ecf5a3a7b | -10.19996 | -69.08928 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb42ccf5-76e1-3462-8b31-0453996aeaf9 | -8.69629 | -64.20412 | 2025-09-22 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e01df952-5604-3ceb-b427-ced5e3787918 | -10.19577 | -68.78915 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa278a50-2473-3649-941a-d09fcc1d2e51 | -9.79973 | -68.88173 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 801c73c0-9d48-3064-9546-162ac6ad039a | -8.84201 | -68.66876 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 031fe5cf-7ecb-39f6-bdf7-4ce71ce7bb64 | -10.6753 | -69.09295 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2527dfae-9414-3725-8810-36cf4fd85ecb | -10.49209 | -69.16434 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7299f27b-73e9-3e13-a4ac-9e92a3244349 | -9.74079 | -68.43492 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 336655e4-a7f6-3863-aff8-7f6fbd46aebe | -7.6044 | -69.8966 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85b3593e-0ef1-35d0-ba48-582bf029cbe0 | -11.6809 | -61.16641 | 2025-09-22 05:57:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 205ff33b-66fb-3fbc-b242-7ba3420169c2 | -6.61208 | -62.96402 | 2025-09-22 05:57:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21fdb801-f61a-3e4a-bfd6-22a1dcf21a08 | -10.19176 | -69.35035 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4abd53d-eb18-3120-b8be-91fb68de2de4 | -7.96161 | -71.35259 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83cab21-b118-3ee3-bcd8-84fa64d3306b | -8.16518 | -70.89924 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 635316c9-41f6-3203-b717-fcfd7e6e949e | -10.14571 | -69.28202 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcb0ba12-1703-3b50-b95c-1c8755fbb9e7 | -10.85653 | -68.55827 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60dd4f1d-28fb-3150-877a-378563e61c15 | -8.36316 | -70.73051 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75221118-4339-34e4-a297-de93bdba5ae8 | -9.44981 | -68.58438 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59e0db1e-0d9a-3b15-bd1a-9c5d079c5fba | -7.566 | -69.91195 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0a99ee0-6b1b-35cf-b664-7d6fc5f780b6 | -9.68084 | -69.01378 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a6e2e52-6432-32a4-af47-731f9752d5ee | -9.28508 | -68.11934 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db6d5607-9470-3437-862b-97f82b74a9c2 | -9.24656 | -67.3914 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e235fe0-d023-3c64-b8c0-dcedc50c6c82 | -9.4675 | -67.10557 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e76d9fad-127a-33c2-b543-459cbfddedc6 | -9.26564 | -68.40022 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5714b1c-b6b9-3763-844c-7834daca3c1f | -6.85389 | -59.96434 | 2025-09-22 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eea963a-a3cb-355b-be06-673af1907733 | -8.98384 | -65.45935 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97b2a5d9-85d0-3635-80ec-36e9bd5f2277 | -8.35531 | -70.71397 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed2ebb5b-2fd1-351c-8b43-53737ee2508f | -7.56714 | -69.90481 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d233dc0-90c1-3a94-8122-daf4e0adfff9 | -8.22378 | -71.0287 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a545447f-0a33-3ed5-bf5f-8964deb8c391 | -7.85616 | -70.88879 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d77a3af1-43b8-37c5-9068-04d17b42833f | -10.18165 | -69.09715 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b08fba04-a88b-3013-be14-808274a31948 | -8.53394 | -70.94625 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75076e4b-73b2-3e3e-82c3-a359d6456703 | -6.85906 | -59.96516 | 2025-09-22 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67bc80ba-feb0-3d2e-837d-33bbdde53e40 | -9.91396 | -65.04753 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d3e7df4-a8ca-3c24-ba29-fb661f2666ef | -10.11232 | -68.19967 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14932668-8fa3-300b-a994-27b8339d6633 | -8.03428 | -71.26321 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b94ae92f-36ea-3d3c-aee0-4d14b459d2a1 | -9.10465 | -64.00607 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bb0c854-945a-38eb-bac9-fa2b846b975f | -7.24624 | -72.50598 | 2025-09-22 05:57:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf4efde0-f824-3548-aff3-2db3e9821f60 | -8.29045 | -71.06648 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac2c747-91f7-3883-9147-89ac1decf3bd | -9.47006 | -67.89033 | 2025-09-22 05:57:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0280f228-8ceb-31c9-82d1-f0878f496cce | -8.49097 | -71.44822 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0e2d48-d835-3cb6-b10b-5861b5e1069e | -8.20701 | -61.20414 | 2025-09-22 05:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a12c43df-685d-3552-aa11-5f8123643ae5 | -8.24382 | -71.10262 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c391d6-2d25-38d6-bc2d-787e615635da | -6.62913 | -62.93504 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a8d1231-ae02-324f-8a31-ae139e8f791e | -8.528 | -71.48537 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c12c39a5-febb-305e-bb00-3b5778c825c9 | -9.74024 | -68.43847 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcc6d3b5-0c6f-3036-947c-403e9f4de35f | -9.1246 | -67.73008 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09cdfd18-c09a-3712-9c30-a63e074b5a2a | -9.98894 | -67.57589 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a33de4f2-6edc-35e8-a432-56a7dc9c7696 | -7.85528 | -70.11313 | 2025-09-22 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 889e1ba0-9148-3662-a3e7-a2ebdeab9859 | -8.63301 | -69.26547 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3227274-271b-3307-a2a1-a235d0d4e4ec | -9.4695 | -67.89394 | 2025-09-22 05:57:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f98335-367c-3fd0-9fbd-918618bd0dd8 | -8.63634 | -69.26601 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3b48d08-bc33-360a-a2e9-71796cea5b73 | -9.67752 | -69.01325 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf1ca06f-290f-33df-8492-95c69a567272 | -7.65929 | -61.12421 | 2025-09-22 05:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b49cd736-4632-32c2-97ee-9cb74d51d6e1 | -10.27477 | -69.48955 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f183da4a-3f99-383d-ab4a-f2b31afda5a4 | -8.9845 | -65.45493 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a67fda8d-9c3b-3bb9-80a8-8280e1d5802e | -10.85317 | -68.55775 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| efb5cd69-fee2-3f19-a2b0-1979faf7a715 | -7.5902 | -69.89019 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553320e6-7393-318f-aa5b-ad8e2ba6e506 | -10.16289 | -68.70022 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 91aa6cc4-9923-33ca-9b29-bcf1f8284712 | -9.47211 | -67.09852 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35dd70ad-22a9-3a17-a99a-7acf1b6d583e | -6.6339 | -62.93181 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 493d2c68-1095-314b-be77-13dc5645dd37 | -10.27421 | -69.49306 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b979c4f5-94c0-335a-b2dd-2164f841e8c2 | -10.67475 | -69.09647 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5ee9439-ef94-37d3-ba9b-a19025a1b299 | -9.97567 | -67.09483 | 2025-09-22 05:57:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88ba4d7c-4b18-3950-b8d8-2ac3cd89008b | -7.2455 | -72.51051 | 2025-09-22 05:57:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b6aa514-3bf9-3799-9a61-1c4b2f1cd695 | -6.85347 | -59.96739 | 2025-09-22 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c67731-c739-321f-8ecb-7e2b11ada419 | -9.11508 | -65.50418 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d91a5f-a0b3-3bb2-a130-07c9db5bc9b4 | -9.13996 | -67.79115 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75a3ced5-82e6-3b9c-9da3-4c46a676ecfd | -9.12459 | -67.73308 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74fff5dd-2e78-384e-bc12-ee72cac88ef5 | -10.91061 | -68.43086 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29014b8c-60d5-312d-b232-af186c296b61 | -10.27164 | -68.77557 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be75173b-8eb3-354c-9370-f0358911e3ac | -9.12122 | -67.72955 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0536ea31-01d5-39fc-9936-dce5c5610fa7 | -8.02549 | -70.8303 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b53506-264f-3814-a0b4-b75fed64de41 | -9.30864 | -68.73169 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05616ac5-a8f6-3e7b-9c9c-fbdade433927 | -9.46864 | -67.09798 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52413e99-c915-383f-84f8-715e2b780e6f | -10.63705 | -69.04011 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa3a421-8623-33e8-8fa4-1f92b8bdb459 | -8.3716 | -70.80848 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24c10f50-2117-39d7-8801-24fd19012c04 | -6.59728 | -62.91977 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7989f336-7fbb-305c-9d99-263815a670b2 | -10.17131 | -68.79248 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abd4da0f-9377-323c-9295-a18f501e67de | -6.63445 | -62.92795 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb6fd933-10c6-36ba-982a-ba0af85c7a24 | -9.12515 | -67.72945 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 255e6f98-4e15-3f7b-9f06-b61ff6366d08 | -8.83739 | -69.51411 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| babf0385-3d8d-3347-b9df-1a1fefab6b0d | -9.10007 | -64.00905 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f7e2141-b6e4-3bc6-bbde-6fcf4112b82f | -7.31068 | -72.74568 | 2025-09-22 05:57:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16182433-7c76-3781-ba0d-5fc5efb4fdc2 | -10.6376 | -69.03658 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 646b50a8-e91e-3c5d-9fb8-48f080278ab4 | -7.60104 | -69.89605 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 378589f0-e7cb-3af4-8f6f-3de9be74baeb | -8.6923 | -64.20348 | 2025-09-22 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c381165-9e20-3937-9892-ec4acb45a91e | -10.00756 | -65.03377 | 2025-09-22 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db19f56f-21b0-3750-aa1a-450b3f596859 | -7.66412 | -61.12495 | 2025-09-22 05:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e358155b-10fc-3b5a-9ebc-87f452242038 | -10.43631 | -61.34153 | 2025-09-22 05:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82a966d1-0f31-39e8-b0c1-25dbc43fd157 | -10.16557 | -68.69742 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8013bbd-3e38-3f6d-b700-ca5636eb9189 | -9.36453 | -68.32856 | 2025-09-22 05:57:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7b7fdb1-2361-3ec4-b041-830d0129251b | -8.33515 | -70.72975 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea5ce1b4-26c1-3af3-b827-798f12b8797d | -9.87801 | -64.82855 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 083766dc-9339-333f-926f-0496af6e0a48 | -7.71353 | -55.45562 | 2025-09-22 05:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README40.md)
