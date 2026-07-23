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
| 351a9dfc-7179-3ec6-8939-3fe8a9e32ec0 | -11.80792 | -47.12562 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| c02a39b8-a5ed-3530-8e5c-a36aedd14d8f | -11.89807 | -50.38225 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 3612d757-edcb-31bf-8cbe-3ad9f9ea658d | -11.88959 | -50.37286 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f695f4a7-79ff-331a-ac23-db9acf262ddb | -9.12199 | -61.06004 | 2026-07-23 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7460c2f5-74f0-3527-8b59-66f8e0cbfef0 | -8.67208 | -54.59567 | 2026-07-23 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 60e28a1b-8cfb-310c-ad8b-6a33d4630400 | -10.80968 | -50.45053 | 2026-07-23 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| fe2135f7-0c01-3c95-9421-65ea685e407a | -10.89631 | -51.09552 | 2026-07-23 00:37:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4c16a042-ed63-3104-8e02-f0f1a9de2c30 | -9.1238 | -61.07424 | 2026-07-23 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5055cd1e-9126-3e2a-a0a2-6ad3f0a049f6 | -9.1256 | -61.08845 | 2026-07-23 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e603692e-b5ea-3246-989a-7832d0112fcd | -9.16891 | -58.31263 | 2026-07-23 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 67281971-dd70-3863-8c70-4ed76cc8afbc | -10.89647 | -51.10497 | 2026-07-23 00:37:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4143ff1c-fc17-3f82-b8ab-11a1b9846358 | -5.7554 | -49.08468 | 2026-07-23 00:37:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 71d0f767-9ebc-3db9-9322-4d9486290b99 | -10.80227 | -50.44533 | 2026-07-23 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| dbbff08a-8b46-3132-a0ee-623f9d23c592 | -11.34471 | -62.22425 | 2026-07-23 00:37:00 | TERRA_M-M | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a89d19fd-bd5a-33e5-be12-0fe45db16f28 | -11.33223 | -62.22588 | 2026-07-23 00:37:00 | TERRA_M-M | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4207b653-bdfc-3a62-ab2d-06b65b2c7e03 | -2.42011 | -60.01251 | 2026-07-23 00:39:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60f33d38-19a5-3d6a-b93c-15dbb9e592c7 | -2.8497 | -54.48854 | 2026-07-23 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5eec121f-57af-3142-b202-8613448c23e6 | -4.45983 | -61.04995 | 2026-07-23 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2b59ec91-b95c-3f17-ae58-876f0e8add91 | -1.63687 | -53.58361 | 2026-07-23 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 167ea19a-f12e-38df-b033-f7d81d08c826 | -11.6792 | -50.3437 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 670a75ca-4f49-31a8-a20b-54200f09c842 | -11.8066 | -47.1082 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 203fc400-645d-33a8-aafb-de63d296d07e | -18.8004 | -51.2417 | 2026-07-23 00:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 0fa90cab-02dd-31e8-8fc6-f22725c52ff1 | -11.6983 | -50.3415 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 599b9a39-e07b-3ece-8cdf-93b348059a65 | -11.7687 | -47.0909 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 74b7e795-d278-389f-85fe-d82fb939d9f1 | -11.7738 | -50.3756 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 76426b7a-bc24-3bfd-8597-7611ce0a7faa | -11.6602 | -50.3459 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 54cb91e5-c3b8-35d3-9566-dbcc5eb043fd | -14.3919 | -58.3361 | 2026-07-23 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 18f23e23-a7bb-3386-a383-d0680201174d | -11.7875 | -47.1108 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 61f7832e-ed75-37d8-b2f2-1c0f44966ad3 | -11.9069 | -50.3815 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 13e642bd-f79e-347c-8ce7-dcd79b22b32a | -11.7683 | -47.1134 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b5191797-41d3-3a5c-8a7f-074fcf9c0b52 | -11.698 | -50.3629 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 40a458bc-36d3-397e-986e-71e36d139cab | -11.807 | -47.0858 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6898f126-28c7-3cc8-8f51-a64f710ba471 | -11.8879 | -50.3837 | 2026-07-23 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 04e7dc9a-01ea-386b-880c-000f811ef22a | -11.7879 | -47.0884 | 2026-07-23 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 225.4 |
| ed92dbb2-3d90-332e-8a43-d87f71a3b2ac | -11.8033 | -47.096401 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbcd07fa-5320-3b2e-a4c6-cd129498ae8b | -11.6276 | -50.3158 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef8a885e-46b5-3839-ac09-bcf3ee888544 | -5.6327 | -47.097599 | 2026-07-23 00:42:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15ef5f01-a849-3806-a0eb-17b600a21ca4 | -11.7096 | -50.3619 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2fccb6-61a0-3063-abda-fc79937bcf44 | -11.8994 | -50.384602 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29da9639-f43e-336e-85d7-b552e5099717 | -11.9173 | -50.372601 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad5f0319-f3f6-3299-8e3b-c8480d8aae67 | -20.1677 | -43.917801 | 2026-07-23 00:42:00 | METOP-C | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b28b3811-8008-326b-8a68-18f8b66942a6 | -11.6637 | -50.339901 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdd0d302-e745-3624-a13d-2525b485cebf | -11.9876 | -50.3652 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a89e63ba-f30a-3863-9d3a-fa6084d1ac9f | -11.608 | -50.320099 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6eaccbb-d8c8-389e-bca3-b3ab1be14ddc | -11.9467 | -50.3661 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fce7b1bd-1086-38b5-be40-35652cd36837 | -8.8059 | -49.375999 | 2026-07-23 00:42:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0074f12-7391-3c08-99bb-9f80e51586f3 | -8.8385 | -48.338402 | 2026-07-23 00:42:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 236c8dd7-eeeb-34e1-b789-cb9ebcf1af5c | -11.6293 | -50.323399 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d01f2988-9426-32dc-9f9f-99397f09da95 | -12.0268 | -50.356499 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a9284e2-c4e0-3d41-bd68-ddc2084d0133 | -7.8891 | -46.905102 | 2026-07-23 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7273a41-11b4-3158-a033-46abcb2e91c8 | -5.1056 | -41.720001 | 2026-07-23 00:42:00 | METOP-C | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c196f1df-19bf-3f2b-a4b7-ba1feb8c31b1 | -11.8879 | -50.379101 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59231190-cfa7-3357-b191-4a57148868c8 | -12.8509 | -44.380199 | 2026-07-23 00:42:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a83d9b59-3e5a-3eaa-8202-de16af146901 | -7.0123 | -45.4118 | 2026-07-23 00:42:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc108a0f-ac4f-3b1b-bd2d-f9b62d11603e | -20.1658 | -43.909901 | 2026-07-23 00:42:00 | METOP-C | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6134acf-90cf-340f-a2ad-a30005ccb361 | -18.7887 | -51.253899 | 2026-07-23 00:42:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 64466971-b927-36be-9921-96849905c84e | -12.0349 | -50.346699 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53455cac-96cd-3bcc-bf73-81abf2ca4525 | -11.7112 | -50.369598 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d0f8f37-438f-3020-b139-e88655a97cf3 | -7.0125 | -45.849899 | 2026-07-23 00:42:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b59b2472-4ac4-31e6-a702-42b2959bbfe0 | -11.8977 | -50.3769 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 387b16fa-4932-3509-81c4-3de20a922565 | -12.017 | -50.3587 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31d2a5d0-8484-337e-b9b1-38d03eeaab7a | -11.6998 | -50.363998 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1dbc620-5953-36ab-9555-fea0a880b743 | -18.7964 | -51.241402 | 2026-07-23 00:42:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb78c49c-bc14-360b-a71c-d713ba96eec7 | -17.5832 | -47.506802 | 2026-07-23 00:42:00 | METOP-C | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62183f3f-09e8-3c73-a162-e3605e4e7d5b | -10.8042 | -50.449501 | 2026-07-23 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7db080b9-fe16-3bcd-9e35-5396f7601ad4 | -11.9156 | -50.364899 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 323d888e-37ad-34e5-a75f-47d332963339 | -6.3044 | -43.6549 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5ce617a-645e-3991-8664-d5c70ff05668 | -5.1517 | -47.6031 | 2026-07-23 00:42:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1c5562f-752d-3cfb-b7ae-894ddf6b01a7 | -8.8367 | -47.074699 | 2026-07-23 00:42:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1986ae6-0d97-38d4-a785-dedfb5ece218 | -11.7854 | -47.108101 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71db3b0f-f9de-3f39-9b64-3e2eb07b3ca7 | -8.8369 | -48.331501 | 2026-07-23 00:42:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54b95b05-e102-32cf-8ab5-757c1f82d9d6 | -5.7593 | -49.077599 | 2026-07-23 00:42:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce94737-9f35-3262-82d1-5f326ee7e9e0 | -19.708401 | -48.077301 | 2026-07-23 00:42:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43500ff6-08f5-3888-b66e-885a3c59ad8d | -19.7101 | -48.085098 | 2026-07-23 00:42:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b590136d-1596-3bae-942a-dde8c4474c9c | -4.8387 | -44.074001 | 2026-07-23 00:42:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19ae982b-6eed-3ea2-991f-bee521171f37 | -11.7968 | -47.1129 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5369d23f-dcda-33f5-be24-94857370d2cb | -11.685 | -50.343201 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7094eb-f2f8-394f-8a7e-73a27048e25e | -11.9974 | -50.362999 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35c59ce3-f595-3846-b3cc-9aa4638e5075 | -12.0186 | -50.366402 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6615b91f-f45a-3ce0-8866-cbb4ef372e35 | -12.0284 | -50.364201 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7184c8e-68fd-3fcd-84b3-8e1a044ae1c1 | -11.9157 | -43.8452 | 2026-07-23 00:42:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd7bb9c0-eeb3-32ed-8674-a3a275a20c19 | -11.8143 | -47.3246 | 2026-07-23 00:42:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec749a69-6679-3dfb-9380-19e56bcf4ad6 | -12.0088 | -50.368599 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cee4b072-e3e1-3100-bc29-5ed8bd814b5d | -7.8873 | -46.897598 | 2026-07-23 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd6fd5db-a088-3a62-8afa-3291d90268b1 | -11.6964 | -50.348701 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b60735b-c7d1-3919-8810-c2836ff766a4 | -11.9433 | -50.3507 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fee2554-76bc-3b30-bda6-c07e944ea56d | -11.7619 | -50.366402 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 377db4ca-871c-3a74-bc0e-c283c7cebd62 | -11.5737 | -48.400299 | 2026-07-23 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 594a0005-d5b1-36f8-b3df-dd626c49e96f | -11.7963 | -50.383099 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9675a888-e6f5-39fb-99a9-452d977c2232 | -11.6768 | -50.353001 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5172c3-decb-3854-8191-c82561ebb627 | -11.7636 | -50.3741 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77ea2bcc-b873-3458-8d4a-ea112a626cac | -9.4166 | -40.310501 | 2026-07-23 00:42:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 151060cc-5239-393a-b838-6944b5634102 | -12.0072 | -50.360802 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c26111c-4bf0-3454-a235-ae3583be4421 | -11.9629 | -50.346401 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5067b703-2a2c-378d-8a8d-3b5138bfd660 | -11.7821 | -47.093899 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09ad1791-c91d-3288-9395-13aed450fcc8 | -6.3142 | -43.6525 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 230b6442-687e-3665-9142-dc735a0bb33d | -11.6735 | -50.3377 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2dff59af-aa2c-38b4-9e04-328952d0a5fd | -11.7832 | -50.369801 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7d07bff-f491-34af-af54-544a17265596 | -12.0366 | -50.354401 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de13f643-dff7-3449-8e3e-48fd59207e77 | -12.454 | -49.583401 | 2026-07-23 00:42:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
