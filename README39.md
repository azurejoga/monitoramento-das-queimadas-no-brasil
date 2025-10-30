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
| e3652ac1-3633-34d8-9af5-26be35227098 | -3.10511 | -39.61334 | 2025-10-30 04:23:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5581203-96f3-3e0b-8353-9b73c7c3e8b0 | -3.97384 | -45.42171 | 2025-10-30 04:23:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8a51dad-2fae-3e50-a990-7dde60c8ba96 | -3.36018 | -44.26419 | 2025-10-30 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 676d9709-1d43-3281-a146-e3862b19a856 | -4.63898 | -42.52809 | 2025-10-30 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3251c3d3-5d38-3920-ad65-20b2f0707e2b | -3.64933 | -44.71914 | 2025-10-30 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2fed46d-94e6-3c02-92d0-b191c02cac51 | -3.92344 | -47.6989 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 005d0548-841d-30d4-b257-810c60d78034 | -3.86861 | -43.35387 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e112e8a-fede-33a4-8524-e28b6d1cb871 | -5.30043 | -35.97884 | 2025-10-30 04:23:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 878118cf-6345-3636-a76e-86dd44f5ebdc | 1.95812 | -50.95316 | 2025-10-30 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4707d5d3-7ed7-348c-9905-2b39631ee0c4 | -2.93332 | -44.38953 | 2025-10-30 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7001228-d762-38fb-9952-b1086a66e68f | -3.28991 | -46.0507 | 2025-10-30 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3f8abd6-9660-3eea-ad11-8fcafc1814b8 | -3.8672 | -44.04171 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ad59413-b864-3485-b375-506d98068849 | -3.79533 | -43.89397 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7a79d3cc-a0d1-393c-a2bc-73c2e4d3ba67 | -3.84322 | -49.37577 | 2025-10-30 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a85dd8f-935b-32f0-8b49-3a70618d84a9 | -4.4413 | -43.23014 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57e4b6ae-1244-3c50-a8e9-52a271b1ea50 | -3.32365 | -52.62743 | 2025-10-30 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac61cc0e-002c-3e42-b2f6-80f02e3b2fef | -4.03415 | -47.77371 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30e822d8-ce10-38e4-a47c-324d7f707613 | -3.93122 | -44.19494 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0aa717f8-4c38-36c1-a606-cb56da7bcbfd | -1.33992 | -49.03323 | 2025-10-30 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 584733da-b35f-3a02-ad9c-3617728881ed | -3.13191 | -40.05191 | 2025-10-30 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d18c368a-ad79-34f9-b517-d3b4c7aaae43 | -0.73448 | -47.56139 | 2025-10-30 04:23:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 200fe528-6048-3d95-8f7e-2a4c9416b39d | -4.49026 | -44.02496 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7371cb9e-9ed9-3931-bb28-8a3e429f3136 | -3.96128 | -40.61518 | 2025-10-30 04:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 647cff0f-682b-3557-a65b-b240c376ace6 | -4.4303 | -43.37057 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c56fa1df-95be-3e02-8b1f-a3e4b2b3c116 | -3.08549 | -48.67752 | 2025-10-30 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bf0a87d-3ddb-3759-9f4d-d69dbe476cfa | -2.76872 | -45.39398 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ef455d9-ce06-36bb-a917-609205db04e5 | -3.84251 | -49.38021 | 2025-10-30 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe9bbb4f-158d-3cdd-8ad3-39e828287903 | -3.87155 | -42.77267 | 2025-10-30 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 632dd5b6-6759-368f-a52a-df7ff051503a | -4.15493 | -46.79163 | 2025-10-30 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af9a9294-8da6-3e52-93d3-ecd24bab9d39 | -3.86326 | -44.0448 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfaaa90-859d-31ea-acde-6971fecc73ac | -4.26845 | -43.71304 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee92e174-6035-389e-9abf-387d3e632a91 | -4.22436 | -45.57705 | 2025-10-30 04:23:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79eeaeac-0e31-3540-8d23-b857700c4115 | -1.14186 | -48.09434 | 2025-10-30 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72aabf85-59d5-3b22-82bc-0dc9720a2580 | -3.79816 | -43.89811 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41841be4-dd39-3e12-a2a5-7f3a5001b079 | -4.30515 | -41.43974 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b490b9f-f02f-3773-a93c-584368be383a | 1.61459 | -55.69246 | 2025-10-30 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef761839-31fc-37bf-8e68-c59379fd8531 | -4.05625 | -44.04485 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40a43ba0-9f49-3622-85a1-d8755abd8b54 | -4.43063 | -38.88245 | 2025-10-30 04:23:00 | NOAA-20 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02ea1347-7103-36ca-bb7d-7cff770c8573 | -2.31746 | -45.64687 | 2025-10-30 04:23:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7651ce46-cac4-3738-a398-1c640dfe80ae | -3.27105 | -40.03081 | 2025-10-30 04:23:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99f53ac9-3f7e-3212-8a14-97270dbc32c7 | -4.26277 | -43.70448 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4fb5d454-33c3-311a-aa46-df5c3cb859fb | -1.45704 | -46.71812 | 2025-10-30 04:23:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1661f494-194a-3d94-98f6-d5dfdfe27489 | -4.83619 | -42.73013 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0313fed5-fda7-33c6-8455-dc3b46de0b96 | -2.89633 | -48.06557 | 2025-10-30 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2737b82c-399f-3cfe-a384-76c68b8377ed | -4.05426 | -44.25811 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cb1aa83-34d3-34dd-991b-77c66e8148e0 | -3.70692 | -45.38998 | 2025-10-30 04:23:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ba2b48d-8779-3234-a8d8-a1a2ffdacada | -3.37182 | -48.9478 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb34c285-d08e-338f-b65b-453f5424c6f8 | -1.33687 | -49.02804 | 2025-10-30 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70359eaf-a1ee-3967-9ca5-74e79c029608 | -3.9886 | -43.41794 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28eed03c-7b61-3fd7-bab9-54f7328d2dbc | -3.80099 | -43.90224 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bca4011-6490-3dc4-b44c-d58d568da246 | -4.25533 | -43.70719 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 31df17f9-d75a-35d2-b58a-e17cc70b0c71 | -2.5724 | -45.79602 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbfcb712-e475-377b-a8d9-5f955fe1729e | -3.80155 | -43.8986 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6934753-44aa-352f-9648-5407a39c6d8e | -4.15677 | -46.79543 | 2025-10-30 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db2a2548-8263-315b-b069-08106e401754 | -1.3331 | -49.02744 | 2025-10-30 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8e8b3a-6c70-34c8-b921-e59f52ad894b | -2.37089 | -48.29662 | 2025-10-30 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0448914-5581-3a2c-aa14-bd9a3e5e4d6b | -4.67469 | -43.26389 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f25f009d-f3b1-30ba-9bba-8870c04871be | -2.66558 | -47.87532 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10162dcc-ef7a-3ee7-8874-afd6fe76d722 | -3.48754 | -49.89856 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0149cd93-1c83-3745-9800-f6bb29b1bb8a | -3.9491 | -43.25971 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f45aa97-11bd-380c-a6bb-5dfe65d15fa0 | -3.47587 | -49.92147 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8572404b-775f-316b-b112-74198643209a | -4.83259 | -42.72959 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d8980ceb-3e6f-369b-8fb5-b393e068514d | -4.15411 | -43.88469 | 2025-10-30 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7b13214-3929-381a-86f7-0c1930a91457 | -4.26619 | -43.70501 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| ab6bd73b-f22e-33c0-a7af-1deb65a30d1d | -3.86382 | -44.04118 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3a6ee7-d1c5-3ef2-83bb-59814c1ac147 | -4.26503 | -43.71248 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 56fcee92-6a83-317c-9d90-2f5a0f80f7fa | -3.12339 | -45.70632 | 2025-10-30 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e4f282d-2293-38c9-afd1-61583175e944 | -3.51315 | -49.71688 | 2025-10-30 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f96f8983-c1a4-3ee6-a26e-e1d6f10f32a9 | -3.62936 | -43.92066 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a1ff57-87bb-362c-beaa-da3d2ad213c9 | -3.63056 | -43.92091 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fadc1230-5b9d-3178-af4f-79fc2324e566 | -3.79024 | -43.90434 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| a2832d8c-21fe-36c6-a537-52e964ad93fb | -3.97474 | -38.73162 | 2025-10-30 04:23:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 307e706b-47e1-3290-aa0e-e86be5faa388 | -2.77202 | -45.39449 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 419da677-a70b-3e86-83fe-feceecd99724 | -4.01026 | -47.42014 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 589d1151-701e-3f7f-8283-f0847e7ddbfb | -4.829 | -42.72905 | 2025-10-30 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3eed4341-cfe9-3da8-8399-33b936f47a8a | -2.25288 | -47.02411 | 2025-10-30 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00286236-331a-3774-a350-cc9a71e3e0b6 | -3.7908 | -43.90071 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 63c85746-d4ac-3908-a2d8-18d637577c2e | -2.76488 | -45.39689 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6337985f-e3e7-3e30-82d1-5dc8be638bad | -2.76818 | -45.39741 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fbc2fe71-89f4-3647-9c35-04318b93e4a1 | -3.08611 | -49.50425 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e26b2fe-b0a8-398e-8c68-9ac6143141d1 | -3.80608 | -43.89185 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11fe50b7-1766-390c-a2d4-9b81482e607c | -3.08687 | -49.49962 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90d2659e-6eff-3893-9a57-242842b3d9e7 | -1.33614 | -49.03263 | 2025-10-30 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dad6ee8-1e24-325f-93d1-1ad267064ca7 | -4.43064 | -43.43713 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7e12c0b-572f-353f-b480-c44b6222d205 | -4.01771 | -44.81916 | 2025-10-30 04:23:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a6aee20-0368-33dc-96a0-a4065c3ab19f | -4.07731 | -44.37473 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f86056f6-5619-3d9d-ae89-be6f19e84e2a | -4.15734 | -46.79189 | 2025-10-30 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d7a6c5-e7ee-3f0f-9226-21db59f1d8db | -1.63187 | -54.2168 | 2025-10-30 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e0c4290-212d-35a9-9fe2-9e277aea9ad4 | -2.43418 | -45.51021 | 2025-10-30 04:23:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ed0eb5-795c-3588-93a5-9713aaa33ff2 | -1.52821 | -54.44683 | 2025-10-30 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1cde576-adeb-3cc3-b527-734814c2aa3d | -4.25133 | -43.71037 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f55a2c3-9043-34b8-8e0e-9909e9f548df | 0.29195 | -51.20381 | 2025-10-30 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06112b97-c983-3670-acbe-5a7950ac0269 | -3.36401 | -44.78487 | 2025-10-30 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7beedda3-b8b5-32af-81e7-f6bb29cb6a41 | -4.47034 | -43.4458 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 30388b76-9e70-3d50-a18d-823f83825cae | -3.23111 | -46.87248 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d964fc5-53eb-363d-8388-698feeca0f49 | -4.30588 | -41.43498 | 2025-10-30 04:23:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8510a13a-cb25-336a-892c-15028efce972 | 1.17002 | -51.26322 | 2025-10-30 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f286eb1-be45-3854-9417-560e81dda1b3 | -3.69175 | -47.63652 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a6935bb-5689-3eac-a908-df58a39abd79 | -3.33656 | -46.2075 | 2025-10-30 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ae3a6fd-3daa-3c9f-9917-77c47d513643 | 1.89899 | -50.82329 | 2025-10-30 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
