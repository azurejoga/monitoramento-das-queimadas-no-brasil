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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9ed6252-56ff-3096-bc19-cb7102b88982 | -9.7999 | -59.103 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 845bd90f-b22b-32f3-9856-585f1157a303 | -9.51507 | -54.63382 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ff6b7c26-837e-396e-8833-bd92e319242a | -10.26922 | -57.79964 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de72248d-b7bc-3854-bd3e-572a9aaabf93 | -9.51574 | -54.62811 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8ce78861-a9d8-3b3e-9564-985841de8e01 | -9.7966 | -61.51178 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82f849d8-4273-327e-b3de-d49bd68142e4 | -9.52187 | -54.63449 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| bca25968-df7a-36a2-b8cb-2b83c5489ae0 | -9.88717 | -58.33282 | 2025-09-13 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51ebe670-a66d-3877-8ee1-2434e3d73537 | -10.09909 | -59.16736 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c62f7e45-a6d1-31dc-8f1c-4c5eb739944d | -7.85637 | -61.17481 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec337c3c-7da0-3b14-b270-8dd1f60b7207 | -9.72486 | -64.92507 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbb5e07b-1953-3983-8766-86f3dc7025ed | -9.25861 | -57.06871 | 2025-09-13 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9815ddc0-e535-3601-8186-a6c2d9127ea1 | -9.79347 | -61.51466 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8a732a8-6fa4-35cd-b1e1-e84d5db1acf6 | -10.09991 | -59.16132 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721e7ca9-d553-3950-899a-f07db6ca01b6 | -9.79477 | -59.10241 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 630a6c25-511d-321c-a65c-26719100ad4c | -9.73731 | -65.01204 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5117895e-827b-3404-971d-3387d1608f42 | -10.09869 | -59.17035 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bc1345c-ca96-3730-a83e-764054903920 | -5.29417 | -60.10836 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c86c594b-5bef-3ed4-a1ad-14d17ab92414 | -9.27075 | -59.40948 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 635c54fe-50d0-3af2-983b-fc92398b1f26 | -9.48483 | -55.97362 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fd27a76-e1fe-3cc7-898d-1a89bb32d7fe | -9.30494 | -65.58752 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8507e606-b68b-336a-b020-ef2407ac0a56 | -9.74025 | -65.01654 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bee66a43-c434-37ef-8c37-093d9f0b2645 | -8.5424 | -63.99748 | 2025-09-13 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a23d4a-c5fe-3e59-90aa-4d3ecb146307 | -11.23094 | -55.00349 | 2025-09-13 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61fd3f10-789d-39a4-814f-5f5e54e784f4 | -10.33032 | -58.02058 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf14aa49-0459-3719-9ce9-6e04dfe944e3 | -10.33539 | -58.02502 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92827af-b31f-3739-899d-fed42438a86a | -9.30381 | -65.59502 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aef60fc-c562-39ab-b007-46e8a4d19749 | -10.00336 | -59.97909 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f661cd-0cf8-3f14-ac19-14751a3a88e5 | -10.15037 | -64.73625 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed55bf9b-0f47-3069-88eb-2cb28e0cf24c | -9.49929 | -55.9596 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3ae41b48-0c78-3f61-abc2-051e461f9662 | -9.72425 | -64.92909 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88afc157-ad21-309c-a5ab-ab65556c01d4 | -7.86187 | -61.16715 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b59452fc-8644-3f5c-b439-6728d7d31156 | -9.23792 | -65.79859 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b594149-070f-303b-a737-d389da0ad867 | -9.7329 | -62.3523 | 2025-09-13 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4b086d0-13e1-31b0-b14e-b83233270f69 | -9.82683 | -62.33168 | 2025-09-13 05:48:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1749cf1-bddd-3de7-8b71-b6fb0116562f | -9.30522 | -65.58812 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 267d5247-1dc1-3cf7-ad96-1290ac4cf9d1 | -9.74084 | -65.01257 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04b267d7-13be-3977-b2e2-cd773ecfd6dc | -9.49803 | -55.9697 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 33426fc4-289c-3732-ad33-ba657ed4f8b2 | -10.70735 | -54.44526 | 2025-09-13 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dd0eeda-a36c-3467-8b26-7ba62c96ed2f | -9.49176 | -55.96898 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c1b08c4-1944-3cf6-bb4c-57a3ab64cd24 | -9.81025 | -61.5213 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125c8047-a630-3d1f-a714-39f5610e300e | -7.85696 | -61.17068 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a23d9fa4-e76f-300c-ad00-8cdcae6bc613 | -7.76036 | -61.12434 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 113faaa2-4c2b-30b2-b242-f0eb0c0d54a7 | -9.29836 | -65.58706 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f3c8ca7-9f98-31a5-a71d-d69677589035 | -9.86618 | -63.40639 | 2025-09-13 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3abe2dba-25d0-3ec8-a499-11fce912480e | -7.81721 | -63.5769 | 2025-09-13 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d62ecaf-a2cd-3b27-acd2-e21b3a7dccd3 | -9.50428 | -55.97055 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ad70dc8e-6197-3546-a6d3-92265d862b96 | -9.4924 | -55.96384 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f097a408-2088-356f-b058-8cc26d0eecc8 | -9.99927 | -59.97308 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 477d2279-4307-31cc-9242-bf1e8eb47cdb | -9.88988 | -58.33691 | 2025-09-13 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10aefcfa-3723-3702-89b7-45a8fb64d7c3 | -10.00359 | -59.97048 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8d321fa-9d43-32e1-baed-4dc7519bf3d9 | -10.33707 | -54.32023 | 2025-09-13 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 897af58e-0c76-38c0-895d-f7d4d90fb67e | -7.6677 | -61.17051 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06768a8c-1490-3ef8-810f-78a3d1a93d70 | -9.72011 | -64.93255 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db540e51-1723-3d56-be7e-04cc76244e68 | -9.4974 | -55.97475 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b0bc6a94-8adb-333d-bc2f-2b6b9d67869e | -9.26004 | -59.4138 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 37f9c591-e51a-3602-ad49-adbdbfec7306 | -10.1474 | -64.73158 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 927ade18-11df-3e0d-86ae-dca2ddab8827 | -9.26999 | -59.41515 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 647f1aeb-1d8c-3588-b6f3-e6fc470dd39d | -9.88449 | -58.33619 | 2025-09-13 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4a2fc2-273e-37dd-ab12-058b121dd4a8 | -9.96482 | -64.96308 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b08419-b0d1-34f4-9225-dcc713cb945a | -10.14802 | -64.72747 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77d2dd32-5bab-314e-9953-6799fc76cf1f | -10.09438 | -59.16368 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93b67412-80d6-31bc-af15-0f8393118674 | -10.0041 | -59.97377 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bc3a674-883e-3a8e-a646-4d54a3cc3d1e | -9.79404 | -61.51046 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81e10174-8dd9-3b07-92e3-fed66e66eb35 | -9.26158 | -59.40233 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2a4503cf-1a4d-39a0-94c3-2f93d5edfa5c | -9.26655 | -59.40305 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| cfab8cdd-53cf-3900-bfb9-ff35dca7c74a | -10.10032 | -59.15823 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad8eb4e-8be9-387c-8d2f-feac6c442a2b | -9.51939 | -54.63944 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 0a7abd80-1ca4-3392-b0cd-ba0a33711e09 | -9.55524 | -66.73301 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fbbd8a2-0d97-3f5a-99ab-a33aa3a55b4b | -9.79735 | -59.1021 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa8d62ca-d1b4-3a7e-abb6-ce3f39d6ab07 | -9.50492 | -55.96538 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7435736d-87e2-316d-aab0-c46791678538 | -9.03933 | -65.40155 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eeac05ac-6206-3982-a1c4-4280113dd6ff | -15.1359 | -52.4892 | 2025-09-13 05:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b42cc8ab-dc47-3619-94dc-f5038ecbe5bd | -9.2656 | -59.4191 | 2025-09-13 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 47dd9bca-fcc3-32d0-bbe4-fcca49e681c4 | -9.2658 | -59.3997 | 2025-09-13 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 6f8e067a-51b5-3503-b1a3-6bb2a0f30187 | -21.0633 | -48.9356 | 2025-09-13 05:50:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| df67a2cb-bd53-3ffd-89b5-204c2daa87c9 | -10.1611 | -64.7401 | 2025-09-13 05:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4b4cd475-0430-3100-843e-9315c287f412 | -12.8637 | -62.14054 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce085b1d-d5ff-37f9-95ed-24e2ed95db3b | -11.79374 | -62.73656 | 2025-09-13 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| da08e920-0414-3c3b-a11a-98bfedd08c45 | -12.86875 | -62.10237 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043c3119-fd06-3ae6-acf0-8ad0b7673d39 | -12.89225 | -62.09258 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619a2e3e-7153-3a47-b7a7-eb370055f2eb | -12.86538 | -62.12785 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1bbd94f-61da-3e81-a05d-9424969f86a5 | -11.77447 | -64.93869 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b91bb50a-c2c0-3a5b-87b2-11491b38404a | -11.77746 | -64.94342 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 500ee641-9d36-385b-b6fb-cd0c0985b213 | -11.77149 | -64.93394 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cedd971-e6a1-3600-ad09-8eebca65c05d | -10.66276 | -65.20033 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01bee560-1c02-32ea-b10b-15bb38f03fa5 | -12.87561 | -62.15084 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad53bda9-8755-3fd0-9466-74bbb03428b3 | -12.87448 | -62.15929 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a43019-131e-3050-a2a9-6871516f6508 | -11.38025 | -63.36091 | 2025-09-13 05:50:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f221ca0-9409-370c-b8e0-186d787b5a2e | -12.38689 | -62.20951 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9f82ac7-1d10-3553-980c-611527b27473 | -15.20392 | -56.67979 | 2025-09-13 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4da9657-6216-3dac-9b37-54882e6195e5 | -12.15799 | -60.73991 | 2025-09-13 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4692980e-6541-373b-9487-3652329aef25 | -15.20339 | -56.68507 | 2025-09-13 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 199a6edf-59bc-39ea-9fcc-59f1984cf795 | -11.77024 | -64.94236 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d58a9c35-c919-3844-bbad-a1f8845beac3 | -10.98285 | -68.51455 | 2025-09-13 05:50:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19dfaa2b-7723-3731-9d0b-0ce4251301f7 | -15.21562 | -56.69229 | 2025-09-13 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33595412-a65e-302b-9b01-d70429ff9911 | -12.3852 | -62.20782 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0033f9e-bd54-3b7e-a26e-c5ef7e7c6252 | -15.58888 | -54.77217 | 2025-09-13 05:50:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34e88d41-65d2-3da6-80f9-670743fa2e81 | -14.38895 | -60.28901 | 2025-09-13 05:50:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89fbf7e3-9a3d-3ee9-a075-388d7cd7456d | -12.86258 | -62.14902 | 2025-09-13 05:50:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acfd0ffa-7126-3e12-9dd2-8ab2659fc261 | -11.77385 | -64.94289 | 2025-09-13 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README115.md)
