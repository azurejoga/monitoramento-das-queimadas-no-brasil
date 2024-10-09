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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4493c1-3771-3d19-8167-e5282a03c399 | -17.16565 | -57.44767 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a36b8335-3b09-3f0f-80b2-297983d6e47f | -17.16511 | -57.42743 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 77e56666-b67e-38cf-86ad-7667dd52fa51 | -17.16493 | -57.45156 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7468a53d-cfe8-3be8-82ed-93fce079261f | -17.16439 | -57.4313 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 981014cb-f491-326a-a6be-4c1fb074cc95 | -17.16421 | -57.45546 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6c4cba23-92a4-3e16-833c-d02bb9147f23 | -17.16368 | -57.43518 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f00d7e7c-ab7d-354c-a1b8-1954a09c948b | -17.16315 | -57.41494 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6d52c230-a4b9-39f6-8ab4-35dbf9191099 | -17.16296 | -57.43905 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8941b448-4360-3401-802f-ba8f226ed37a | -17.16242 | -57.41883 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cb3c1d15-7830-38ec-a8ef-3a03284e2bb7 | -17.16225 | -57.3508 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5c472ea1-c1df-3778-8860-726684b11201 | -17.16223 | -57.44294 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f4a37b6f-4c5b-349e-ad34-6d6027096625 | -17.1617 | -57.42271 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 607512a4-f2b9-3aae-84a7-d40d5a2b37ed | -17.16151 | -57.44682 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 57a875f0-98fb-3ec0-b9d4-9c86e2e45969 | -17.16098 | -57.42658 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 56942148-aa2a-3b5f-97d4-6c11700b59ac | -17.16079 | -57.45071 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4059caf6-86d7-3a96-88dc-73583d754c05 | -17.16026 | -57.43046 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| cddbaddf-6e7e-348b-8bd8-8bae9aea343e | -17.16007 | -57.45461 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 45eff459-10a3-3cf6-8cda-5e74b91aff21 | -17.15954 | -57.43434 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ef659b26-6b28-3eac-86cb-748217371bc9 | -17.15934 | -57.45851 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ee5c1c21-092c-3576-b80b-f4551ecaf179 | -17.15902 | -57.41409 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42dc1adb-e8c5-3af2-a030-d02ae560d26d | -17.15882 | -57.43821 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 8650a17f-8cf3-31ee-9eaa-e8018a553eee | -17.1583 | -57.41797 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0ba2e5b9-16ce-3e8a-afa1-9f493bb73f8e | -17.1581 | -57.4421 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| db4432ba-849d-3086-88bb-9af0a557991c | -17.15758 | -57.42185 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a997e70a-c9f5-313f-a6a1-8343fd97d4f6 | -17.15738 | -57.44598 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 60542184-024b-33dc-b90d-6eff1497356c | -17.15685 | -57.42573 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 32660a62-8666-31ab-bb9c-5cf78fe94e63 | -17.15665 | -57.44987 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 51b00206-62db-3cd2-8a3b-5f1acc90d39f | -17.15636 | -57.31385 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 42f46e93-45e3-35e3-a105-c6c586bf8bc7 | -17.15613 | -57.42961 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1c63fb40-d8f3-38e1-bf72-e43dff236976 | -17.15593 | -57.45377 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 04911137-f60d-3c14-a719-6def1547c8d0 | -17.15561 | -56.11455 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3c128c00-0686-3500-8afe-b846dccf6fcf | -17.15541 | -57.43349 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| fd509b72-4fd3-3615-963a-79e43051b7e4 | -17.1552 | -57.45767 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 889dadad-a703-33c9-adb3-938f429469b1 | -17.15473 | -56.11942 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d08a70b0-475b-3ec4-b0c9-20d75f241679 | -17.15468 | -57.43737 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| e676266a-7786-3498-8f3e-f608311ad0a9 | -17.15448 | -57.46157 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b141d143-b341-3bae-a2c6-9e6d262cfbab | -17.15417 | -57.41713 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7c6eede6-ebcd-39b1-bc22-24e600a91a87 | -17.15396 | -57.44126 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 933fde84-fe44-3cf7-b479-7e87dfb75d4e | -17.15357 | -56.83176 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 206d32ff-e764-308d-8190-43dc2b180ead | -17.15344 | -57.42101 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d1f09bb4-f859-3500-abb8-5418e90a915d | -17.15324 | -57.44514 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 6f3b4e1f-ca69-33d8-adb9-6992ff97d54a | -17.15272 | -57.42488 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d179c1ea-1d9c-3a0f-b589-3418188cc8f1 | -17.15259 | -56.83711 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6dc1de48-e0b8-389e-8d90-c077745d9434 | -17.15252 | -57.44902 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 74532247-a183-35c2-b2bf-90d1815613ec | -17.152 | -57.42876 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 32808c14-c46a-3c2c-ada9-ea412fa66b57 | -17.15179 | -57.45293 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 2beda640-a704-3125-b60f-ca9b2fe6d437 | -17.15161 | -56.84248 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bbae5fae-3f36-35b3-9734-332cda2bd2e0 | -17.15155 | -56.82026 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bb1d7520-6bab-32c2-b0dc-254bbc7c51bf | -17.15128 | -57.43264 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 71dee171-1ab6-35c8-9d27-2971fbb2a291 | -17.15057 | -56.82561 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5afdc44a-6f0e-3046-9b9f-7c0684ddf733 | -17.15055 | -57.43652 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 12732842-cdb3-31dc-91ab-c012f2fb078b | -17.15034 | -57.46073 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0f4a2217-9b55-3ecf-8bd2-47d08eb75d8f | -17.14983 | -57.44041 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 01758c45-7970-3bd4-8caa-9fdc583cae2d | -17.14959 | -56.83096 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b89d51a7-cc98-33ab-ac17-472c5ba50506 | -17.14931 | -57.42018 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4c703082-2bd7-3d30-8c84-c9889873c41e | -17.1491 | -57.44429 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| b89f3aba-8b50-383c-b39e-fb4443546b0c | -17.1486 | -56.83632 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 400d938f-0db4-3acd-b413-8d24e97851d0 | -17.14859 | -57.42404 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a0fc04db-d493-3b3a-b927-eb70ea259a82 | -17.14838 | -57.44818 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 20716716-56c9-3a12-8128-679de2cb8f45 | -17.14787 | -57.42792 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 26797f8b-d356-3dbe-bfdf-3e0a48ac17fe | -17.14765 | -57.45209 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 93cfd1f5-fd09-3cf3-8212-ac4f0a82ca06 | -17.14762 | -56.84169 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1f55d30e-36e6-38ed-a91e-c3dd4b703a34 | -17.14715 | -57.43179 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4cef7851-d2b4-3768-8a62-17d7ae1429d2 | -17.14692 | -57.45598 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c0f5578c-0fa3-37a4-b150-5bee2675f55d | -17.14663 | -56.84706 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7e7f833b-bdfd-3aad-b1e3-fe44d98ee0b7 | -17.14659 | -56.82481 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c1007483-3861-3d39-940d-a8f2a99a8e50 | -17.14642 | -57.43567 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 94e9af76-6d2b-3791-8d09-6d873c0f2e0f | -17.1462 | -57.45987 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 82cc9d78-a135-3fd4-a6b0-88552235d44a | -17.14569 | -57.43956 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| fdf4597f-72f8-3c4c-922d-527039528c39 | -17.1456 | -56.83017 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e6e1bcde-0aa2-3cb3-b778-1189082590e5 | -17.14497 | -57.44345 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 9ba6e7c7-07ed-37a0-a6cc-06f94397b25b | -17.14462 | -56.83552 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c028c18f-3606-3640-bc80-b37103ba49b7 | -17.14424 | -57.44734 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 2ad2e905-be7b-30ef-8978-81fdfa91c230 | -17.14363 | -56.84089 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e49c3cbb-c300-3bfa-8438-a26046c87ffd | -17.14351 | -57.45125 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 11f41b60-0f6c-3b78-8b09-986fe10fbacb | -17.14301 | -57.43095 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 98f6b766-3fae-3b4b-a477-4408d0295e4e | -17.14278 | -57.45514 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7d7e7fd5-4802-3357-9aba-5fd828b05000 | -17.14264 | -56.84627 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf51bc9c-4e1f-3b71-82ab-decb65d130b2 | -17.14229 | -57.43483 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 068b8d89-0856-30cf-90c5-75a65e5455c2 | -17.14165 | -56.85165 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 54ed72a7-90d4-38a9-b7c4-99c3906f6e19 | -17.14156 | -57.43872 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cb47edef-1653-38a0-97ce-5f58f8032f5e | -17.14083 | -57.44262 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 7f2b3d64-9bf9-33f5-81d0-ca10f3284091 | -17.13937 | -57.45041 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e88d4351-7682-31c3-a25a-9764a5794a76 | -17.13888 | -57.43011 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ab97fdc2-ac49-30c7-b5fa-a13967058701 | -17.13865 | -56.84547 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a3b61b7-8eb8-3ab6-9bdd-f5b634237857 | -17.13864 | -57.4543 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 3c0b961f-3934-3db2-866c-9801bd52a8a2 | -17.13815 | -57.434 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 24c7d3eb-a102-3a95-a8b7-986ef52d304c | -17.13766 | -56.85085 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6de4ea4b-6daa-327a-995a-1cf1eddcb0c9 | -17.13742 | -57.43789 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 062fb915-19d3-36c3-9dbc-ce956eb8c68b | -17.13669 | -57.44178 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 042c0be8-5fe6-3901-8ab1-44fb9ef95bdb | -17.13597 | -57.44566 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| d6ce74d4-a4a1-3826-a1e4-40e2ba17d784 | -17.13523 | -57.44955 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 49070974-d428-333c-86cc-7601718fc9af | -17.13474 | -57.42927 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b8f431a4-6477-3e5b-9c55-092205ec42b8 | -17.1345 | -57.45345 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| a7deda45-3086-304b-b91f-4d6a9cc1adb5 | -17.13402 | -57.43316 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b74f79e-cf45-384f-8bef-7edd01b73cf7 | -17.13397 | -57.365 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 46d1c726-0c8c-3bf1-88c6-d4c1ae24e36c | -17.13367 | -56.85006 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 22161302-ead4-3930-8c22-1dc18c7c7793 | -17.13329 | -57.43704 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 87828cb2-e551-3c62-9a19-12f3e1b5e489 | -17.13256 | -57.44093 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 50eadd5e-3936-3d08-b20b-3059d834b57a | -17.13183 | -57.44481 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README133.md)
