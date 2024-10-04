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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3679aefd-60b3-33b1-848e-88aa136a66c1 | -6.4702 | -43.748501 | 2024-10-04 00:44:16 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56e25664-cdff-306b-b6aa-3172db505f05 | -8.0819 | -51.1255 | 2024-10-04 00:44:17 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3992558-1919-3616-9dc2-f07c916810b6 | -8.0701 | -51.118599 | 2024-10-04 00:44:17 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ae908b-d915-3c4d-b7e8-38ba6684d91e | -8.0721 | -51.127701 | 2024-10-04 00:44:17 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef676b4-55d9-3fe4-aa6c-deba3322612f | -8.0741 | -51.1367 | 2024-10-04 00:44:17 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06924c2e-ad49-3ed7-87f0-dc22b176ff2a | -6.2918 | -43.432098 | 2024-10-04 00:44:18 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb9f013f-ef93-37ec-8d0f-9084a7f9333c | -8.0114 | -50.897701 | 2024-10-04 00:44:18 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5447b4b3-507f-369c-a92c-aeb12e45df4e | -7.8267 | -50.5243 | 2024-10-04 00:44:19 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0833fdb-6dfe-3c48-96a2-cbda60c380b0 | -7.8286 | -50.5327 | 2024-10-04 00:44:19 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f04d6c-5a58-3928-8edf-4fb8f92fccb9 | -7.8304 | -50.5411 | 2024-10-04 00:44:19 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0465a25c-d5c0-31eb-ab98-a9b2d4364850 | -7.8169 | -50.526501 | 2024-10-04 00:44:19 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7651efc-9073-3043-bf5f-9bc8647d5531 | -7.8188 | -50.534901 | 2024-10-04 00:44:19 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddac8ce-18cc-31e7-976a-d9c3f4ac25a5 | -6.2517 | -44.133202 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4a64490-c2f9-3c43-be58-1e9767f88118 | -6.2537 | -44.1418 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd50e765-dd5b-30c1-aefd-6db8db899895 | -6.2399 | -44.1269 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a60416e2-38f4-3f5f-b594-322e87c20d7b | -6.242 | -44.135502 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 436dc3be-d9a8-380c-8e01-d50dd03d5474 | -6.244 | -44.1441 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4ca95e0-1ead-363c-a8c1-a623578b913c | -6.246 | -44.152699 | 2024-10-04 00:44:21 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9950893d-844a-3e05-a706-e68bad3feab2 | -7.1057 | -47.8592 | 2024-10-04 00:44:21 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 604a9a86-c331-384f-ac17-a9b5dc6fb4d4 | -7.1073 | -47.8661 | 2024-10-04 00:44:21 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce3f122d-34b6-30af-80aa-278825914e4c | -7.1088 | -47.873001 | 2024-10-04 00:44:21 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2ee810f-d94f-341a-aab7-2fca3a400ccb | -6.1987 | -44.127399 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c757b8d7-172b-3d6b-a823-3961851200c8 | -6.2007 | -44.136002 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f91746ee-23b3-3821-8a6a-d25a381ce6e1 | -6.189 | -44.1297 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 023fe9f4-4fe3-3c03-b022-9efc9bac57b0 | -6.1771 | -44.123299 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9f79fbc-9cb9-3bc6-ab86-9f63cfab0504 | -6.1792 | -44.132 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4bfe0d98-1975-3bee-8ea6-b06fee5865c0 | -6.1694 | -44.1343 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79b76315-49ed-339c-9300-b7a82a9e423e | -6.1714 | -44.142899 | 2024-10-04 00:44:22 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| baf9f131-a785-353f-92d8-91ec08e06726 | -6.1498 | -44.138802 | 2024-10-04 00:44:23 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0bc6a3e-81f8-3b8d-8e96-d083a8ec0f4a | -6.138 | -44.132401 | 2024-10-04 00:44:23 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d94b72c8-f095-3c1d-8a1d-6271a9120094 | -6.1401 | -44.141102 | 2024-10-04 00:44:23 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8f47d3e-2e23-31dd-8ec1-d2b6c6c784b9 | -6.1421 | -44.1497 | 2024-10-04 00:44:23 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d21264c-da37-3fb8-99e7-f0a9124cb3f4 | -6.2551 | -44.805302 | 2024-10-04 00:44:24 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 749e963f-8b5c-316e-a608-9da97beb5791 | -6.722 | -46.9482 | 2024-10-04 00:44:24 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04ccd925-7f05-385c-9613-dc523bc5a94c | -6.7236 | -46.955101 | 2024-10-04 00:44:24 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c22d490-b807-3960-b4bc-bef3ebea18a1 | -5.962 | -43.9986 | 2024-10-04 00:44:25 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84e8af3e-b304-38ef-b4e3-2197cbd0eac6 | -5.9739 | -44.005199 | 2024-10-04 00:44:25 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5267cce-13cb-309b-9dfd-d9d993ff3bcb | -5.9641 | -44.007401 | 2024-10-04 00:44:25 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1791d5-8747-371d-b5ca-31fc79218cf3 | -5.8892 | -43.865501 | 2024-10-04 00:44:26 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b8de931-2a82-36e4-8b27-b675637a6662 | -5.8914 | -43.874401 | 2024-10-04 00:44:26 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18bcf53a-c235-3ec8-9d65-cfbfb79bdc62 | -7.1312 | -49.155602 | 2024-10-04 00:44:26 | METOP-C | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8078b5ac-2185-32ed-8204-6a8b232267e9 | -7.1328 | -49.162899 | 2024-10-04 00:44:26 | METOP-C | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f57d5514-2eaa-309d-98e0-aa00f427b2a8 | -6.3251 | -45.678101 | 2024-10-04 00:44:26 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcf4d7cf-21be-3b8c-a981-fa3aa841ece5 | -6.3268 | -45.685501 | 2024-10-04 00:44:26 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 437787ad-18af-3d35-a05b-668f19eacb8a | -5.5932 | -42.923199 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c3a10ba-043d-3567-81f5-4351bf5ef673 | -5.5957 | -42.933498 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e428a95-573b-3fd6-bf5c-276964f3e100 | -5.5981 | -42.943699 | 2024-10-04 00:44:27 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 325ee8b1-c479-3ede-a6b8-3e3b85071477 | -5.5462 | -42.7696 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50c0863d-9873-3be1-88a2-88945e76877c | -5.5488 | -42.780201 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4673d23e-cfc8-35a3-8797-97f60dd632f1 | -5.5834 | -42.925499 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 313b15dc-454e-3e2c-8adb-236373ac998f | -5.5859 | -42.935799 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 452e600f-7435-34b0-b6dc-017bbf6ed001 | -5.5883 | -42.945999 | 2024-10-04 00:44:27 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5694573-60ad-3bf8-a60d-b9b1fc9278b4 | -5.5364 | -42.7719 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98ba053c-6476-346d-9188-a333d699ef0a | -5.539 | -42.782501 | 2024-10-04 00:44:27 | METOP-C | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d72faa1d-2c25-3de7-b621-23db80db7c49 | -6.7234 | -47.945099 | 2024-10-04 00:44:28 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bcb5917-7074-32a5-b80b-885e5cb614d9 | -6.725 | -47.952 | 2024-10-04 00:44:28 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8080154f-babe-3bb6-9141-85b099322d4e | -5.8242 | -44.113998 | 2024-10-04 00:44:28 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46b13ef3-010f-3e63-a8d5-b244bfee476f | -5.8263 | -44.1227 | 2024-10-04 00:44:28 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5181f62b-5750-37c5-b388-44c2da8e93ee | -5.8283 | -44.131401 | 2024-10-04 00:44:28 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0253950a-9de5-3845-80f7-219085e3c44f | -5.8144 | -44.116299 | 2024-10-04 00:44:28 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7084c2b-e3de-3f14-8a4f-6b482f10b9dc | -5.8165 | -44.125 | 2024-10-04 00:44:28 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4370b212-6a21-345c-830a-5201fabc0a4f | -5.8185 | -44.133701 | 2024-10-04 00:44:28 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 383c6889-ecc5-3ce7-8c91-46cfde9d2e67 | -6.3976 | -46.9272 | 2024-10-04 00:44:29 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9e78fa3-2643-372f-93fd-5e1d9ed0d07e | -5.5795 | -43.255001 | 2024-10-04 00:44:29 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| feea3cf6-f8ae-3a36-949b-7eeef3e42015 | -5.4052 | -42.912899 | 2024-10-04 00:44:30 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8698b052-784b-3bec-bb14-3747ea160c3b | -5.4077 | -42.923302 | 2024-10-04 00:44:30 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| e23bf1ba-ba7b-3a99-bfcf-c0ef591c8740 | -5.4101 | -42.933601 | 2024-10-04 00:44:30 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 83136b23-3200-39da-a756-7244c21a7753 | -5.398 | -42.925598 | 2024-10-04 00:44:30 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 9236bf5b-7007-3811-ab63-ebf65f9210d0 | -5.5584 | -43.731499 | 2024-10-04 00:44:31 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a91baade-3b16-39f5-85aa-5a990edc527a | -5.5606 | -43.7407 | 2024-10-04 00:44:31 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efc47002-5455-35f2-a1f2-a8da951072fb | -5.3053 | -42.9692 | 2024-10-04 00:44:32 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49204e77-9ab5-36c2-bec5-119827ac534f | -6.3282 | -47.4785 | 2024-10-04 00:44:32 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0f8b8c4-645a-330f-8e18-b60d87310e6b | -5.315 | -42.9669 | 2024-10-04 00:44:32 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| e6a5308e-c3af-3ada-b1f6-ca447c2607c5 | -5.3174 | -42.9772 | 2024-10-04 00:44:32 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| d88a8610-c162-37cc-a176-070515cc7279 | -5.7932 | -45.079102 | 2024-10-04 00:44:32 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e30b281d-7698-38a0-b723-a798360234ac | -5.795 | -45.087002 | 2024-10-04 00:44:32 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcbc125-f914-3f80-9d69-bc27e33f8590 | -5.7834 | -45.081402 | 2024-10-04 00:44:32 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e8a0d6b-669f-3bd2-a6ca-48c5354132e7 | -5.7852 | -45.089199 | 2024-10-04 00:44:32 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 006c2b2c-9bf9-3f61-909f-ab22bbd570fa | -5.8861 | -46.275398 | 2024-10-04 00:44:35 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f71a1ce3-95d3-35d5-80ed-ca3c46a11893 | -5.8877 | -46.2826 | 2024-10-04 00:44:35 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4464f734-40df-3f0f-bff5-6fd4c5156b00 | -6.147 | -47.4977 | 2024-10-04 00:44:35 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0e9c939-5860-3e32-a070-ac02012461c6 | -5.9827 | -47.455399 | 2024-10-04 00:44:38 | METOP-C | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b1dfe36-ac1d-32ba-87cf-0289ed721c8d | -5.5987 | -46.370998 | 2024-10-04 00:44:40 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d29060a-4d85-3c97-8f5c-da4f0ce0bed4 | -5.2982 | -45.168301 | 2024-10-04 00:44:40 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5073409d-1d46-3cc3-87db-a81062b26ae5 | -4.9284 | -43.770599 | 2024-10-04 00:44:41 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1d0491a-668f-3b61-bcfb-9cb5cee0cfb2 | -4.9306 | -43.7799 | 2024-10-04 00:44:41 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7541f777-e43b-331f-8b8f-160a67281920 | -4.7947 | -43.771999 | 2024-10-04 00:44:43 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 754b03ea-98dc-393f-aa09-3b3cb347c35a | -4.7969 | -43.781399 | 2024-10-04 00:44:43 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0853f68-1292-37a7-9c32-24a7f8992841 | -4.4595 | -42.878799 | 2024-10-04 00:44:45 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a496be6-e8c3-3520-aacc-14983bf4bf48 | -4.462 | -42.889599 | 2024-10-04 00:44:45 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c66a7e6f-da72-3eb1-9745-070b6c342503 | -4.4497 | -42.8811 | 2024-10-04 00:44:45 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdf59094-55ed-3978-ba64-6e875d7b5e75 | -4.4522 | -42.891899 | 2024-10-04 00:44:45 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62938619-3f48-303d-9798-a896ed318eb0 | -4.6912 | -43.726501 | 2024-10-04 00:44:45 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44bdb211-59e6-3d41-bed9-f9774d8d27fe | -5.4664 | -47.362598 | 2024-10-04 00:44:46 | METOP-C | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf6612a-10d6-3a6e-aba7-7386a0166e1f | -5.468 | -47.3694 | 2024-10-04 00:44:46 | METOP-C | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc71c67d-6143-3819-8621-d7fa8fec965f | -4.5385 | -43.298901 | 2024-10-04 00:44:46 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6d62a49-f0f9-33ad-a03a-74ae735f6bed | -4.5409 | -43.308998 | 2024-10-04 00:44:46 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e701fab6-4462-3ac7-bfce-b4146bd1135e | -4.5263 | -43.2911 | 2024-10-04 00:44:46 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 834573a5-305e-3f3a-b033-71f0b16f4c58 | -4.5287 | -43.301201 | 2024-10-04 00:44:46 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2894f3fb-b369-3b60-a035-1c581e2840ef | -4.5311 | -43.311199 | 2024-10-04 00:44:46 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
