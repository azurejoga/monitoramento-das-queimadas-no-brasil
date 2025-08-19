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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47f4237-8810-3612-ad03-e805f1626531 | -7.14664 | -44.20695 | 2025-08-19 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d87c4fe4-0c82-32a1-ba3a-59cfe8d9c072 | -8.70517 | -47.86604 | 2025-08-19 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aaa2f03e-7517-30fb-ad45-d4af1bf7410e | -12.29388 | -50.01218 | 2025-08-19 04:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a207d558-b5f4-37a7-8951-281198d63bad | -9.51756 | -60.53308 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4faaa26-8418-3fcd-bdea-7e1e6be98514 | -11.31183 | -55.22501 | 2025-08-19 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1d062d-bd26-3caf-a1d1-f57fd9c791eb | -6.42266 | -53.3713 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758f336e-5a63-3bd7-9e6a-567aa8156393 | -7.59426 | -55.46774 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2c0b05e-81ed-30ae-86fb-bfa595e71a05 | -6.19595 | -53.51992 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c4fe06-cfa0-3e99-b71b-5e0c1c3f877a | -9.81949 | -49.22173 | 2025-08-19 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ea649f-11e1-353b-9eb4-c17c16362285 | -6.49179 | -53.38956 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5967d4ef-738e-3d52-b7b3-c17a9ff5a180 | -9.51664 | -60.53808 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6171018-4cdd-3a02-95fb-81261de0a535 | -7.25542 | -50.17265 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbe58d42-b750-3794-a46f-9e6b919e12fb | -12.96092 | -46.15238 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90c76bce-bdea-3dac-8bef-16d7b784c970 | -9.19115 | -59.63111 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c201e199-914f-39ae-b2a0-389f1f77c97c | -9.23926 | -59.64464 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b8c2e3f-1261-3d5e-9f8e-2f8f2186e597 | -9.22439 | -59.651 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eebf082-cd0d-3d29-91a2-a57084fcf4fe | -8.89678 | -50.86645 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b5e7447-3d33-358d-bd55-14a0fae0c372 | -9.71493 | -51.97046 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97d29535-774d-330b-a1cd-b198f3d64fce | -10.58295 | -49.13272 | 2025-08-19 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3afa8c9-8dfc-354c-9551-4f42a795f86a | -9.51656 | -60.51215 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dabf5a76-9adf-3d6b-b308-6523ffb84f61 | -8.81928 | -52.05541 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05ca7d06-1c0a-37d2-b4e4-c03581e4e9df | -11.58926 | -49.01048 | 2025-08-19 04:53:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0e70a83-24e7-3e4b-a224-7c2f2562fd95 | -8.23444 | -47.85985 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 257d2c9d-9a5e-3ad3-b487-a42805f8d126 | -10.08474 | -46.35438 | 2025-08-19 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 159e21d0-505d-31c2-9c79-225fafd749e5 | -7.25661 | -50.16478 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1763028-5614-3acc-a2fc-5da6f012cfbd | -9.85441 | -44.68891 | 2025-08-19 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8732d243-6bd2-3ea8-bb51-b50df9208d7f | -12.64605 | -45.82301 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2aa5e1f-a63f-3bac-9eb1-d0ace4bea6e7 | -9.03715 | -50.1773 | 2025-08-19 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc9f85bc-b53c-3e5b-a275-06dfc64f7849 | -10.89004 | -48.49467 | 2025-08-19 04:53:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50edc41f-742b-3883-95da-1963b5204f42 | -8.40332 | -49.49601 | 2025-08-19 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc86562-50f4-3c81-b5a8-d0d453b8c842 | -9.711 | -51.97356 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 25ad3d27-abe8-3113-8c8b-6fab419eec5a | -11.75593 | -51.93999 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75dc44f5-194b-37f5-a8d8-2acac65b2b52 | -8.23798 | -47.86395 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f8ce238-22df-3f6e-9181-78f698837b8d | -7.79434 | -66.95679 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f862fe9c-9af4-39a2-b01b-98eb1b293916 | -12.04142 | -44.01557 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4992ead-0a83-3a08-bbdc-b58b7033f210 | -9.19484 | -59.63623 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f8bfdfe9-c3ae-33a0-9e62-6dc979f318f9 | -11.85624 | -51.57965 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03d20fd8-1017-3827-9804-b60cff7c7662 | -11.85971 | -51.58017 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f55d5ce-cb7d-30f5-8d9b-056f88f9b4cb | -8.88011 | -62.39477 | 2025-08-19 04:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73fc72db-5348-3702-9df3-ab9fd490d0d2 | -12.99443 | -45.18605 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8855db-b34d-3b87-81f4-e96f0d1bd8f7 | -12.29763 | -50.01273 | 2025-08-19 04:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd57063d-3681-36fc-92ab-3b9432fade4c | -10.80863 | -56.29017 | 2025-08-19 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef696e3a-5508-3dcf-856e-6a2f86c82c67 | -8.96859 | -60.49705 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16fcb797-6a5e-3728-9648-df524ea521b6 | -11.09048 | -58.94166 | 2025-08-19 04:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cd09b37-6196-3f4e-a3c7-cfd2b0b7ef15 | -7.78573 | -66.96262 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 472e2920-47af-3513-84c2-009a45c636a5 | -8.77169 | -50.01813 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e54561e-0f1a-353a-9138-94deb9db0348 | -12.99846 | -45.19622 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1812ce-7103-3459-951d-d2bf0e26b95b | -12.62749 | -46.88826 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a82dc5-a7e6-3d37-b3da-721ec9258f83 | -6.49513 | -53.39009 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26eccbe-c875-30c2-bcd3-fa4fd5bd999f | -12.5016 | -45.56811 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| beb59036-1d98-360f-90fc-1e333fbe0799 | -11.7491 | -51.9389 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d94d7263-3336-3179-98a2-bb778c4ae54c | -10.11018 | -57.76131 | 2025-08-19 04:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1283e654-e85e-3860-91d8-39f2a477a4b9 | -12.9634 | -46.15228 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c2594c1-d3d0-331b-98f1-ed66f8813c5c | -7.68407 | -46.75074 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab939c60-e7e4-3f44-88c6-9fbe0443f589 | -9.19562 | -59.6318 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2a32fb4-5f6b-3a84-bb15-278a9857adbd | -6.42209 | -53.37483 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57b598e5-3c8b-3f7e-a696-db770a8e1845 | -12.95724 | -46.12389 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4018259f-ff84-398d-a36e-aba02b3856b7 | -11.86663 | -51.58124 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4cdf15c-e25d-33f0-99c8-81ff3adb6c40 | -9.04788 | -50.1789 | 2025-08-19 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd968919-e423-3a4b-9110-7cc5a139083a | -7.25191 | -50.17215 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7002b6ed-1016-3bed-93d5-08129109b3a5 | -12.98769 | -45.19802 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0193f3ce-6f2b-3d3f-a668-c0aea4807197 | -11.34232 | -48.1275 | 2025-08-19 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 980199ad-4018-384e-a116-33c0a1ab79e5 | -7.06856 | -46.87842 | 2025-08-19 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94bc4fff-76d6-357c-a3dc-d17cec10306b | -7.29569 | -43.69504 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ccd64d8-0655-3be3-8f39-6487e4204a45 | -12.64331 | -45.80518 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51694c8e-5470-3a0f-8a43-9fd3bbcffd03 | -9.8552 | -44.6828 | 2025-08-19 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22b3faac-9c85-3028-a5a7-5551c61e4d38 | -12.92461 | -46.10812 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12e2501a-3a21-36d7-a524-5bf446e60406 | -11.81093 | -44.26126 | 2025-08-19 04:53:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ac1222e-a0c4-38a5-b8e1-7e44535f24c0 | -8.08578 | -46.66419 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de4c7b06-7247-3125-ae8b-32888f3bbbde | -7.59391 | -44.39891 | 2025-08-19 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b0ea7d1-3113-3f46-96ab-a17f273d3479 | -9.17567 | -59.61489 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f00b04b8-544a-3e4d-84ad-c32e26a61505 | -11.86375 | -51.57688 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ac094f1-7cd1-32e6-bcbe-72b661f2f5af | -9.14919 | -60.82631 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0696bc0e-75bd-325d-83ad-68dc3d666cd2 | -11.31244 | -55.2213 | 2025-08-19 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e36273a-d680-3104-9f24-513b2a1a8066 | -7.58438 | -45.42978 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ebf943c-5423-37d9-af12-b314679fdeb1 | -12.99808 | -45.19938 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e57a10a-d061-33a5-abd1-ee414afeee46 | -8.4017 | -49.49812 | 2025-08-19 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec5658dd-1c12-3e6a-a85c-09d379d11b97 | -12.88359 | -46.07972 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 418fd812-3d67-33f9-998c-2a609a7c4114 | -9.71437 | -51.97408 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| db24678e-0710-354e-96d6-89e8d048624f | -9.51274 | -60.52498 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c9e190-09df-3587-9247-5b9a8a200fc3 | -7.12046 | -50.4222 | 2025-08-19 04:53:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08c20fff-2186-3909-94a7-0c849b559339 | -9.19639 | -59.62741 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03f9ce07-2a79-3a68-81a9-6fe5de4722f3 | -8.82818 | -52.04229 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c66c2a3d-67e3-36a5-b72d-29af5e3143df | -7.14171 | -44.61071 | 2025-08-19 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9c42034-56b6-3bef-bd25-d169147f458e | -6.18923 | -53.51884 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48da0693-d936-3dc2-b79f-906ae194d2c8 | -11.80927 | -44.26171 | 2025-08-19 04:53:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 041e352c-26ef-3fc5-8c1d-a6ae3fd68953 | -9.53474 | -63.57718 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be182dd-13e5-3f5f-af2e-29b3522bdbd0 | -7.78641 | -66.96397 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ce5887c-4a50-38da-a8ea-bacde210302c | -8.70342 | -50.69267 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b09dfeb6-64f7-33fc-bbba-5c71d81372da | -7.58841 | -44.40123 | 2025-08-19 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4611e04-47c9-34c4-a1f2-aacc8d99410f | -12.65745 | -45.81273 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99ffb91e-cf19-30a9-8ee8-e8ef55658749 | -9.17123 | -59.61414 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6555ecdc-a204-3a3d-a375-1c7d53e706f2 | -6.19316 | -53.51583 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bbe764f-a4bb-3798-bc14-17ab5d7daa88 | -12.6393 | -46.89713 | 2025-08-19 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36352799-f921-3c3e-bc8a-26fdd23ed59e | -12.9149 | -46.10652 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2edda47-ff0d-3e06-addc-6d8d5c626726 | -7.58983 | -45.42544 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99b81db6-0021-3268-b66e-34e8f79bd7c4 | -9.1199 | -60.33115 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 193039e7-de34-3182-85c7-f8b1c1bf730c | -7.57894 | -45.4341 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4c7af88-f7d5-3f40-ac49-3b489ae724a7 | -9.54048 | -63.57832 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b6d245-b7e2-338a-9c4e-d72c0e3e4d79 | -11.86029 | -51.57635 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README39.md)
