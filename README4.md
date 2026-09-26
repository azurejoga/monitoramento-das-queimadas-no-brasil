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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9cf721d-23d8-303f-8e9c-6b6ab46fa565 | -12.9047 | -61.714401 | 2026-09-26 01:36:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c008d704-fda3-3551-8be0-c1547326163c | -11.8266 | -50.542999 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5a4c967-0c51-337c-b20b-4715c60baf08 | -12.2541 | -50.298801 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcc27625-e1ed-38ca-9069-b84a0ebc37b2 | -12.2811 | -50.321899 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1065f3cd-8dfc-3fa7-bdb7-d921657db5a3 | -17.041401 | -56.585499 | 2026-09-26 01:36:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4dcfd48a-1171-3e43-a176-bd15d09d145f | -11.278 | -54.430801 | 2026-09-26 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 065f6ab7-669d-30dd-84a0-60f42fcb7eeb | -12.2524 | -50.330101 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec353156-62c8-373c-98c0-bcb37122eda5 | -12.2637 | -50.296101 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74e75165-2dd6-31b6-bbb7-4b39c2441d7a | -12.2986 | -50.347698 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62e85828-d21e-3c5b-83ac-a83f1534f717 | -29.1318 | -55.623199 | 2026-09-26 01:36:00 | METOP-C | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | nan |
| b79170d9-4e88-311b-af07-10231d04fcbd | -12.262 | -50.3274 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7123e7c7-5996-3f49-a982-22e9b4c1ad16 | -11.8684 | -65.0261 | 2026-09-26 01:36:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4778fad-25e4-39a5-bb87-573b03e7986e | -12.2716 | -50.324699 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b254eaeb-f83e-3788-9acb-06046459154c | -11.282 | -54.446499 | 2026-09-26 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3ed90e-e9ed-38ee-b521-558ee5ff6072 | -12.2907 | -50.319199 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e81fbb6-8c4e-3503-b086-539de10109e6 | -13.4547 | -61.320801 | 2026-09-26 01:36:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ffe3502-6db1-3334-88b0-a6fa843a704f | -23.7686 | -53.221298 | 2026-09-26 01:36:00 | METOP-C | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d8e4068-1ce2-37ba-841e-1282926e52f9 | -12.235 | -50.304199 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 482df654-62f4-3902-9d51-268de7f6a31c | -12.289 | -50.350399 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed7422fe-797d-31b7-8110-a029b9b8ba68 | -12.2795 | -50.353199 | 2026-09-26 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b16d6a5-c8b0-3c19-bda6-4f157f70128e | -11.9037 | -50.5961 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fa86f134-ab22-3f44-beba-c491a11101db | -12.0175 | -50.6256 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 02c57e99-865f-3f5f-8713-306713f5372d | -16.5732 | -43.9798 | 2026-09-26 01:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 15c79ac9-6285-3bee-a682-596814b8bfde | -5.7756 | -45.0826 | 2026-09-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b3dcf7f9-2f41-37fc-9e45-52cd11365968 | -5.7754 | -45.1053 | 2026-09-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d02cce8d-9b20-31a5-aa6a-b79a8cd61314 | -5.7571 | -45.0613 | 2026-09-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1b9aa8f7-5e3d-3879-8ab5-b1524b459779 | -12.0171 | -50.647 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| c59b2e88-2c6c-3bb7-934e-45fbd6294700 | -11.9228 | -50.5938 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dca382f0-0a43-3bb2-9f7e-590b0336a4ed | -12.289 | -50.3143 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a76057e1-ecb2-3440-bc01-b88f0dc07df6 | -12.0362 | -50.6448 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e7663454-dec0-31ad-b89a-73c49432cf85 | -12.0365 | -50.6233 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8ab4c978-175e-3d65-85c8-711f7d664931 | -5.7384 | -45.0626 | 2026-09-26 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 5b569ce5-f1b4-3e5f-a54f-9256a1c05908 | -12.2887 | -50.3358 | 2026-09-26 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f3c67612-88fd-3cc5-99de-36b69613241a | -3.2728 | -50.1372 | 2026-09-26 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 820bc6bd-d3da-326a-b524-4c029e85cf7f | -3.2727 | -50.1583 | 2026-09-26 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| fca07c8a-7a5a-3b80-93b2-867fe8ec4048 | -4.2951 | -49.1234 | 2026-09-26 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 4b0c07c9-00c5-3b58-947f-15a38ed02cc8 | -12.0175 | -50.6256 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d68ab2f2-4a9a-3d57-a0f0-d75ac0443e5d | -12.0365 | -50.6233 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0c7fa456-80fb-3c6f-b5ac-39293087a5bd | -11.9231 | -50.5724 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 44e34c27-cf6b-365d-93e9-9ace3d425212 | -12.0362 | -50.6448 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 6d510767-7b09-36e9-923c-10ed6d432e68 | -5.7571 | -45.0613 | 2026-09-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f6722386-c3a6-37a0-8d7c-ec502a253c77 | -4.295 | -49.1448 | 2026-09-26 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c2ae14c1-361a-3dc4-8d8a-cd01c48e6bb8 | -11.8284 | -50.5406 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ca02dc89-7fab-34e7-9796-aac62476ce31 | -3.2728 | -50.1372 | 2026-09-26 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 8315fe4f-e0ba-3036-aa01-7ddd94958a54 | -11.904 | -50.5746 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| dae54305-0d16-3c94-b3ce-32a6e7b4113d | -5.7384 | -45.0626 | 2026-09-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8b9daf11-a8aa-3ba1-8dc9-620c5f71209a | -11.9228 | -50.5938 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 60d73e5f-2678-3a96-a744-f30790fcdf46 | -12.0171 | -50.647 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 60e9553c-0bd5-3860-b466-062e7604c941 | -5.7756 | -45.0826 | 2026-09-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| edf04780-577e-31b1-bc8d-6305cc6b6c27 | -5.7754 | -45.1053 | 2026-09-26 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 24d6c133-b27b-3d2d-9a7a-a9a96f0d947e | -11.9037 | -50.5961 | 2026-09-26 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 34fc29c5-50b4-3d96-af54-0ffd29f268ee | -3.2727 | -50.1583 | 2026-09-26 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 60d9651b-19f0-3287-b642-4f7e9aca4282 | -5.7756 | -45.0826 | 2026-09-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c9204fc7-309b-3da8-b99f-06231feff2c0 | -12.0175 | -50.6256 | 2026-09-26 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 88067bfb-5c05-342d-bc7c-878b7a48db30 | -12.0362 | -50.6448 | 2026-09-26 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| f7cadcde-2260-364f-92b7-b7841c7797b1 | -4.3137 | -49.1226 | 2026-09-26 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c3a8fb99-4547-3e52-9dc2-2c566451fffb | -12.0365 | -50.6233 | 2026-09-26 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 8b99ffa1-3f77-3ada-8c05-5e7912fbe90e | -5.7384 | -45.0626 | 2026-09-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ae91b95e-abee-3bd4-81ba-c7e67b712279 | -5.7571 | -45.0613 | 2026-09-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1f635a4b-75e3-304b-bce8-af9b65653b6e | -7.3656 | -42.0819 | 2026-09-26 02:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| ac3bb165-fcec-3199-ac5e-7df0eaf6d003 | -11.9365 | -38.2942 | 2026-09-26 02:00:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| ad8c1f93-dce5-3f9d-911b-b3a53202cecc | -4.2951 | -49.1234 | 2026-09-26 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b7385001-554c-37ee-a9c4-847c7d038c80 | -4.295 | -49.1448 | 2026-09-26 02:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 891796f0-748e-3414-8ae7-b5666d789cf5 | -3.2728 | -50.1372 | 2026-09-26 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| c72c56c7-d002-300b-a05d-735d87fb1c8d | -5.7382 | -45.0853 | 2026-09-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d9d18cc3-2657-3a53-b002-06a9e0959707 | -12.0553 | -50.6425 | 2026-09-26 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c1d5f78d-97b3-338d-a31a-60238433d924 | -12.0556 | -50.6211 | 2026-09-26 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 546bbd7a-af51-376a-9dd5-0c2cfaf199f4 | -7.3467 | -42.0839 | 2026-09-26 02:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 26f7b980-9a89-3132-88af-d0292565a5ea | -5.7754 | -45.1053 | 2026-09-26 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| da5c06f9-f631-3811-b8bd-f5da90fd22a5 | -14.8192 | -43.3141 | 2026-09-26 02:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 6160340c-de27-3310-b9cc-feb32964e375 | -12.0365 | -50.6233 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 05674c62-d51c-3d85-8d5b-dc8fde234048 | -4.2951 | -49.1234 | 2026-09-26 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 82372908-3f01-364e-84ff-352ec13fb717 | -7.3467 | -42.0839 | 2026-09-26 02:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| d1622ae6-ee25-30c2-bce3-4a23c55afc9c | -11.9231 | -50.5724 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 59fd76d9-5a02-399a-986e-b92dfb551e81 | -11.904 | -50.5746 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5606728a-0bd7-3a70-8483-591273eb07a6 | -12.0556 | -50.6211 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 63143294-f6c1-355e-9bc3-07b5fd9e7be2 | -5.7569 | -45.084 | 2026-09-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b85e15fd-1bd9-33c5-9a9e-66ff139aff5a | -5.7384 | -45.0626 | 2026-09-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7ce99bf5-c434-3697-bf99-da8df08f3628 | -12.0362 | -50.6448 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 1e41d8ba-0792-3b50-a21c-776106937f4d | -5.7571 | -45.0613 | 2026-09-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| addafb01-4ebe-3847-9b46-846e3abbf434 | -5.7756 | -45.0826 | 2026-09-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8b57823f-0b5e-33c2-9593-08d7f77bed7a | -12.0175 | -50.6256 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c11ac25b-1c11-3224-99f2-df9c3b836156 | -11.9037 | -50.5961 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 45a6c9eb-991f-30cd-9547-901e2dd86ae7 | -4.3137 | -49.1226 | 2026-09-26 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d76a4405-1a74-357f-87c7-ae0b58f85476 | -3.2728 | -50.1372 | 2026-09-26 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| ed6bf8c6-d5a0-3f3e-91db-8ada2a76f183 | -12.0553 | -50.6425 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 6d9acd1e-c975-34de-abfe-7a2e8109ed1a | -7.3656 | -42.0819 | 2026-09-26 02:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| d8583944-c458-349a-861d-8e40b100d486 | -3.2727 | -50.1583 | 2026-09-26 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c153d249-8786-3c77-a7aa-5ea9f50f45c1 | -4.295 | -49.1448 | 2026-09-26 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d8dc4c07-ff4e-367e-8a34-ebdd074eba67 | -11.9228 | -50.5938 | 2026-09-26 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 74e9592f-2092-3d43-b7a6-464d9be361ed | -5.7754 | -45.1053 | 2026-09-26 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b4ae2814-a870-371e-aac7-06865154f8ef | -11.9231 | -50.5724 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b84527dd-a40a-3c64-b4df-172fe2dd83a5 | -5.7384 | -45.0626 | 2026-09-26 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 0954c0b1-7fe0-3f0b-905c-68807c3b61e4 | -12.0365 | -50.6233 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 7ef4c602-70a8-32e4-85c7-c687008ab0aa | -11.9228 | -50.5938 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| bbcb40a8-dca1-3ff1-b367-78a372c89069 | -12.0556 | -50.6211 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 7f5425ef-d5cb-377f-b9b1-89fecf0e84ea | -3.2728 | -50.1372 | 2026-09-26 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b9ba448d-10cb-399c-96b2-7ad6fac47156 | -3.2727 | -50.1583 | 2026-09-26 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1ac39adc-07c9-3498-9fcb-dd3cc4d1b1ad | -12.0553 | -50.6425 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ccc95f4b-84e2-3b0d-81f9-4ffe5ec85261 | -11.9365 | -38.2942 | 2026-09-26 02:20:00 | GOES-19 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |


[Clique aqui para ver as próximas entradas](README5.md)
