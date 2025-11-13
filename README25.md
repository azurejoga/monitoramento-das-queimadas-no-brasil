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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f1e9e6-3ed3-37c6-a442-12f22cbd5ffb | -3.09761 | -49.27514 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05c9ecc5-5d3e-33bd-8aab-a72ea7dd7da9 | -2.31498 | -48.44768 | 2025-11-13 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8feceb9-425a-3baf-b4f0-71d77cf91a04 | -7.39328 | -43.32745 | 2025-11-13 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4237ca68-ad1f-3e89-aa82-62e1df02e9b9 | -3.10656 | -50.19827 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aaa7793d-c5c1-36e6-9b3e-69b75b294e4a | -7.06247 | -41.58677 | 2025-11-13 04:42:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 933bbeba-f5e6-3fae-a07a-5e30babe2eba | -4.70873 | -47.01309 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2801ed96-49a2-3585-b5ca-9e230c7f7caa | -3.08777 | -49.27712 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0dbdd958-73b0-3506-861a-55bb14f00056 | -7.06382 | -41.58368 | 2025-11-13 04:42:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c99f9dd-639b-354e-a5e1-abf9da1a077e | -4.24342 | -48.38533 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c954301-ecac-3cea-bd7b-e551737e2353 | -2.72627 | -47.40951 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d766531-616c-37fe-bd6d-de72d7080c53 | -2.72347 | -47.40544 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1952498-25ca-36a5-91b2-cf998c185f73 | -4.10531 | -48.01664 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52e8e782-e566-34db-8b08-aa7e1bcbda78 | -7.68633 | -45.8823 | 2025-11-13 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474b9253-6cfb-3319-9a50-7b7d740534f9 | -5.72714 | -43.52946 | 2025-11-13 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42aa55bb-c945-3373-8856-6551062adb90 | -7.55618 | -47.24664 | 2025-11-13 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0909a26f-977f-31e2-bfdf-47b11db552f9 | -3.40094 | -50.1743 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d0de8f2f-e831-3416-9e1a-1031fb2cf54a | -2.14449 | -53.64772 | 2025-11-13 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d37f7db4-752c-33f7-982b-9a95821ae565 | -3.21246 | -50.19263 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aca7dff5-bfc1-3d81-9170-136c110a34fc | -4.36937 | -48.70677 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37e31cbc-2b23-347e-ab9b-7af8fbc0ea5a | -4.21066 | -48.57203 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f1b89dc4-97f2-33e8-af20-260a958c7ca9 | -5.6144 | -41.06949 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7032ce5-2dbd-3f0e-910e-7a7a1f74bd50 | -3.46892 | -50.59815 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b890b71-8aee-37b6-a932-7680587a10f4 | -7.11627 | -42.7207 | 2025-11-13 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 358bb075-91f2-38fe-ae25-e0e00c73717b | -7.25923 | -45.3725 | 2025-11-13 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 335954e3-bab2-3821-94d9-1cc56b2275d0 | -4.45568 | -46.55484 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b514c2b4-e9cb-3687-9c99-8b132eb7556a | -4.61497 | -49.29081 | 2025-11-13 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8600ad8-b896-3e48-b2f1-c7b7728b21ed | -2.55945 | -48.20667 | 2025-11-13 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ca53cc2-2bd7-38fd-aef7-b6626266af76 | -5.64872 | -41.0807 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6032db2-b136-3fb2-9225-820d40f10f60 | -4.71378 | -46.44807 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bfe13597-08df-36d1-8216-b55717ea6eb9 | -2.43339 | -48.62157 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0de509e-ed73-3383-872a-7ab53b4a2ce5 | -3.14313 | -50.27444 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f459a68-9dce-359d-9e04-c5ca463daed1 | -3.72237 | -50.52079 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ffb6b97-6c07-3702-81c4-8b7ff0806e41 | -5.32712 | -44.78729 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbb3b544-4a45-356c-8881-d868cb5a2778 | -1.42842 | -55.70711 | 2025-11-13 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4dd6801-929c-3c4b-a1a7-a115734bb017 | -4.30748 | -48.23837 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2585ea8-aec4-3e5d-92b7-d1dcf0a335ef | -4.75455 | -48.83829 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5a8f36dd-0220-371d-89ea-e566a30966b8 | -3.56971 | -44.16088 | 2025-11-13 04:42:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 527ebf2d-06a8-374b-8128-d06df188eb11 | -5.838 | -47.56264 | 2025-11-13 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1722cbdd-34c6-328c-90a3-fc2140486f96 | -6.16 | -48.05053 | 2025-11-13 04:42:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eb618b8-0d48-3495-ad04-1430f0f21f1a | -3.46423 | -43.17913 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 906dab72-0eb8-3755-b026-904c51954157 | -5.38539 | -46.76541 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb0a6265-428b-320f-99b3-f66f2bd4e0d9 | -5.67751 | -51.13956 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bce7dff8-bab1-3981-a8b5-cfaf378d4284 | -3.38186 | -50.13422 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5749e75-2ab4-351d-9bb9-40ad87c81a52 | -2.37513 | -49.41457 | 2025-11-13 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fed27687-a1d2-3813-98d2-d5ad2d26fe3c | -2.71955 | -47.40845 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8c163b8-696b-3dbd-8f1b-6d5627bd7365 | -3.98585 | -48.00176 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 943b8769-0186-3ce7-851c-b28cb3292024 | -3.86577 | -49.79245 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5c99461-dcaa-3f14-993d-6ed5a9298f3b | -5.46784 | -47.0485 | 2025-11-13 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ddb1db2-9bfe-3268-a19d-f2a9ec89e4d5 | -4.10476 | -48.02015 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a9780b0-5ae6-38bb-8c0a-20d4c94bd110 | -5.74752 | -42.73731 | 2025-11-13 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f6b41f2a-61c3-3bd3-ba24-b6143e4f04fc | -7.0913 | -45.45679 | 2025-11-13 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76301c22-f376-3bb9-b9ae-cb52ab8864ff | -3.2251 | -45.59493 | 2025-11-13 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d50aae5d-0146-3173-86ad-1f32c3039410 | -6.16337 | -48.05106 | 2025-11-13 04:42:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92e76039-afcf-34c9-9bb2-ecab4d2bfe36 | -5.3895 | -46.76208 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d07aa487-3618-3581-81bc-c2492763c7d8 | -4.18478 | -50.33715 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac2e93e9-ed7f-345e-8345-3c5b8043679a | -4.69083 | -48.64035 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a74b0640-e9ef-3b03-a2bc-440632af8f00 | -7.12811 | -41.85502 | 2025-11-13 04:42:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb82d601-122e-343b-8d09-30dee407623e | -4.77877 | -46.44477 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d2b503c-3912-322e-b0dd-c5313dd091e8 | -6.10577 | -41.57888 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bdaf4c5a-6b60-3958-8bdd-945911057cf9 | -2.87014 | -51.46919 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc8176e7-42ef-38df-940a-08c6ebeebcfa | -5.644 | -41.07364 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7592f913-3283-3b7b-a387-b58fe1f6ddb5 | -3.15503 | -50.26517 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 546b9429-f0ae-361c-84c3-2bc2bd4c3ff7 | -4.45914 | -38.38815 | 2025-11-13 04:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f37d8c53-b0b2-3a16-a3ca-8f3072bf1810 | -5.66394 | -46.28626 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 890d7cd6-dec1-3848-ac96-40a23637322c | -4.93593 | -48.54677 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bc5bc78-2b94-3931-9870-c622f5e35e5e | -2.61744 | -49.21003 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c05154-0ad8-37ff-8384-7ff0f1f55527 | -2.86818 | -51.48122 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b170f58a-8a90-3249-a28c-935b8555c0b5 | -2.45036 | -49.25826 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 628b2d15-8804-3c63-a47c-85cc96822f46 | -4.26769 | -49.66591 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c4457d1-8f28-3ead-b7ac-68b2f6bca4fb | -7.30485 | -45.28274 | 2025-11-13 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5aab8e4-885e-393a-bfeb-1f0de26d535a | -3.08942 | -49.26672 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc061e9c-dcc6-3d35-8e0a-afe41f14d0e5 | -1.82921 | -53.80897 | 2025-11-13 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1b315b-219c-3aea-93d6-69bc61686351 | -3.78437 | -42.75493 | 2025-11-13 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd94adee-9d1c-3056-b143-3aefd754b0d2 | -3.46667 | -43.19131 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecd70593-9cb3-3d62-b556-bdd895e8ec77 | -6.10153 | -41.58617 | 2025-11-13 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d17ca5f0-1275-3ca6-ad8e-3b44113cc63a | -5.32463 | -45.19534 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c1f1177c-8a04-3369-ac6b-db216d5969b1 | -2.06638 | -56.62025 | 2025-11-13 04:42:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 257cbf75-bcb8-3022-91c9-1415329e0d1f | -7.13073 | -41.87215 | 2025-11-13 04:42:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dd070e33-2cb0-34ea-87b2-b382826e3b83 | -4.71792 | -46.44469 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 11c8c49c-4a27-30d8-80c5-cab8dcc9bcbe | -2.55655 | -51.2472 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eccbf3f5-c90d-37a7-b145-3ad06e7b7b46 | -3.08554 | -49.26966 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc309e71-577f-30fb-88b9-b2f25540c381 | -4.20327 | -50.09145 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fc6bb8-ba9b-3e87-81e6-513584ca67e7 | -3.78502 | -42.7531 | 2025-11-13 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1071fbc1-e1a3-3ef6-a353-fea043bd7ca0 | -6.35487 | -39.79679 | 2025-11-13 04:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 83142575-fb4b-3ebd-9d90-f47d85b052d1 | -5.12837 | -47.02917 | 2025-11-13 04:42:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 611494df-4d91-36a8-8530-d04b83bb2e33 | -7.22379 | -47.98584 | 2025-11-13 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea8c4ea-37ed-3467-95d0-149750959867 | -6.28965 | -41.73423 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b4df62f-7bfe-3fb8-9710-c61691964374 | -4.75233 | -48.83085 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d6e50d-f75c-3406-a9fe-b860a9102362 | -3.16071 | -50.62626 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd8b21e-891f-328f-88b4-a1adf99cbfe2 | -3.80179 | -44.4655 | 2025-11-13 04:42:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f3f187f-9329-3789-8ad9-7b827bd75681 | -2.89411 | -51.4565 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d93a68a8-da5c-3885-a9ee-5f3346c8dba4 | -7.8193 | -41.78246 | 2025-11-13 04:42:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 95befe73-2ed2-351b-8a90-185f6f4f5b7a | -7.45741 | -44.74219 | 2025-11-13 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2975d4d8-c71a-380a-b29e-b891a94da3f9 | -3.20744 | -43.47584 | 2025-11-13 04:42:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c6e30d7-8ccf-3310-b936-36bacd1dbfb7 | -5.6245 | -45.04083 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 725274fc-f314-3abb-9a07-26cb87fafd83 | -4.45858 | -46.55928 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a92cdff6-0a01-311e-a8bd-2af13e88d25d | -2.45647 | -49.26278 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e36e7765-00b2-3664-a3af-bae16687f800 | -3.07851 | -49.37896 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3a09bea-c58d-3c64-a6e2-c3aa46f634c4 | -4.6762 | -45.80192 | 2025-11-13 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77231ef8-e36a-3325-9eb1-1ecc22e3cc42 | -3.78364 | -52.16622 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
