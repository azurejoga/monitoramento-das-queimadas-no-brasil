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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 696201a3-6a0d-31dd-9b7d-5a9c0b6d3719 | -9.5936 | -49.278 | 2026-08-26 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 240.8 |
| bd191657-7ffe-3335-a22e-d036ac8151cf | -11.7544 | -54.5414 | 2026-08-26 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 5373cf24-ddf5-3998-951d-9476f725cd78 | -9.5748 | -49.2799 | 2026-08-26 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3a3e6a8d-0b11-361d-917c-774619aafcaa | -8.5962 | -54.8563 | 2026-08-26 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9746df97-7561-34ec-865f-e022a4d47cf9 | -10.7598 | -54.0179 | 2026-08-26 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 22fad13d-1368-3b24-81c2-aa96469d4c06 | -8.8187 | -49.6093 | 2026-08-26 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| e695b2db-e054-3328-b1ef-1002be42d88f | -13.264 | -51.5205 | 2026-08-26 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| bc01fbbb-725e-3781-a6bf-6bfa4dd6b590 | -12.6836 | -48.4116 | 2026-08-26 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 02f3236b-e6c5-36dc-a3f6-b7dd106ac81e | -7.6461 | -47.1258 | 2026-08-26 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 341.3 |
| a96f04b6-5fa2-3780-b2bb-8fc986b6b37d | -9.6024 | -55.1078 | 2026-08-26 13:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 43f3bc94-e7e4-3140-bacb-760594d1d92c | -11.7736 | -54.5191 | 2026-08-26 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0fc25896-7a30-3ec1-af46-9ecdb008980c | -3.79 | -59.284 | 2026-08-26 13:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6ed1432b-3e00-3aca-ac5f-fcbaa85b081f | -4.8002 | -43.1709 | 2026-08-26 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2705d802-3699-3c2f-a1e3-8f7cac18395a | -14.3368 | -51.7448 | 2026-08-26 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 69c32127-bcd6-3ce3-bc36-8da137f08b64 | -9.7246 | -49.3512 | 2026-08-26 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 73fccf75-ed11-3cb8-aa20-cbd4ce9329d8 | -3.2178 | -61.2362 | 2026-08-26 13:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 194b5add-f005-398c-9824-2f350a38e015 | -10.7784 | -54.0368 | 2026-08-26 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e83022c7-49c7-3e73-beaf-8de224e314bc | -7.385 | -55.1523 | 2026-08-26 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 3748cd3a-7e1a-3d93-b0db-a612194329ac | -3.7717 | -59.2844 | 2026-08-26 13:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e6f06fcd-1646-3e82-b263-36a6611cbe56 | -9.7249 | -49.3296 | 2026-08-26 13:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| da7ff2e1-6784-3374-a11e-9f17d58ff8af | -14.3751 | -51.7611 | 2026-08-26 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 9c5a9d59-ef58-383a-871f-69236b7135f8 | -11.7733 | -54.5396 | 2026-08-26 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 94c6ec44-2b9f-3b79-a8d9-3a18cceb8062 | -8.1484 | -47.4998 | 2026-08-26 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 63583720-744f-3eef-9ec4-e0225181bbd7 | -9.6776 | -55.082 | 2026-08-26 13:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 99f9f779-820f-3a64-864e-d488bf7aab10 | -14.3179 | -51.726 | 2026-08-26 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 50a3f36f-b1ce-3743-b141-793d724ee8fb | -11.7546 | -54.5209 | 2026-08-26 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 208b67a9-f039-39f7-bbe1-c5ef6866660e | -7.6649 | -47.1242 | 2026-08-26 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| cd5661c2-3249-3957-8d8a-55dbdda3836a | -6.2676 | -53.3768 | 2026-08-26 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 09f46945-6a06-3d41-b967-4d129f981d93 | -10.7596 | -54.0384 | 2026-08-26 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 198.3 |
| a427afec-c92c-37c9-84a3-73f021e9181f | -9.9506 | -46.6251 | 2026-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ae290fb9-e619-3cc1-91d3-9685c57173d3 | -8.9418 | -45.748 | 2026-08-26 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8dc0ada2-aad7-3f9d-b602-83a22dd317d3 | -8.1482 | -47.5218 | 2026-08-26 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3dc2df28-a972-365e-8e7e-303586fbb9b1 | -12.6452 | -48.4168 | 2026-08-26 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9ea7cfdc-c434-3a93-a888-5ad7f6a6f031 | -7.1309 | -42.7945 | 2026-08-26 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 9c95fea7-900b-38fc-a161-1e5255f5ade7 | -12.1422 | -43.3707 | 2026-08-26 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 51387694-24f1-3c45-988d-d1c694c65411 | -11.7546 | -54.5209 | 2026-08-26 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 219.0 |
| de1ed959-4d44-3cbf-a720-0415499e77b4 | -6.1169 | -53.7501 | 2026-08-26 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 459e4960-add1-3837-9efc-038fc268e982 | -8.5363 | -55.3027 | 2026-08-26 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fd4281be-8857-3f34-a817-73593ee61045 | -14.3175 | -51.7474 | 2026-08-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b39e7ba5-d323-34ca-82cb-fe9966255562 | -11.7544 | -54.5414 | 2026-08-26 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 200.2 |
| ec9976d5-171a-36e3-8478-1aec7acadd5b | -10.7596 | -54.0384 | 2026-08-26 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 12b35d8f-50a6-3635-8784-ac769ca6e118 | -11.7733 | -54.5396 | 2026-08-26 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 272.9 |
| b952d02e-8f33-3a53-a4b1-79ebf223aca9 | -8.9418 | -45.748 | 2026-08-26 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 304.8 |
| 9ba4cf02-0b75-3f8f-a44c-311390973e67 | -14.3179 | -51.726 | 2026-08-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 069da27d-68a0-367a-804f-0ce7edee0b32 | -3.2178 | -61.2362 | 2026-08-26 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 135.7 |
| d681f684-264c-35a4-9e31-87363fc9bacd | -3.7717 | -59.2844 | 2026-08-26 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b218f974-7fc2-3ef5-99b4-f674a0136894 | -7.1312 | -42.7708 | 2026-08-26 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 3b5406eb-8cb7-3e5a-a3e3-82d551cf81a3 | -6.8358 | -59.9379 | 2026-08-26 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 81cb8ade-57b9-32fc-8250-8fa759b941e4 | -8.6344 | -54.7528 | 2026-08-26 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b90ed2cd-5f88-3734-a621-fbc0c10fc753 | -12.1417 | -43.3945 | 2026-08-26 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| ffc79d60-a43e-38ef-8e0f-2e7447997b06 | -8.9421 | -45.7253 | 2026-08-26 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f1bd3bf9-fc8b-3c14-9606-dd14fed46cbb | -12.6832 | -48.4337 | 2026-08-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 1ce2e3d9-c081-35ae-acbc-a3717b0ee661 | -9.5936 | -49.278 | 2026-08-26 13:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 4844d2d1-7ef9-3c33-970f-47c46ffa10e2 | -9.5748 | -49.2799 | 2026-08-26 13:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9826f438-18c8-3bca-8366-bc3acd9715ec | -12.6452 | -48.4168 | 2026-08-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 90969fb2-578e-33cb-9276-26a273f7d3fd | -7.0236 | -45.7303 | 2026-08-26 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 01a56793-1b75-3964-b965-d9bc20aa0454 | -9.6588 | -55.0834 | 2026-08-26 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7e3e6f2f-3340-3eb8-b23c-16f4cb3b73af | -7.385 | -55.1523 | 2026-08-26 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 31df4147-d5cf-3964-8f87-355c07e3d0dc | -6.2676 | -53.3768 | 2026-08-26 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1a51c5ad-f944-304d-90d9-23669a6dcd65 | -15.5543 | -47.106 | 2026-08-26 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a4a56054-203d-3960-9291-af362bc1cada | -14.3368 | -51.7448 | 2026-08-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| fa005f01-7ccf-32a3-bc9d-8dc7f3d35a96 | -9.6024 | -55.1078 | 2026-08-26 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 8bbd454e-e1ff-3841-a361-8f71e44e3f53 | -12.6644 | -48.4142 | 2026-08-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 645db006-f2ed-3aee-94b5-f6e0a068945e | -12.1229 | -43.3738 | 2026-08-26 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| b3dfe59c-86a8-3acd-9fe3-7ac6629b7b3d | -3.2179 | -61.2174 | 2026-08-26 13:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4a8e3967-1ab9-391a-bab3-c3a7c2722125 | -9.6776 | -55.082 | 2026-08-26 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1e95b90f-03b8-3512-a015-014464b47095 | -3.79 | -59.284 | 2026-08-26 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 3aea1c7e-a4bd-3456-924f-3b14a239c20f | -9.7246 | -49.3512 | 2026-08-26 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 211.4 |
| b32da38a-9260-3d9e-8211-f4fa2657f4ed | -7.6461 | -47.1258 | 2026-08-26 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 3a8f654b-d2af-3198-bfc8-d08e63e5f020 | -8.8187 | -49.6093 | 2026-08-26 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 01f7daf6-4be2-3c92-b446-5a385d9f67c8 | -12.1422 | -43.3707 | 2026-08-26 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 89e894f5-921c-3f8d-a434-8a3b116b0e4a | -9.7249 | -49.3296 | 2026-08-26 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| cabd2ba0-95d2-3823-a8af-83b9813cd715 | -12.6836 | -48.4116 | 2026-08-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 286.3 |
| bd586149-5c8d-3228-950b-9d5ca13b6428 | -7.6649 | -47.1242 | 2026-08-26 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0a40c5cf-73e4-3768-9633-f594b65d9ee3 | -10.7598 | -54.0179 | 2026-08-26 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| bb53c8b7-15a9-345f-8263-e93c20335f2e | -4.8002 | -43.1709 | 2026-08-26 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 27d5ca37-52d7-3be0-b319-2e4cd5546864 | -8.1482 | -47.5218 | 2026-08-26 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b8a59b6b-6950-31f7-929c-76cad026c0af | -11.7736 | -54.5191 | 2026-08-26 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 372.3 |
| 74563e8a-1ad3-3b03-be51-ef0cdb387e6a | -7.1309 | -42.7945 | 2026-08-26 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| ed100c24-c908-3669-9982-23a092733322 | -10.7784 | -54.0368 | 2026-08-26 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 9f0a0918-064b-30c4-8b0f-38c7af960073 | -7.3849 | -55.1723 | 2026-08-26 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8509097c-2663-3904-8c55-329e7e09920f | -12.6452 | -48.4168 | 2026-08-26 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e92fcc0d-9cc8-3ad6-8f61-8e2556549746 | -11.8165 | -47.6647 | 2026-08-26 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e119e291-3a57-3680-bba8-1ed9e43a043c | -7.6649 | -47.1242 | 2026-08-26 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 013fae67-ebd5-37a8-8d65-cb66b4f480ad | -13.2835 | -51.4968 | 2026-08-26 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d5d32e43-6ae1-32e2-933f-261741d2f691 | -8.1484 | -47.4998 | 2026-08-26 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c007ddd7-e425-3333-ad83-7e55181c2562 | -7.0234 | -45.7528 | 2026-08-26 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 74c9cd8c-5851-3365-a6f4-051331711ef9 | -6.6409 | -58.5181 | 2026-08-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 86029d8e-bc70-33fb-98e2-70f5886dbf39 | -13.3031 | -51.4731 | 2026-08-26 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a23fb482-991c-3648-929f-1eb6907b2fda | -8.5361 | -55.3228 | 2026-08-26 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f66e80de-a42f-3325-a5e8-4d1e35a8c23b | -14.3179 | -51.726 | 2026-08-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 60016773-2022-39de-923e-1da46c6f0b58 | -6.1169 | -53.7501 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| af309cd7-f269-38ef-bcfe-956e8ae2f2da | -13.264 | -51.5205 | 2026-08-26 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 3361e23c-0455-3635-9bfd-16b26aa18c55 | -6.1743 | -53.4834 | 2026-08-26 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 87fe0785-0b46-3861-bbb9-542963b66d28 | -3.2178 | -61.2362 | 2026-08-26 13:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9208b469-0a54-3b28-827b-522f6b8bfa78 | -12.6644 | -48.4142 | 2026-08-26 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 69ca4bca-5cf0-3838-945f-de91a938d079 | -10.7784 | -54.0368 | 2026-08-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 2772f6e0-403f-3f5a-8a9f-fba5af43c664 | -6.0353 | -58.0376 | 2026-08-26 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 754e6c22-842c-3a28-acea-1e4c3365d4ba | -14.3368 | -51.7448 | 2026-08-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| cd452e8e-f29c-31dc-9e6b-647bff6d308f | -9.6024 | -55.1078 | 2026-08-26 13:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |


[Clique aqui para ver as próximas entradas](README82.md)
