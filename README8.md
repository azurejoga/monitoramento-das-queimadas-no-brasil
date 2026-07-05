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
| 713eb9b2-ac2a-3d64-915e-05f35c52af36 | -13.2449 | -54.32655 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 226bd571-3e25-3579-862a-fd9037408b99 | -10.9363 | -43.04027 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1fcb920b-ee45-34d3-8236-fc87c31ed96d | -11.89241 | -43.83039 | 2026-07-05 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0273e41f-c16c-36c7-9f88-ff47468b9d78 | -11.91235 | -43.38464 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2391bddd-41e3-3a30-a02f-921c7746bbea | -11.31338 | -54.47447 | 2026-07-05 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11e0a61b-dff1-3f36-a956-0446e8376dd1 | -17.26626 | -49.00686 | 2026-07-05 05:04:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c70db2e1-a0be-3630-9071-e1248b975bad | -13.21493 | -54.34343 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82b79f33-eddd-3260-bd19-55248a874404 | -13.23548 | -54.32137 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e0e7585-ba9b-3f25-88e7-4a87a458af84 | -13.23713 | -54.33255 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a87001b7-3e86-3054-8bd3-de28e27825be | -11.35701 | -62.44857 | 2026-07-05 05:04:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c3ef8b11-5fd3-33bb-9147-d227cfe06815 | -13.22439 | -54.32681 | 2026-07-05 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49e39e2f-2745-3c47-b479-bd51c5ed4061 | -11.91534 | -43.38656 | 2026-07-05 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93c3f3b5-fe3c-3efe-9ff0-5c2b3afa45a4 | -10.93683 | -43.03588 | 2026-07-05 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ee6b66c9-c6bb-332c-876c-e3614bca3220 | -11.52668 | -46.48093 | 2026-07-05 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc2ac308-5faf-3276-a5dc-87ecd8dea408 | -21.29068 | -56.87504 | 2026-07-05 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ce4c5ea-c723-3554-a637-8d7b3a513277 | -10.9401 | -43.0355 | 2026-07-05 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 45f9c06c-ed18-3f7a-91f6-5aff7e151103 | -10.9397 | -43.0593 | 2026-07-05 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 6e0d3af9-f5dc-3706-a0aa-00431c39cc43 | -10.9209 | -43.0384 | 2026-07-05 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 893ec26b-a20b-3229-aeb0-488fa0f419dc | -10.9397 | -43.0593 | 2026-07-05 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 8ac305c8-49d7-3994-a0bd-83b9a68fc090 | -10.9401 | -43.0355 | 2026-07-05 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 54690070-aae4-3f1a-b54c-9a46a79ccb3f | -10.9209 | -43.0384 | 2026-07-05 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 9aa6a5e5-7b44-3533-b519-9fbc16a18391 | -3.21514 | -53.02627 | 2026-07-05 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 269b79d2-57fd-38b4-9d02-799aafd7427b | -5.86856 | -51.73984 | 2026-07-05 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caef94cf-e6db-36a9-84a3-ff72a85c55c8 | -5.86929 | -51.73489 | 2026-07-05 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047b74c9-56c8-3f11-bc9a-e2a80083f5ab | -3.21397 | -53.02568 | 2026-07-05 05:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8408c098-9b41-3a3d-af37-03178f6c6bbb | -3.26155 | -51.10083 | 2026-07-05 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a0415e4-b289-3173-b60f-5823e5b559ee | -17.00336 | -48.28302 | 2026-07-05 05:23:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3333b4f8-6f87-3705-b509-93a9c32c019a | -17.26815 | -49.00977 | 2026-07-05 05:23:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a71b4964-b832-3989-a924-81f97b742496 | -17.0101 | -48.28391 | 2026-07-05 05:23:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72331926-5a8d-313b-aa18-2d1e47e87bbc | -10.9686 | -48.13179 | 2026-07-05 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c960296-ff74-3a0c-ad07-5facf5ebc28f | -13.22013 | -54.33693 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bb214a5-6f15-3b03-8466-9ed57123d166 | -13.23552 | -54.32154 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f82311b3-9562-3aa4-bbe8-db242cfc3a0d | -13.19741 | -54.30715 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6ff7bb0-3b45-3fa2-975e-ed7b20c764b5 | -8.71787 | -54.54908 | 2026-07-05 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9562228-665c-333e-a682-c38d9b281d7f | -10.90099 | -56.85151 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 996da5ff-bbf2-38b0-9b72-3fe0f7538e21 | -13.21693 | -54.32761 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afc89d13-01bc-3741-bff3-b67987e808bc | -12.16875 | -54.53526 | 2026-07-05 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66157d8-d11f-3b22-becb-76b0ccd7fae5 | -6.99076 | -55.88688 | 2026-07-05 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a30ccd9-89f4-34ba-af6b-601b3b01fdb0 | -11.32044 | -54.47102 | 2026-07-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7dea1051-ebd0-3548-8eca-e6b7d223910a | -11.3107 | -54.47411 | 2026-07-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cc4616c-0f8b-3e72-b589-266646289e75 | -7.90121 | -48.25249 | 2026-07-05 05:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d87d5b3-253c-3f2b-a258-c62ed0aaedb6 | -7.90789 | -48.24882 | 2026-07-05 05:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2339ddaf-39a4-3303-95d7-87eedf02751a | -13.21519 | -54.34063 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b248c830-6041-36e7-bcf8-c8ce19e2a359 | -13.2393 | -54.32645 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0699d99-1ea7-3513-affc-74b6f76c1e8e | -10.08453 | -60.49355 | 2026-07-05 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d1ec328-c52d-3e33-9e42-a2a156ce0c43 | -11.43893 | -46.60013 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ac84b29e-d07d-32e4-bb26-79ac82db1ff1 | -13.22071 | -54.33257 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f737157a-b944-3c57-8b67-ea73f73a13cb | -13.22129 | -54.32822 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30bb8dfa-5da3-35b7-be8f-bc8291033a30 | -9.66545 | -67.21524 | 2026-07-05 05:23:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 444621ad-66d6-3c47-af84-fa3beed511c7 | -10.12223 | -52.08755 | 2026-07-05 05:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16a941bb-ce6a-38df-8019-d7799f458a63 | -10.90761 | -56.85681 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc976160-fcda-3f1a-8208-144e81dff5a4 | -13.22187 | -54.32387 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35df985a-ef78-3806-bfae-2ae17cedab44 | -11.31966 | -54.47136 | 2026-07-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34c8b7c-2f50-34f5-9747-6435f75df69a | -9.18665 | -58.06955 | 2026-07-05 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04a06f89-5dcb-3c9f-a9d0-26eddb4886f5 | -13.21577 | -54.33632 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffefe3ea-461f-3888-aa11-6c1a555a48e4 | -10.20109 | -54.95082 | 2026-07-05 05:23:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4416bf2-d7b1-3a10-a413-0175b2fdddc4 | -13.23437 | -54.33006 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 928476c5-b622-34e1-8194-de7c3d1d184e | -13.21635 | -54.33197 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fd3e8fd-40da-384a-a07d-590cbccbfa87 | -11.3115 | -54.47376 | 2026-07-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77741ad5-8be5-351a-b824-0eded64728d5 | -6.4291 | -55.79613 | 2026-07-05 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee523ac8-3718-3503-99aa-a43d3fde4e2b | -11.35795 | -62.44656 | 2026-07-05 05:23:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a56c35f4-d305-3bd9-a453-eac31d03d474 | -10.90461 | -56.85202 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54241407-10d1-3237-b287-b33f1b85f81a | -13.19798 | -54.3028 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 292b0eb1-a625-30b9-8c96-9809b909d10e | -11.43967 | -46.59375 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36833aa7-a344-3dc6-9543-c1a832c0edc0 | -12.15427 | -57.217 | 2026-07-05 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0c9625b-86de-365d-87ed-d520f7538f4b | -13.24366 | -54.32711 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d8e8391-53db-31d0-abfa-0b6d3afd4e06 | -13.23988 | -54.32218 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bb18697-49e7-31c1-b333-61f7ab5b2316 | -11.4382 | -46.60639 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 045b2a8c-b053-3d87-b29e-fb650b4be464 | -11.3545 | -62.44596 | 2026-07-05 05:23:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 53eace1e-b054-3725-a97e-1d2aca984ecb | -8.86136 | -62.21548 | 2026-07-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad25e239-94a1-36b6-9e48-7f3091636068 | -8.85434 | -62.21433 | 2026-07-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 38360f02-9a37-3b29-83d3-dce06a6c6f12 | -13.21751 | -54.32326 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de869192-9609-3260-9445-d24b2f738b03 | -13.20177 | -54.30778 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 020679ef-ef04-3641-87b3-879914e6e571 | -13.22565 | -54.32881 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39862cc8-b219-3277-9299-83b2dcb6427a | -11.43655 | -46.60741 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52f4ebe8-e8dc-3a1e-8431-3ffd9f558067 | -10.90337 | -56.8605 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38c9e5b6-775c-30db-a54f-2b00ffdb37b0 | -11.01127 | -55.24333 | 2026-07-05 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2cd3c62-6a0c-3c42-96d9-44027180f1f6 | -11.43794 | -46.59467 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c985924b-5072-398a-9b9e-10e1cef0562f | -8.86486 | -62.21606 | 2026-07-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fcbb007-6678-3629-a288-477c610064b7 | -11.43156 | -46.58789 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ca160e3-c6e4-33c3-81d0-b84d06a8219b | -13.23495 | -54.32579 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22d270d6-ae30-3583-97f9-3de5fe464e3c | -9.37357 | -65.77344 | 2026-07-05 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23b89197-6f83-352b-99df-0166f3bd8714 | -12.06391 | -58.0458 | 2026-07-05 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95b8a96b-0cee-3e4b-8e16-a16245fb237a | -10.96921 | -48.12658 | 2026-07-05 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1fc03c7-7c48-30e7-ae8a-638e3725d40a | -10.97352 | -48.12838 | 2026-07-05 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a685f7b-aecc-3ee4-9fd7-8b09260f171b | -7.02518 | -55.4376 | 2026-07-05 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90bead6a-2de2-3b4e-b9ad-d7c3418d9c75 | -7.388 | -55.4912 | 2026-07-05 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f483160c-84f4-3f48-b4f9-24ac4c438da6 | -9.36146 | -65.74197 | 2026-07-05 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa79d539-8379-3c6a-b5b6-6930be8a6866 | -10.90399 | -56.85627 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93056760-8dcd-33fd-ac33-672b24aac21b | -11.3199 | -54.47499 | 2026-07-05 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06db18af-975a-31c4-8d86-4aa93ed71fc8 | -6.42547 | -55.79557 | 2026-07-05 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d31b59c-809a-3a4e-9866-b5ef55260a0f | -12.16881 | -54.5359 | 2026-07-05 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0240ace6-5695-339c-9d18-55b27eea7fa5 | -8.855 | -62.2104 | 2026-07-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 793c5327-01e8-3dbe-ad1c-46aa63c51de4 | -11.43725 | -46.60102 | 2026-07-05 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eb157252-74cc-3182-8d08-1b0ca3efd626 | -8.8585 | -62.21098 | 2026-07-05 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 828545c1-4c87-33ef-b8af-021de3486083 | -10.49918 | -57.6109 | 2026-07-05 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b54c81-573f-3d1b-9234-7038e75b6135 | -9.24156 | -60.61965 | 2026-07-05 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8da1ce8d-a3c0-3fa6-8792-43f38df41cbb | -13.24424 | -54.32283 | 2026-07-05 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 143a52f2-a7c2-3b97-8cd6-4eac4a19408f | -11.6343 | -59.01215 | 2026-07-05 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e63636a0-a83d-3ad8-9694-b4faf0040db9 | -10.9401 | -43.0355 | 2026-07-05 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |


[Clique aqui para ver as próximas entradas](README9.md)
