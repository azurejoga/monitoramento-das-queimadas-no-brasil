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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c2b5688-36c4-3365-aec5-123d5683f6f2 | -23.444 | -47.6894 | 2025-05-30 00:00:00 | GOES-19 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| f205da48-b207-32a3-ac55-2abe456e0f69 | -7.2405 | -43.0899 | 2025-05-30 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 6900fb83-44db-378a-a91d-696c11b34f8d | -7.6239 | -45.7447 | 2025-05-30 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4783d00c-b921-3118-85fe-45ec559b16fb | -11.9214 | -54.8117 | 2025-05-30 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9bf4d7d3-8949-3ba7-82e1-cb55cedfcbbc | -11.9211 | -54.8322 | 2025-05-30 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f47e5553-a912-3f8f-86e9-82b7e27feffb | -11.9211 | -54.8322 | 2025-05-30 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| dca46073-87c6-3512-87b4-0c5e6a481c37 | -7.6239 | -45.7447 | 2025-05-30 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b720a293-6793-32db-b16d-9892446be446 | -7.2405 | -43.0899 | 2025-05-30 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| d3769c61-a404-39e9-b6ba-96c7a1ed233d | -11.9214 | -54.8117 | 2025-05-30 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 50f00d06-0e0b-33b0-aa45-50bb5ce7848c | -4.9812 | -38.603802 | 2025-05-30 00:14:00 | METOP-C | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 22c4658b-0e85-346a-aed6-041d32af5cea | -6.2432 | -43.368401 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba9917a-02bb-3a84-88f4-b6923e1a44de | -6.5561 | -41.344601 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d769454-980f-3513-b28d-5091b7bda79e | -5.0521 | -43.246498 | 2025-05-30 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8e1ad8b-0b3d-35cd-a7bf-d438611b0b4c | -7.1843 | -43.113899 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7dc3f8ab-7771-3742-914e-6e4fa30a7e55 | -4.9792 | -38.595402 | 2025-05-30 00:14:00 | METOP-C | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9897f841-27a4-3177-88f5-23bf5a29c6c3 | -11.7924 | -44.278599 | 2025-05-30 00:14:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 220dfb38-0f60-33fd-9ceb-dddbcc0c40d5 | -15.9062 | -43.4646 | 2025-05-30 00:14:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c95388b-0272-3d04-83c9-fbac85ccbc35 | -7.5794 | -45.8722 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f707324-e684-3367-a2d5-42609f1224f4 | -10.4503 | -47.960499 | 2025-05-30 00:14:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8addd8fc-7c5b-3624-9657-3b08560da597 | -7.2431 | -43.100899 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 835827c2-aa89-352c-acd0-55d7fcf867ae | -11.7963 | -44.297001 | 2025-05-30 00:14:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a590a45-808e-3720-8517-32384354c559 | -7.2415 | -43.0937 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88326d24-95a0-3483-8843-af8ea72b38ff | -7.5707 | -43.323002 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc64d65-6cbf-33a6-ba64-a89dd0e62627 | -6.3414 | -43.392799 | 2025-05-30 00:14:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df3251df-26fc-3cbd-95ef-66eb0b2b5f6e | -7.181 | -43.0994 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a40e2d27-21ff-390c-809f-c364b7f01d56 | -7.0859 | -46.051399 | 2025-05-30 00:14:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5bb5bd6-c4e7-3d2b-a95e-69ac5291845a | -7.9982 | -45.678902 | 2025-05-30 00:14:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87e6576b-6fa7-3cba-bc73-f339c054cdcc | -8.548 | -46.4235 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 689a8e15-23ca-3afb-8a58-87bdf3a0ceee | -7.2398 | -43.086399 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c26be6c2-57e3-36f8-a0f5-0a749f2c4cbe | -7.6323 | -46.115101 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86936536-3e07-3fde-bbe6-e3d138c900c1 | -12.0068 | -49.518501 | 2025-05-30 00:14:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38ea0400-ea57-3d8f-9e78-bc2df3d0681f | -7.6242 | -45.748901 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71545473-fe2a-3c5d-b3cf-a53b212c8678 | -7.6264 | -45.758701 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d048313-54cb-32e2-bdc6-676e28e20b25 | -5.212 | -43.315899 | 2025-05-30 00:14:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9c09d67-4fc4-3577-805d-06aac822b675 | -10.46 | -47.9585 | 2025-05-30 00:14:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63582f0c-2d9c-3564-8643-c80d1c58e0c7 | -12.0108 | -49.538898 | 2025-05-30 00:14:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5aa858b-9d78-30f5-af2e-2c872375656d | -7.569 | -43.315498 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d06cf74c-9231-3374-a1ca-26c6264d0f9e | -7.5871 | -45.9543 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd11530-5077-31c7-a7b6-5bb51d388d98 | -9.3478 | -40.208099 | 2025-05-30 00:14:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 594b3e5b-c847-3806-bfb7-c9d9fc54a614 | -6.2465 | -43.382999 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 797c9bc2-197b-392a-bd53-c8fd21eca693 | -7.6053 | -43.386101 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d36aa1c7-67a6-3124-9953-034553ed2389 | -7.9529 | -46.1772 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8ca1217-bfb6-3779-9e02-308cbb915e22 | -5.2104 | -43.3088 | 2025-05-30 00:14:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46d0b276-491d-30d6-83b5-ad8362393b7c | -7.5298 | -43.3241 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afa6682f-3dc1-363a-a1d0-717bb1c47221 | -7.6144 | -45.750999 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4d06c3-5f80-3787-ab77-f7263f405822 | -6.3495 | -43.383301 | 2025-05-30 00:14:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee89a1b6-dcec-385d-bea9-02869215acd9 | -6.5577 | -41.351501 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa6688b9-6be6-379b-9218-fce5ffd4de82 | -7.0837 | -46.041401 | 2025-05-30 00:14:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce09750-7cab-30b2-86a6-ba215befe7d7 | -5.6454 | -43.592999 | 2025-05-30 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1ab69d0-c0e8-370c-80d4-d80d062b2b9c | -5.5897 | -43.574501 | 2025-05-30 00:14:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53da0480-5d73-3ff1-878c-39e58fadd414 | -7.5893 | -45.964401 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 831b8f09-11a3-3a2e-b1a4-f63021b36c94 | -7.5315 | -43.3316 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5a79cfd-e47c-384f-a816-3bef1b25f962 | -6.6884 | -44.160702 | 2025-05-30 00:14:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5264004-1f12-3718-b0ca-83b80ca209a3 | -13.2917 | -39.869598 | 2025-05-30 00:14:00 | METOP-C | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1fc30266-2a36-3c33-92ec-19c786bfbda6 | -8.1958 | -49.813999 | 2025-05-30 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b7851f-d57f-3df0-bc99-b3983dfff29e | -7.0061 | -44.618301 | 2025-05-30 00:14:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0f1db9-c1f4-3563-b4dd-d843e6bcc5fb | -15.3243 | -43.072899 | 2025-05-30 00:14:00 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a4fdfc22-d749-3074-b8f3-16baa44e98bf | -15.3262 | -43.081799 | 2025-05-30 00:14:00 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| c63a3cf8-8780-3a23-bf5a-602923c119d7 | -4.8943 | -37.535099 | 2025-05-30 00:14:00 | METOP-C | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4eed869d-5cbe-3ea3-80eb-c176bbab582d | -11.4503 | -49.1008 | 2025-05-30 00:14:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad08dde2-1127-30b5-ba0c-3e8949db49a9 | -10.4569 | -47.943501 | 2025-05-30 00:14:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb5e22a4-f111-3073-8cab-2b2ecb1da1ed | -11.814 | -44.2836 | 2025-05-30 00:14:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b69ce29-dcef-3122-b538-f53ddbc5f7e1 | -11.4466 | -49.0821 | 2025-05-30 00:14:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7236d93-b456-3a56-8537-0d0c42263329 | -6.3397 | -43.385399 | 2025-05-30 00:14:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8e13c0f-7195-38d3-bc6f-c339b1cedbff | -9.2461 | -48.865601 | 2025-05-30 00:14:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 132202fb-591a-332b-a005-6cf2f30bbadc | -8.192 | -49.7953 | 2025-05-30 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4313fc27-a999-3b8f-9b2b-e3eb05ff0743 | -8.8157 | -46.004299 | 2025-05-30 00:14:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b882ba38-b72e-306d-8801-2170db552691 | -7.5849 | -45.944199 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61665014-0480-3502-89fb-9ad378cad30f | -7.6221 | -45.739101 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd326613-5cdd-3641-bb33-bb422cc5cbfe | -11.7944 | -44.2878 | 2025-05-30 00:14:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1933b00d-6f1e-3423-b4ab-28fd3a4873d4 | -10.4472 | -47.945499 | 2025-05-30 00:14:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d00a091e-f84f-365b-88d3-95693f25130a | -12.2603 | -44.604401 | 2025-05-30 00:14:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aba308af-aa66-37fa-bde1-032d3221503e | -5.7845 | -43.616402 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 213cb95a-fe8c-314c-84a2-be16d717905d | -7.5494 | -43.319801 | 2025-05-30 00:14:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23dc9d1e-4e26-3894-947d-703835d62bcf | -6.9854 | -42.779499 | 2025-05-30 00:14:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 495da9f3-17b8-3314-8457-8b63c35cf349 | -12.2624 | -44.614201 | 2025-05-30 00:14:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe7259c3-7429-366b-9ae2-477f4624eb59 | -3.9583 | -41.4828 | 2025-05-30 00:14:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db79db07-83d8-3a95-ba5f-ee06bf1cbd90 | -6.2448 | -43.375702 | 2025-05-30 00:14:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30a1ef2c-fd25-34df-80ce-bf41518dd2b2 | -7.2317 | -43.095901 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5471124-6d8e-376c-824d-a6173e4e3886 | -11.794 | -47.379799 | 2025-05-30 00:14:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 744af564-3601-3c21-8ab5-f697e74adf92 | -6.3381 | -43.378101 | 2025-05-30 00:14:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 019183a8-b803-352a-a3c8-5dc46aa3065a | -7.5772 | -45.862202 | 2025-05-30 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84d22da7-3cce-3151-8468-767d277eec20 | -7.6102 | -45.731499 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 308d98a1-bde9-3be2-9923-11b49ef6394d | -8.0003 | -45.688702 | 2025-05-30 00:14:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a48bb6cd-fe31-3908-8333-f6180907f412 | -9.2559 | -48.863602 | 2025-05-30 00:14:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70293b55-63bb-340a-92a5-5e2f4598cbc3 | -18.376801 | -44.519901 | 2025-05-30 00:14:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf19c18e-6608-3d92-84bc-fd3eb640423f | -7.2447 | -43.108299 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fde38d73-2b80-3121-a030-af0ce558c8e2 | -12.0165 | -49.516602 | 2025-05-30 00:14:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f74ee62-df2a-3625-abdf-a357ab430252 | -7.1827 | -43.106701 | 2025-05-30 00:14:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f4cef98-c2d5-3fae-ac18-76a2fb15c010 | -7.6123 | -45.741199 | 2025-05-30 00:14:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef090b1a-272b-3536-88fe-250d1eb34f3b | -7.2405 | -43.0899 | 2025-05-30 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 662f55cc-4ded-322e-9ccc-31f4a630e5fb | -11.9214 | -54.8117 | 2025-05-30 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 48e76a13-39db-39cf-8d56-d0bebb4b9581 | -11.9211 | -54.8322 | 2025-05-30 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 034a8455-9d1a-3cf9-ac1b-39fa2b575340 | -7.6239 | -45.7447 | 2025-05-30 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a67d1920-bf66-39a3-b46d-53a5e94f8fa8 | -11.4508 | -49.0961 | 2025-05-30 00:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ab0e6a3c-eb7f-3bcc-b0d2-bca853e819bb | -11.9214 | -54.8117 | 2025-05-30 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0c3c5782-427d-315c-8d56-d33f205a5613 | -11.9211 | -54.8322 | 2025-05-30 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ae3291c5-bf45-3be3-8aaa-639fae7e3267 | -7.2405 | -43.0899 | 2025-05-30 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 59fbdc18-bd06-3fdb-af7f-bc6b78834709 | -7.2405 | -43.0899 | 2025-05-30 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| d49d7eb1-6cfe-3c20-8a8c-667a5bf5f5f3 | -7.2405 | -43.0899 | 2025-05-30 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |


[Clique aqui para ver as próximas entradas](README2.md)
