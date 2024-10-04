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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d8587be-4102-3efc-ad5a-08e4ef778608 | -4.8149 | -42.76904 | 2024-10-04 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53a4b233-c5ba-32ac-991f-78969c7b4243 | -4.80953 | -42.76348 | 2024-10-04 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f6aef62-620b-3773-bd5c-4bbf54842d5c | -4.80889 | -42.76802 | 2024-10-04 04:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff126882-314b-3dda-8a15-9d1b0118a9e8 | -6.17306 | -43.21282 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8265f963-66e2-304d-8297-27630fc56f0a | -5.31843 | -42.97184 | 2024-10-04 04:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 676b8bf0-4ce0-313f-b418-935e66332bfd | -5.31779 | -42.97636 | 2024-10-04 04:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ca769a3-537d-3d9e-bd41-938002efd5ca | -5.31178 | -42.9756 | 2024-10-04 04:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 40bcf77a-2dbb-3817-b41e-b26b3c3b8223 | -6.40329 | -43.10279 | 2024-10-04 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f42235c7-9f77-396d-87c6-be7eb63868fe | -6.31394 | -43.4262 | 2024-10-04 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f032720-1143-34a5-810c-2a5577792ebe | -6.30803 | -43.42535 | 2024-10-04 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3868faa4-ebb3-3058-a772-26c8f066caa0 | -6.29387 | -43.44091 | 2024-10-04 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 193f1399-02c9-3a5c-8108-3aac073af299 | -7.75677 | -43.07022 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6c1e81be-b780-37cd-bb75-fa4a43d1f7b7 | -7.75619 | -43.07455 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0f416beb-55b8-33b4-9469-f8ff00cf5632 | -7.75059 | -43.06947 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 33595aa3-b04d-3a05-b372-cf38209d304d | -7.75002 | -43.07381 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5580f9b6-a8c9-33e6-b9ea-aa97be453e78 | -7.74503 | -43.06407 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 97a5c1ac-22b3-3d93-ad3c-5e33b00fc157 | -7.74444 | -43.06856 | 2024-10-04 04:55:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c7c36be1-bcec-3ad7-a037-efd22de28ccd | -7.69251 | -42.99042 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 15cf4032-43be-3efb-b5a7-cbe8a2e006da | -7.69195 | -42.9886 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 18a91138-e1df-3048-8012-e2d661866336 | -7.6919 | -42.99498 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 273f7d8d-e6f6-361a-bc07-361162532c84 | -7.69136 | -42.99321 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8486a88a-ec4e-3c54-8bc2-eca62cf1a131 | -7.68632 | -42.9896 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4439919f-bbfe-3f8f-abbc-bad6a979b75f | -7.68576 | -42.98774 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bdfd42f9-6d86-3064-a041-76c8a3804e3d | -7.68571 | -42.99416 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d984d96-432f-3ade-9ee5-bc6d29a7fd33 | -7.68517 | -42.99234 | 2024-10-04 04:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2180be9a-688b-353c-b0be-f474d50305e3 | -9.14764 | -43.15754 | 2024-10-04 04:55:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| debc9a9f-4c5b-3088-b1b6-39cd4adef415 | -9.14705 | -43.16239 | 2024-10-04 04:55:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d59aff7e-7939-3a7c-8f40-2dc656a42848 | -4.93264 | -43.77891 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2437b4bf-df01-305a-af6c-94c0da1cdbce | -4.93048 | -43.77572 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 223f8e78-607c-39fd-a182-d8c7a36dd706 | -4.92993 | -43.7795 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47911f6f-5d05-3632-aec6-921a1f42ff14 | -4.92749 | -43.77439 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11d0aa41-73fd-3647-8e3f-afeaa156a23f | -4.92696 | -43.77817 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a77c8b3-f4e8-3cdf-95c6-56c3b827f1de | -4.92427 | -43.77863 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bde7b898-7ac1-3859-b047-408902ce3ad7 | -4.53644 | -43.30664 | 2024-10-04 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e1907f02-1265-30ce-9c27-c0c6a1faa8e0 | -4.53585 | -43.31069 | 2024-10-04 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e0a01bd3-07c0-3676-a41b-7da82c653c4f | -4.53122 | -43.3017 | 2024-10-04 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f576502d-734b-3532-9ab3-1dee838265cf | -4.53064 | -43.30577 | 2024-10-04 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ac0d52a1-55cb-326d-bcb6-7f6527b88409 | -4.53005 | -43.30978 | 2024-10-04 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a93b5af6-416b-3e5a-89b3-481b6f0a7974 | -4.02418 | -43.23838 | 2024-10-04 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3e31140-5dd5-3eba-a0b7-1e1cd2711b05 | -4.01778 | -43.24166 | 2024-10-04 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a53272-031f-395d-aeed-9e8981d41a54 | -6.51934 | -43.91803 | 2024-10-04 04:55:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36634452-cc35-3031-8e7d-734fa6b162c2 | -6.1413 | -43.8207 | 2024-10-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5f5fad5-234e-3a2a-b132-93c5e12c2a64 | -6.14074 | -43.82476 | 2024-10-04 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30c2d4e9-de97-37de-b862-4647193b3b0e | -5.89695 | -43.87663 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca5087db-f452-3ef4-8c9d-e42cbe746cdb | -5.8964 | -43.88063 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c2a114-07a6-345b-ae52-2cfa3b783cbe | -5.8918 | -43.87174 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e2e87b5-b358-3232-bfaa-7b3044749c87 | -5.89126 | -43.87568 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 994bddea-ba49-36ae-830b-08fd1b3a5122 | -5.89071 | -43.8797 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8998ba3-7e9a-3540-a462-20f9b0e02216 | -5.88914 | -43.87538 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95175df9-1c64-3284-b03a-1aa4a429acee | -5.88856 | -43.8794 | 2024-10-04 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b7b5983-467f-315e-a811-a8dc23b207d2 | -5.56126 | -43.73516 | 2024-10-04 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e2fe647-48de-374f-aca1-e7dc2955d1e9 | -5.56071 | -43.73919 | 2024-10-04 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cca1ba6d-644a-3e06-942d-1a85d1af1b27 | -5.55981 | -43.73621 | 2024-10-04 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03680397-a5c1-3223-a089-9ddb507a9cae | -5.55924 | -43.74022 | 2024-10-04 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2dff2d-bfae-3bcf-a246-785d02813790 | -6.25232 | -44.14618 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60679b4-b4fc-3e0e-af29-f62388ff9927 | -6.25181 | -44.15002 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 133bb9b0-8bfb-391e-9b15-e8501c781b2a | -6.24915 | -44.14362 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6a9da1a5-70ed-38fa-8575-5b7d18cbce00 | -6.24861 | -44.14745 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58eb22a0-c8fa-3525-9a4f-8f008805dfe8 | -6.24809 | -44.15112 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 415d875e-fbc8-3064-bfde-dd10b2c1b293 | -6.24757 | -44.15483 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6415d104-62de-3ffe-a28c-46713afc6ed9 | -6.24409 | -44.13882 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b9522632-45ae-31a0-b70d-2a77f23d48a3 | -6.24353 | -44.14273 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60d67d9a-975b-316e-aca1-6f469041df3e | -6.20474 | -44.13263 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94e00387-70fe-3212-b677-7d62c54d8c9b | -6.20367 | -44.14032 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75f9c823-2c8a-3463-86c3-9ca4f75cd1ef | -6.19812 | -44.13897 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d96816e7-04e5-36e3-9e08-5b1bac058280 | -6.18125 | -44.13639 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a68f5a8-c9c7-3304-a3cb-7bcd1bc75238 | -6.17559 | -44.13581 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4666a9de-7707-3fa6-a324-7e313fd231f9 | -6.17512 | -44.13923 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eee1277f-dd9e-3561-ba31-ce2044a947d1 | -6.17467 | -44.14257 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f26239f-0751-3bf4-b6d1-c73824660c67 | -6.16947 | -44.13857 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45300900-9782-3458-a386-216b66c73fe2 | -6.16902 | -44.14193 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4581a5dd-8015-309c-afe4-f68adda90318 | -6.15108 | -44.14735 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d60dc2f0-65d6-3a52-9788-49237e293358 | -6.14764 | -44.14785 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79452675-c081-347d-94c6-3263c85f7269 | -6.1454 | -44.14698 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b22c8831-236d-396f-9e18-af57a7bed591 | -6.14349 | -44.13665 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7c120dd-03b3-3388-9f99-bcac3b2af74d | -6.14298 | -44.14024 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6aa69a98-0641-36ae-af27-82f354793453 | -6.142 | -44.14717 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0c32960-5adc-3ccd-bcb6-f0486cd64f1a | -6.13736 | -44.13943 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 865d5303-711b-3190-b7df-24dc66d187a3 | -5.97126 | -44.00772 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78381542-66d6-3dc3-9fb7-27b47634a68c | -5.96836 | -44.00624 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6b88156-86af-367d-8036-928f4e57b330 | -5.9678 | -44.01035 | 2024-10-04 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6922984-307b-3346-bd92-db4a0c30a413 | -5.82795 | -44.1289 | 2024-10-04 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7ac99f9-7b13-3b23-a798-f448230da50b | -5.82744 | -44.13267 | 2024-10-04 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49ff8877-93d9-3bbf-87d7-3f5c5417966d | -5.824 | -44.1282 | 2024-10-04 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1da4db95-eea1-37f5-8e2b-520cb693185e | -5.82346 | -44.13199 | 2024-10-04 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d1f223c-f7f2-36ad-b323-6224a11ef81f | -5.82292 | -44.13578 | 2024-10-04 04:55:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77cdea84-1066-3718-b65b-e5cc47f5ad0b | -5.8184 | -44.1274 | 2024-10-04 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf34142a-dd79-3c5e-8439-0cc4b9e77469 | -6.4018 | -44.7459 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 366aa1e3-a0e9-3e6f-875a-4beb29e491f2 | -6.39993 | -44.74487 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 234047c6-bc1b-3ffe-9726-c9e4d99fd4da | -6.39943 | -44.74833 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4dc21f4-3efe-3b98-a18b-1b55dc4b6c48 | -6.39642 | -44.74483 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d894d72-4a2b-30e7-bf52-b64608a32896 | -6.07425 | -44.71458 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b2ac37-80c4-32cc-a385-3993c34494de | -6.07379 | -44.71793 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9a889e-160a-3469-80d3-897225f35518 | -6.06739 | -44.63273 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c949e2b-901e-3d7f-86dc-fff6458e39f2 | -6.0669 | -44.63614 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 124e0b0e-3c34-31b5-b975-618e2abde1e8 | -6.06642 | -44.63952 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 27d96d50-c351-33c5-90b1-8f5738da5fb1 | -6.06194 | -44.63202 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd5e5ecd-419e-3d11-9461-688c731da354 | -6.06146 | -44.6354 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6d9dea1-7ef4-3f2a-981e-5c5ccbb1de1a | -5.42322 | -44.83432 | 2024-10-04 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee7d743-1941-3204-bbae-8119ff615491 | -5.42166 | -44.83429 | 2024-10-04 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README139.md)
